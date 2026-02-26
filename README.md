# easyar-llm-docs

把 EasyAR 爬取文档整理成：
- 清洗后的基础文档（`easyar_docs`）
- 人类可读的分层手册（`easyar_docs_structured`）
- 可直接喂给 LLM 的 Markdown 输入包（`easyar_docs_pack`）

## 基础目录

- `easyar_docs/*.md`：清洗后的扁平文档
- `easyar_docs/repair_report.json`：清洗修复报告

## 一键执行（2 步）

```powershell
python tools/restructure_easyar_docs.py --input easyar_docs --output easyar_docs_structured
python tools/build_easyar_pack.py
```

## 输出目录

- `easyar_docs_structured`：按主题/路径重组后的可读文档目录
  - `README.md`：阅读说明
  - `SUMMARY.md`：目录总览
  - `TOPICS.md`：主题索引
- `easyar_docs_pack`：给 LLM 的输入包
  - `easyar_full.md`：全量单文件
  - `by_topic/*.md`：按主题分卷

## 建议用法（喂给 LLM）

- 全量场景：直接提供 `easyar_docs_pack/easyar_full.md`
- 定向场景：只提供 `easyar_docs_pack/by_topic/<topic>.md`

推荐提示词：

```text
你是 EasyAR 开发助手。请先阅读我提供的文档内容，
回答时给出：1) 结论；2) 关键步骤；3) 引用的章节路径与 source URL。
若文档中无明确信息，请明确说明“文档未覆盖”。
```
