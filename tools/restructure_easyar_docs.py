#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
import re


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


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


def file_to_relpath(filename: str) -> Path:
    stem = filename[:-3] if filename.endswith(".md") else filename
    prefix = "doc--zh-cn--develop--"
    if stem.startswith(prefix):
        stem = stem[len(prefix) :]
    parts = [p for p in stem.split("--") if p]
    if not parts:
        return Path(filename)
    if len(parts) == 1:
        return Path(f"{parts[0]}.md")
    return Path(*parts[:-1]) / f"{parts[-1]}.md"


def first_h1(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def topic_from_rel_path(rel_path: str) -> str:
    first = rel_path.split("/", 1)[0]
    return first[:-3] if first.endswith(".md") else first


def write_summary(output_dir: Path, docs: list[dict[str, str]]) -> None:
    lines = [
        "# EasyAR 文档目录",
        "",
        "本目录按原始 URL 路径重组，适合人类阅读和按主题跳转。",
        "",
    ]
    by_top: dict[str, list[dict[str, str]]] = {}
    for d in docs:
        top = topic_from_rel_path(d["rel_path"])
        by_top.setdefault(top, []).append(d)

    for top in sorted(by_top):
        lines.append(f"## {top}")
        for d in sorted(by_top[top], key=lambda x: x["rel_path"]):
            lines.append(f"- [{d['title'] or d['rel_path']}]({d['rel_path']})")
        lines.append("")

    (output_dir / "SUMMARY.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_topics(output_dir: Path, docs: list[dict[str, str]]) -> None:
    lines = [
        "# Topic 索引",
        "",
        "用于快速定位专题文档与 LLM 分卷输入。",
        "",
    ]
    topic_count: dict[str, int] = {}
    for d in docs:
        top = topic_from_rel_path(d["rel_path"])
        topic_count[top] = topic_count.get(top, 0) + 1

    lines.append("## 主题统计")
    for topic, count in sorted(topic_count.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{topic}`: {count} 篇")
    lines.append("")
    lines.append("## 主要主题说明")
    lines.append("- `unity`：Unity 插件、组件、快速入门、调试与模拟。")
    lines.append("- `wechat`：微信小程序与 Mega/CRS 相关能力。")
    lines.append("- `native`：原生 SDK 接入与版本说明。")
    lines.append("- `web`：Web 端云识别与接入。")
    lines.append("- `mega` / `cloud-recognition` / `motion-tracking` 等：能力专题。")
    lines.append("")

    (output_dir / "TOPICS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_readme(output_dir: Path, docs: list[dict[str, str]]) -> None:
    lines = [
        "# easyar_docs_clean",
        "",
        "这是从爬取文档清洗重组后的可读版本。",
        "",
        "## 怎么看",
        "- 从 `SUMMARY.md` 按目录跳转阅读。",
        "- 从 `TOPICS.md` 按主题选择文档。",
        "- 每篇文档 frontmatter 保留 `source` 便于回溯原始页面。",
        "",
        "## 文档数量",
        f"- 共 {len(docs)} 篇。",
        "",
    ]
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def run(input_dir: Path, output_dir: Path, manifest_file: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    docs: list[dict[str, str]] = []

    for path in sorted(input_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        rel_path = file_to_relpath(path.name)
        dst = output_dir / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(raw, encoding="utf-8")

        docs.append(
            {
                "title": first_h1(body),
                "rel_path": rel_path.as_posix(),
                "source": meta.get("source", ""),
                "original_file": path.name,
            }
        )

    write_summary(output_dir, docs)
    write_topics(output_dir, docs)
    write_readme(output_dir, docs)
    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    manifest_file.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Restructured {len(docs)} docs -> {output_dir}")
    print(f"Manifest: {manifest_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Restructure EasyAR docs into readable folders.")
    parser.add_argument("--input", default="easyar_docs_clean_flat", help="Input normalized flat docs dir.")
    parser.add_argument("--output", default="easyar_docs_clean", help="Output structured docs dir.")
    parser.add_argument(
        "--manifest",
        default="easyar_docs_clean/manifest.json",
        help="Output manifest json path.",
    )
    args = parser.parse_args()
    run(Path(args.input), Path(args.output), Path(args.manifest))


if __name__ == "__main__":
    main()
