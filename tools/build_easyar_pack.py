#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


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


def first_h1(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def topic_from_rel_path(rel_path: str) -> str:
    first = rel_path.split("/", 1)[0]
    return first[:-3] if first.endswith(".md") else first


def collect_docs(clean_dir: Path) -> list[dict[str, str]]:
    docs: list[dict[str, str]] = []
    skip = {"README.md", "SUMMARY.md", "TOPICS.md"}
    for path in sorted(clean_dir.rglob("*.md")):
        rel = path.relative_to(clean_dir).as_posix()
        if rel in skip:
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        docs.append(
            {
                "rel_path": rel,
                "source": meta.get("source", ""),
                "title": first_h1(body) or rel,
                "body": body.strip(),
            }
        )
    return docs


def write_full_pack(pack_dir: Path, docs: list[dict[str, str]]) -> None:
    lines = [
        "# EasyAR 文档全集（LLM 输入包）",
        "",
        "本文件由清洗后的文档自动拼接而成。",
        "建议提示词：先根据目录定位章节，再结合章节原文给出答案，并标注“章节路径 + source URL”。",
        "",
        "## 目录",
    ]
    for d in docs:
        lines.append(f"- `{d['rel_path']}`")
    lines.append("")

    for d in docs:
        lines.extend(
            [
                "---",
                "",
                f"## {d['title']}",
                f"- 章节路径: `{d['rel_path']}`",
                f"- 来源: {d['source']}",
                "",
                d["body"],
                "",
            ]
        )
    (pack_dir / "easyar_full.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_topic_packs(pack_dir: Path, docs: list[dict[str, str]]) -> None:
    by_topic: dict[str, list[dict[str, str]]] = {}
    for d in docs:
        topic = topic_from_rel_path(d["rel_path"])
        by_topic.setdefault(topic, []).append(d)

    by_topic_dir = pack_dir / "by_topic"
    by_topic_dir.mkdir(parents=True, exist_ok=True)

    for topic, items in sorted(by_topic.items()):
        lines = [
            f"# EasyAR 专题包：{topic}",
            "",
            "适用于上下文长度有限时的分卷输入。",
            "",
            "## 目录",
        ]
        for d in items:
            lines.append(f"- `{d['rel_path']}`")
        lines.append("")
        for d in items:
            lines.extend(
                [
                    "---",
                    "",
                    f"## {d['title']}",
                    f"- 章节路径: `{d['rel_path']}`",
                    f"- 来源: {d['source']}",
                    "",
                    d["body"],
                    "",
                ]
            )
        (by_topic_dir / f"{topic}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_pack_readme(pack_dir: Path, docs: list[dict[str, str]]) -> None:
    topics = sorted({topic_from_rel_path(d["rel_path"]) for d in docs})
    lines = [
        "# easyar_docs_pack",
        "",
        "## 文件说明",
        "- `easyar_full.md`：全量文档单文件，可一次性喂给大模型。",
        "- `by_topic/*.md`：按主题分卷，适合上下文受限或定向问答。",
        "",
        "## 主题列表",
    ]
    for t in topics:
        lines.append(f"- `{t}`")
    lines.extend(
        [
            "",
            "## 建议提示词",
            "```text",
            "你是 EasyAR 开发助手。请先阅读我提供的文档内容，",
            "回答时给出：1) 结论；2) 关键步骤；3) 引用的章节路径与 source URL。",
            "若文档中无明确信息，请明确说明“文档未覆盖”。",
            "```",
            "",
        ]
    )
    (pack_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def run(input_dir: Path, output_dir: Path) -> None:
    docs = collect_docs(input_dir)
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    write_full_pack(output_dir, docs)
    write_topic_packs(output_dir, docs)
    write_pack_readme(output_dir, docs)
    print(f"Built pack for {len(docs)} docs -> {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build LLM-friendly markdown packs from structured docs.")
    parser.add_argument("--input", default="easyar_docs_clean", help="Input structured docs directory.")
    parser.add_argument("--output", default="easyar_docs_pack", help="Output pack directory.")
    args = parser.parse_args()
    run(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
