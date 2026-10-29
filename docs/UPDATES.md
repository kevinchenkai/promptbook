# PromptBook editions / 版本说明

## 2026-10-29 — Five-stage game collaboration follow-up

**360 → 365 templates · 18 categories · 58 tags · 730 language versions**

Added one complete **Design → Art → Implementation → Acceptance → Release** workflow, alongside the ten existing task chains. Five new stage-specific handoffs (`17-19`, `18-19`, `17-20`, `17-21`, `18-20`) provide full Chinese and English instructions. Each states the suggested owner, required evidence, output files, gate, and rework route. Existing 360 prompt bodies and IDs remain unchanged.

The workflow uses a common OUTPUT directory and explicit file handoffs. The web UI shares six in-memory parameters across these five prompts, keeps evidence and release fields stage-specific, offers direct language-specific copying and complete TXT downloads, and preserves template-only favorites exports. Downloaded workflow packs contain current values and are intended for one-stage-at-a-time use.

`game-workflow.json` defines the ordered stages and six game-specific routes. [docs/GAME_WORKFLOW.md](GAME_WORKFLOW.md) is generated from the same data and exact bilingual prompt bodies as the offline website. No additional private session material is published. Human decisions, art acceptance, independent review, and release authorization remain explicit. Tools do not message other sessions or create agents automatically.

Validation covers registry order/references/modes, bilingual parameters, original-prompt preservation, shared-value isolation/reset, direct-copy target selection, workflow downloads, generated-guide freshness, script syntax, and deployed artifact equality. Playwright is not run for this update.

## 2026-10-29 — Game development and recent workflows

**300 → 360 templates · 18 categories · 58 tags · 720 language versions · 10 workflows**

### What was reviewed

- User instructions in local Codex and Claude sessions during **2026-10-24–2026-10-29, America/Los_Angeles**.
- Earlier GameAI conversations and user-authored game requirements, covering Star Fighter, Soulmate, Wulin Tavern, Journey Ludo, Garden Match, and StackPop. These are supplemental game sources, **not new activity within the recent window**.
- Existing public templates, compared by task, action mode, inputs, and acceptance criteria before adding new entries.

Only reusable user task intent is published. Original messages, dates tied to specific conversations, session identifiers, local paths, host details, credentials, and assistant replies remain outside the public handbook. Pasted assistant execution reports are not treated as human-authored instructions. Some concrete engineering constraints are editorial additions, not verbatim historical requirements.

### Added coverage

| Category | Added IDs | Count | Focus |
| --- | --- | ---: | --- |
| Git, sync and archiving | 05-19–05-23 | 5 | Backup manifests, resumable transfers, completeness, throughput experiments, ETA |
| GPU environments | 07-19–07-21 | 3 | Explicit compatibility policy, evidence inventory, portable jobs |
| Training operations | 08-19–08-20 | 2 | Sequential GPU checks and CPU evaluation handoff |
| Models and evaluation | 09-19–09-24 | 6 | Prompt parity, preprocessing fail-fast, scoring definitions, pass@k, output axes, quality/latency |
| Documents | 11-19–11-23 | 5 | Incremental reports, title ownership, upstream patch plans, section ownership, activation references |
| Agents and tools | 16-22–16-24 | 3 | Shared skill resolution, concise skill routing, session organization |
| **Game design, mechanics and levels** | **17-01–17-18** | **18** | Shooter/board/puzzle/dialogue rules, legal actions, solvability, level generation, casual difficulty, saves and playtests |
| **Game art, audio and delivery** | **18-01–18-18** | **18** | Artwork/coordinate contracts, asset integration, icon size, density, iOS audio, first load, exports and bounded deployment |

The two dedicated game categories contain 36 templates. An additional collaborative retrospective template (11-22) also draws on game-development work.

### Deduplication and editing

- Existing **300 IDs, titles, task bodies, bilingual text, parameters, and origins are preserved**. Favorites and previous links retain their meaning.
- Repeated acknowledgements, progress requests, and “continue/deploy yet?” variants do not become separate templates.
- Wrapped tool instructions, injected skill text, generated heartbeat instructions, and copied assistant receipts are excluded as instruction sources.
- Existing general templates remain the entry points for generic coding, DPR, art delivery, and test planning. New game entries focus on distinct constraints such as shared runtime/solver rules, background-to-coordinate contracts, nested texture scaling, or audio lifecycle behavior.
- Chinese and English are rewritten for matching action scope and acceptance criteria. Dates, machine addresses, project-specific thresholds, and model names become parameters where appropriate.
- `curation.json` contains public template IDs and editorial labels only. Private evidence links are kept in the ignored `.local/` directory and are not deployed.

### Validation scope

Checks cover input structure, duplicate identifiers/titles/bodies, bilingual placeholders, editorial mappings, original-template preservation, frontend script syntax, game/workflow template references, public-content privacy, generated-file freshness, and deployed artifact consistency. **Playwright is not run for this edition.** No claim is made that every template has been tested on a model or improves quality in an A/B comparison.

## 中文摘要

本版新增 60 条，按任务意图去重，并非将最近会话原句直接翻译后发布。游戏专题来自六款项目的既有用户要求，和最近六天的工程任务分开说明时间范围。保留原有 300 条的正文与编号，新增游戏玩法和美术音频两类，以及首页六款游戏入口和两条游戏流程。

重点沉淀：规则先确认、关卡可解性与超预算未知状态、轻松难度、多层坐标与缩放、iOS 音频解锁、存档撤回一致性，以及只发布当前子项目的边界。源会话、助手回执和私人连接信息不进入公开仓库或网站。
