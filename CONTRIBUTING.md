# Contributing / 贡献指南

Thank you for improving PromptBook. Prefer a useful, distinct scenario over a larger prompt count. Issues and pull requests may be written in Chinese or English.

## Add or improve a template

1. Find the closest category in `recipes/`. Each nonempty line is a record with seven `¦`-separated fields:

   ```text
   Chinese title¦English title¦Mode¦Comma-separated keywords¦Editorial search terms¦Chinese task¦English task
   ```

2. Use a concrete task with necessary inputs, a bounded action, and an observable result. Avoid generic personas, promises of perfect performance, hidden-reasoning requests, fixed thinking durations, or fictional tool access.
3. Write Chinese and English with the **same meaning, placeholders, permissions, and acceptance criteria**. Use existing `{{PARAMETER}}` names from `build.py`. Generic paths and placeholders are appropriate; real credentials, private chat, session IDs, and identifying infrastructure details are not.
4. Choose a mode: `R` read-only, `P` plan only, `E` local edits, `M` remote changes, `D` deliverable creation, or `C` an explicitly authorized Git action. Shared boundaries and category checks are added by the builder. A planning template must not require execution; a read-only template must not require changes.
5. Preserve existing IDs: **append within a category; do not reorder or delete records casually**. IDs are referenced by favorites and workflows. Discuss an ID migration before a structural change.
6. For a referenced method, verify the exact upstream license and version, record the file/commit/mapping in `references.json`, update `docs/SOURCES.md` and notices, and retain required license text. Public visibility is not permission. Do not import unlicensed prompts or assume a data corpus shares its repository code license. Use `method-reference-original-wording` only when that describes the relationship accurately.
7. Update documentation counts and the content date (`meta.generated` in `handbook.json`) when appropriate, then rebuild:

   ```bash
   python3 build.py
   python3 build.py --check
   node --check ui.js
   git diff --check
   ```

`--check` validates input shape, unique IDs/titles/bodies, bilingual parameter parity, reference mappings, and generated-file freshness without writing files. It does not judge translation quality or model performance.

## UI changes

Use `python3 -m http.server 8000 --bind 127.0.0.1` to preview. Check desktop and mobile, search/filter/empty states, parameter substitution, both languages, copy, favorites, exports, and public references. Filled parameters must remain in memory and must not appear in favorites exports. Keep the existing favorites storage key unless there is an explicit migration.

The published `index.html` must remain self-contained: no runtime fetch, external fonts, API key, backend, analytics, or build requirement for readers. Preserve the content security policy. Render user values as text rather than HTML.

## Pull request expectations

Describe the user scenario, concrete change, evidence checked, and anything unverified. Avoid unrelated formatting or refactors. For new templates, include why existing entries do not already cover the task. Tests should target meaningful behavior, not merely mirror implementation.

Contributions are provided under this project's MIT license, subject to retained upstream notices. Do not submit confidential employer or client material.

## 中文要点

- 新模板要有独立、常用的任务场景，不为凑数量重复改写。
- 中英文执行含义、参数和权限必须一致；公共边界由构建脚本补齐。
- 保留已有编号与收藏兼容性；新增条目追加，不随意重排。
- 开源参考必须核对许可并保留固定版本和出处；不发布私人聊天和真实凭据。
- 运行构建与检查，说明实际验证内容，不把未执行的模型评测说成通过。
