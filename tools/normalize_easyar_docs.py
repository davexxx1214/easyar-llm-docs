#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
CALLOUT_RE = re.compile(r"^#{5}\s*(注意|警告|小心|提示|重要事项)\s*$")
TITLE_SUFFIX_RE = re.compile(r"\s*\|\s*EasyAR\s*文档\s*$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data, text[m.end() :]


def fix_pipe_stream_table(lines: list[str]) -> tuple[list[str], bool]:
    if "## 数据访问情况列表" not in "\n".join(lines):
        return lines, False
    if "|---" in "\n".join(lines):
        return lines, False
    if sum(1 for l in lines if l.strip() in {"|", "||"}) < 20:
        return lines, False

    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip() == "## 数据访问情况列表":
            start = i + 1
            break
    if start is None:
        return lines, False

    for i in range(start, len(lines)):
        if lines[i].startswith("注："):
            end = i
            break
    if end is None:
        end = len(lines)

    seg = lines[start:end]
    cells: list[str] = []
    buf: list[str] = []
    row_breaks: list[int] = []

    for line in seg:
        s = line.strip()
        if s in {"|", "||"}:
            if buf:
                cells.append(" ".join(x.strip() for x in buf if x.strip()))
                buf = []
            if s == "||":
                row_breaks.append(len(cells))
        else:
            buf.append(line)
    if buf:
        cells.append(" ".join(x.strip() for x in buf if x.strip()))

    if len(cells) < 8:
        return lines, False

    headers = cells[:7]
    data = cells[7:]
    rows: list[list[str]] = []
    row: list[str] = []
    for cell in data:
        row.append(cell)
        if len(row) == 7:
            rows.append(row)
            row = []
    if row:
        row = row + [""] * (7 - len(row))
        rows.append(row)

    suspicious_first_cells = {
        "访问/传输",
        "访问",
        "软件功能",
        "不适用",
        "使用 TLS",
        "否",
        "是",
    }
    is_suspicious = any(r and r[0] in suspicious_first_cells for r in rows)
    if is_suspicious:
        fallback = [
            "",
            "> **注意** 自动修复提示：该表格在抓取阶段已损坏，以下保留原始表格流供人工核对。",
            "",
            "```text",
            *seg,
            "```",
            "",
        ]
        merged = lines[:start] + fallback + lines[end:]
        return merged, True

    table_lines = [
        "",
        "|" + "|".join(headers) + "|",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for r in rows:
        table_lines.append("|" + "|".join(x.replace("\n", " ").strip() for x in r) + "|")
    table_lines.append("")

    merged = lines[:start] + table_lines + lines[end:]
    return merged, True


def normalize_body(body: str) -> tuple[str, dict[str, int]]:
    stats = {
        "removed_noise_lines": 0,
        "callouts_rewritten": 0,
        "code_tick_lines_removed": 0,
        "table_recovered": 0,
    }
    body = body.replace("\r\n", "\n")
    body = html.unescape(body)

    lines = body.split("\n")
    out: list[str] = []

    first_content_seen = False
    in_code = False
    code_first_line = False

    for raw_line in lines:
        line = raw_line
        stripped = line.strip()

        if stripped in {"**", "##### Table of Contents"}:
            stats["removed_noise_lines"] += 1
            continue

        if not first_content_seen and stripped:
            first_content_seen = True
            if not stripped.startswith("#") and TITLE_SUFFIX_RE.search(stripped):
                stats["removed_noise_lines"] += 1
                continue

        if stripped.startswith("```"):
            in_code = not in_code
            code_first_line = in_code
            out.append(line)
            continue

        if in_code and stripped == "`":
            stats["code_tick_lines_removed"] += 1
            continue

        if in_code and code_first_line:
            lstripped = line.lstrip()
            if lstripped.startswith("`") and not lstripped.startswith("```"):
                indent_len = len(line) - len(lstripped)
                line = (" " * indent_len) + lstripped[1:]
                stats["code_tick_lines_removed"] += 1
            code_first_line = False

        m = CALLOUT_RE.match(stripped)
        if m:
            out.append(f"> **{m.group(1)}**")
            stats["callouts_rewritten"] += 1
            continue

        line = re.sub(r"`（([^`]+)）`", r"（\1）", line)
        line = re.sub(r"^\*\s*>\s*", "> ", line)
        line = re.sub(r"^\*\*>\s*", "> ", line)

        out.append(line)

    out, fixed = fix_pipe_stream_table(out)
    if fixed:
        stats["table_recovered"] += 1

    compact: list[str] = []
    blank_count = 0
    for line in out:
        if line.strip() == "":
            blank_count += 1
            if blank_count > 1:
                continue
        else:
            blank_count = 0
        compact.append(line.rstrip())

    text = "\n".join(compact).strip() + "\n"
    return text, stats


def build_frontmatter(meta: dict[str, str], source_file: str) -> str:
    source = meta.get("source", "")
    normalized_at = dt.datetime.now().strftime("%Y-%m-%d")
    lines = [
        "---",
        f"source: {source}",
        f"original_file: {source_file}",
        f"normalized_at: {normalized_at}",
        "---",
        "",
    ]
    return "\n".join(lines)


def run(input_dir: Path, output_dir: Path, report_file: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_file.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.md"))
    report = {
        "total_files": 0,
        "total_removed_noise_lines": 0,
        "total_callouts_rewritten": 0,
        "total_code_tick_lines_removed": 0,
        "total_tables_recovered": 0,
        "files": [],
    }

    for path in files:
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        normalized, stats = normalize_body(body)
        frontmatter = build_frontmatter(meta, path.name)
        final_text = frontmatter + normalized

        out_path = output_dir / path.name
        out_path.write_text(final_text, encoding="utf-8")

        report["total_files"] += 1
        report["total_removed_noise_lines"] += stats["removed_noise_lines"]
        report["total_callouts_rewritten"] += stats["callouts_rewritten"]
        report["total_code_tick_lines_removed"] += stats["code_tick_lines_removed"]
        report["total_tables_recovered"] += stats["table_recovered"]
        report["files"].append(
            {
                "file": path.name,
                **stats,
            }
        )

    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Normalized {report['total_files']} files -> {output_dir}")
    print(f"Report: {report_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize EasyAR markdown docs.")
    parser.add_argument(
        "--input",
        default="easyar_docs",
        help="Input directory of raw markdown files.",
    )
    parser.add_argument(
        "--output",
        default="easyar_docs_clean_flat",
        help="Output directory of normalized flat markdown files.",
    )
    parser.add_argument(
        "--report",
        default="easyar_docs_clean_flat/repair_report.json",
        help="Output report json path.",
    )
    args = parser.parse_args()
    run(Path(args.input), Path(args.output), Path(args.report))


if __name__ == "__main__":
    main()
