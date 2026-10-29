# 游戏开发完整工作流 / Game development lifecycle

策划 → 美术 → 编码 → 验收 → 发布 / Design → Art → Implementation → Acceptance → Release

本文件由 `game-workflow.json` 与指令正文自动生成；请修改源文件后运行 `python3 build.py`。 / Generated from the workflow registry and prompt sources; edit those and rebuild.

网站入口 / Website: [打开五阶段工作流](https://g.ismayday.com/tools/promptbook/#game-workflow)

## 使用与分工 / Usage and ownership

人类负责产品决策、主观体验和最终发布授权。建议 Claude 做策划与独立验收，Codex 做美术与编码；也可互换，须以当前会话真实工具能力为准。 / The human owns product decisions, experiential acceptance, and release authorization. Suggested roles: Claude for design/independent review and Codex for art/implementation. Roles are interchangeable and depend on actual session tools.

每次发送当前阶段的一种语言版本，完成后把交付路径交给下一会话；阶段不会自动执行、派发消息或创建代理。 / Send one language for the current stage, then pass its artifact paths to the next session. Nothing runs, messages another session, or creates agents automatically.

`{{OUTPUT}}` 在本流程中必须填写目录，例如 `docs/game-workflow`，并在五阶段保持一致。目录示例是约定结构，不表示文件已经存在。 / Fill `{{OUTPUT}}` with a directory such as `docs/game-workflow` and keep it consistent across stages. Example paths are contracts, not claims of existing files.

网页在五阶段间共享 PROJECT、GOAL、FILES、OUTPUT、TESTS、SCOPE；INPUTS 和发布连接参数按阶段填写。值只存在当前打开期间，复制或导出完整流程使用当前填写值；收藏导出仍只含原始模板。 / The UI shares PROJECT, GOAL, FILES, OUTPUT, TESTS, and SCOPE across these five stages. Fill INPUTS and release connection fields per stage. Values are memory-only; copying/downloading the workflow includes current values, while favorites exports retain original templates.

SCOPE 在前四阶段写本阶段的允许操作，发布前再明确提交、推送和部署授权。已有策划、素材或验收证据应由人类补充确认；仅出现路径不能证明已批准。 / Use SCOPE for stage-specific allowed work, then explicitly authorize commit, push, and deployment before release. Human confirmation and actual evidence are required; a path alone does not establish approval.

| 阶段 / Stage | 指令 / Prompt | 交付 / Handoff |
| --- | --- | --- |
| 1. 策划 / Design | 17-19 | `01-design.md` |
| 2. 美术 / Art | 18-19 | `02-art/`, `02-art-manifest.json`, `02-art-review.md` |
| 3. 编码 / Implementation | 17-20 | `03-implementation.md` |
| 4. 验收 / Acceptance | 17-21 | `04-acceptance.md`, `04-checks/` |
| 5. 发布 / Release | 18-20 | `05-release.md` |

## 1. 策划 / Design · 17-19

**建议分工 / Suggested owner:** 建议 Claude；也可由 Codex 负责 / Suggested: Claude; Codex can also lead

**输入 / Input:** 玩法想法、目标玩家、设备、参考与现有代码约束 / Game idea, players, devices, references, and code constraints

**通过条件 / Gate:** 规则无硬冲突，最小版本、素材契约与验收标准已由人类确认。 / Human confirmation of feasible rules, minimum scope, art contracts, and acceptance criteria.

**返工 / Rework:** 规则或需求冲突留在策划阶段解决。 / Resolve rule or requirement conflicts in design.

### 中文指令

```text
工作目录：{{PROJECT}}
任务：你负责本轮游戏策划，目标为 {{GOAL}}。先读项目规则及 {{INPUTS}}，按 {{FILES}} 与 {{SCOPE}} 核对可用技术和范围；把 {{OUTPUT}} 视为本流程交付目录，只写其中的 01-design.md。文档说明目标玩家、设备与画幅、核心循环、合法动作、状态与胜负规则、关卡或对话数据、最小版本和非目标；用具体例子消除规则冲突。把 {{TESTS}} 转为玩法、美术、代码、真机及发布的验收矩阵，写明素材清单、尺寸与锚点契约、实现里程碑和不改动的内容。末尾给美术与编码方各一份独立交接：必读文件、冻结决定、待决问题、允许写入路径及完成条件。输出本轮结论和需要人类决定的实质分歧；完成本阶段后交接，不自动出图、编码、发送消息或创建代理。

执行边界：本轮只调研和给方案，不实施、不改代码或环境；如指定方案文件，只写该文件。

验收与交付：按本条执行模式交付规则、改动或方案，明确胜负与状态不变量；只报告实际取得的验证证据，模拟指标不能替代真人试玩。
```

### English prompt

```text
Working directory: {{PROJECT}}
Task: You own this design stage for {{GOAL}}. Read project rules and {{INPUTS}}, then check available technology and boundaries against {{FILES}} and {{SCOPE}}. Treat {{OUTPUT}} as the workflow handoff directory and write only 01-design.md there. Specify target players, devices and aspect ratios, the core loop, legal actions, states and outcomes, level or dialogue data, minimum release, and non-goals; resolve rule conflicts with concrete examples. Turn {{TESTS}} into an acceptance matrix for gameplay, art, code, device checks, and release. Define assets, dimensions and anchors, implementation milestones, and frozen scope. End with separate self-contained art and coding handoffs: required reading, frozen decisions, open questions, allowed write paths, and completion criteria. Report substantive decisions requiring human input. Hand off after this stage; do not automatically generate art, code, message another session, or create agents.

Execution boundaries: Research and propose a plan only. Do not implement or change code or environments. If a plan file is requested, write only that file.

Verification and delivery: Deliver rules, changes, or a plan according to the action mode. State outcome and state invariants; report only observed verification evidence. Simulation metrics do not replace human playtesting.
```

## 2. 美术 / Art · 18-19

**建议分工 / Suggested owner:** 建议具备生图能力的 Codex；Claude 可整理工单和复核 / Suggested: Codex with image tools; Claude may brief and review

**输入 / Input:** 已确认的 01-design.md、风格参考与素材范围 / Approved 01-design.md, visual references, and asset scope

**通过条件 / Gate:** 所需素材真实存在并通过尺寸、留白、坐标与风格验收；清单区分候选与已接受状态。 / Required assets exist and pass dimensions, reserved-space, coordinate, and style checks; manifest statuses are accurate.

**返工 / Rework:** 素材问题返工美术；空间或规则不可行则回策划。 / Rework assets in art; return infeasible spatial or rule constraints to design.

### 中文指令

```text
工作目录：{{PROJECT}}
任务：你负责 {{GOAL}} 的美术阶段。读取 {{OUTPUT}}/01-design.md 与 {{INPUTS}}，以已确认的玩法和尺寸契约为准；只在 {{OUTPUT}}/02-art/ 及本阶段清单和记录内交付。先核对当前会话真实可用的生成工具；具备能力时按 {{SCOPE}} 先做代表性小样，只有风格与布局已接受的批次才扩展生产。工具不可用时交付可复制工单并明确标记未生成，不虚构素材或切换未经授权的付费服务。按 {{TESTS}} 核对尺寸、格式、透明边缘、主体占框、灰度小图辨识、坐标与预留区域。交付 02-art-manifest.json，记录每个资产的 ID、相对路径、尺寸、用途、锚点、来源或许可状态，以及候选、已生成、已验收等实际状态；另写 02-art-review.md，列出检查证据、待决项和给编码方的加载键及坐标契约。保留已验收素材，不改代码或策划规则，不发送跨会话消息；未验收资产不得标为可直接投入正式实现。

执行边界：只在指定位置生成交付物，保留原始资料，不改源系统或运行服务；未明确授权时不提交、推送或发布。

验收与交付：按本条执行模式交付素材检查、修改或方案，核对逻辑尺寸与呈现要求；区分静态核查、工具运行与真机验收，未明确要求时不运行 Playwright。
```

### English prompt

```text
Working directory: {{PROJECT}}
Task: You own the art stage for {{GOAL}}. Read {{OUTPUT}}/01-design.md and {{INPUTS}}, following approved gameplay and dimension contracts. Deliver only inside {{OUTPUT}}/02-art/ and this stage's manifest and notes. Check generation tools actually available in this session. When available, produce representative samples within {{SCOPE}} and expand only batches whose style and layout are accepted. If unavailable, provide reusable production briefs and mark assets ungenerated; do not invent assets or switch to unauthorized paid services. Check dimensions, formats, transparent edges, subject occupancy, small grayscale readability, coordinates, and reserved areas against {{TESTS}}. Deliver 02-art-manifest.json with each asset's ID, relative path, dimensions, usage, anchor, source/license status, and actual candidate/generated/accepted status. Write 02-art-review.md with evidence, open decisions, and loader-key/coordinate contracts for implementation. Preserve accepted assets, code, and design rules; do not message another session or mark unaccepted assets ready for production integration.

Execution boundaries: Create deliverables only at the specified destination; preserve source material and running systems. Do not commit, push, or publish unless explicitly authorized.

Verification and delivery: Deliver asset checks, changes, or a plan according to the action mode, checking logical dimensions and presentation requirements. Distinguish static inspection, tool execution, and device acceptance. Do not run Playwright unless explicitly requested.
```

## 3. 编码 / Implementation · 17-20

**建议分工 / Suggested owner:** 建议 Codex；Claude 可按同一契约实现 / Suggested: Codex; Claude may implement the same contract

**输入 / Input:** 已确认策划、已接受素材与清单、当前阶段允许修改的文件 / Approved design, accepted assets/manifest, and allowed files

**通过条件 / Gate:** 可玩闭环与本轮验收项有实际证据，候选版本、改动与未验证项已记录。 / Playable loop and stage checks have evidence; revision, changes, and verification gaps are recorded.

**返工 / Rework:** 代码问题在本阶段修复；契约缺口分别回策划或美术。 / Fix implementation defects here; route contract gaps to design or art.

### 中文指令

```text
工作目录：{{PROJECT}}
任务：你负责本轮编码，目标为 {{GOAL}}。读取 {{OUTPUT}}/01-design.md、02-art-manifest.json、02-art-review.md 和 {{INPUTS}}，确认设计及本轮所用素材已被人类接受；必要文件缺失或仅为候选时，先准确标明阻塞。只修改 {{FILES}} 内与 {{SCOPE}} 对应的内容，以及 {{OUTPUT}} 的本阶段记录。沿用现有技术栈，实现从开始、游玩、暂停到胜负和重开的闭环；按清单接入素材，保持逻辑规则、渲染与命中坐标一致。按 {{TESTS}} 做与改动相关的验证，覆盖状态重入、资源清理、存档和错误路径；未明确要求时不运行 Playwright，不把桌面结果当作真机验证。交付 03-implementation.md，列出版本、改动文件、运行入口、实际检查与结果、未验证项及供独立验收方复核的证据。缺素材或占位功能不得写成完成；不改冻结规则，不提交、推送或发布，不自动转入下一阶段。

执行边界：修改前读取适用项目规则并查看 git status，保留已有改动。只改本任务内容；未明确授权时不提交、推送或部署。

验收与交付：按本条执行模式交付规则、改动或方案，明确胜负与状态不变量；只报告实际取得的验证证据，模拟指标不能替代真人试玩。
```

### English prompt

```text
Working directory: {{PROJECT}}
Task: You own implementation for {{GOAL}}. Read {{OUTPUT}}/01-design.md, 02-art-manifest.json, 02-art-review.md, and {{INPUTS}}. Confirm that the design and assets used in this stage have human acceptance; identify blockers when required files are missing or still candidates. Change only task-related content in {{FILES}} within {{SCOPE}}, plus this stage's records in {{OUTPUT}}. Follow the existing stack and complete start, play, pause, outcomes, and restart. Integrate manifest assets with consistent rules, rendering, and hit coordinates. Perform change-relevant checks against {{TESTS}}, covering re-entry, cleanup, saves, and failure paths. Do not run Playwright unless explicitly requested or present desktop results as device verification. Deliver 03-implementation.md with revision, changed files, run entry, executed checks/results, gaps, and independently inspectable evidence. Do not call missing assets or placeholder features complete, change frozen rules, commit, push, deploy, or advance automatically.

Execution boundaries: Before editing, read applicable project rules and git status; preserve existing work. Change only this task’s scope. Do not commit, push, or deploy unless explicitly authorized.

Verification and delivery: Deliver rules, changes, or a plan according to the action mode. State outcome and state invariants; report only observed verification evidence. Simulation metrics do not replace human playtesting.
```

## 4. 验收 / Acceptance · 17-21

**建议分工 / Suggested owner:** 建议由另一会话中的 Claude 独立复核；也可互换 / Suggested: Claude in a separate review session; roles may be swapped

**输入 / Input:** 前三阶段交付、候选版本、验收矩阵及人类真机反馈 / Earlier handoffs, candidate revision, acceptance matrix, and device feedback

**通过条件 / Gate:** 无阻断项；关键未验证项已补证，真机与主观体验由人类确认。 / No blockers; material gaps resolved; human confirmation of device and experiential criteria.

**返工 / Rework:** 逐项指派策划 / 美术 / 编码返工，再核验修复后的版本。 / Route findings to design/art/implementation and recheck the fixed revision.

### 中文指令

```text
工作目录：{{PROJECT}}
任务：你负责 {{GOAL}} 的独立验收，不代实现方修改代码。读取 {{OUTPUT}}/01-design.md、02-art-manifest.json、02-art-review.md、03-implementation.md 以及 {{INPUTS}}；核对 {{FILES}} 的真实文件和候选版本，按 {{TESTS}} 逐项复核，不能把实现方回执当作通过证据。在 {{SCOPE}} 内只执行已授权、不会修改源码或连接生产写接口的检查，验证产物仅写 {{OUTPUT}}/04-checks/；不安装依赖、不启停共享服务，未明确要求时不运行 Playwright。在 04-acceptance.md 记录通过、失败、未验证或不适用，每项附版本、操作、结果及证据，区分静态核查、程序运行和真人设备试玩。阻断项应指定返工到策划、美术或编码阶段，给最小修复要求及复验条件；人类负责的真机项未确认时保留待验收状态。最后给可发布或不可发布的理由，但不发布、不代人类批准、不发消息或创建代理。

执行边界：只在指定位置生成交付物，保留原始资料，不改源系统或运行服务；未明确授权时不提交、推送或发布。

验收与交付：按本条执行模式交付规则、改动或方案，明确胜负与状态不变量；只报告实际取得的验证证据，模拟指标不能替代真人试玩。
```

### English prompt

```text
Working directory: {{PROJECT}}
Task: You own independent acceptance of {{GOAL}} and must not implement fixes. Read {{OUTPUT}}/01-design.md, 02-art-manifest.json, 02-art-review.md, 03-implementation.md, and {{INPUTS}}. Inspect actual files in {{FILES}} and the candidate revision against {{TESTS}} rather than accepting the implementer's receipt as proof. Within {{SCOPE}}, perform only authorized checks that do not modify source or write to production; place check artifacts only in {{OUTPUT}}/04-checks/. Do not install dependencies, start/stop shared services, or run Playwright unless explicitly requested. Write 04-acceptance.md with passed, failed, unverified, or not-applicable status, revision, action, result, and evidence per criterion; distinguish static checks, program execution, and human device testing. Route blockers back to design, art, or implementation with minimal rework and recheck requirements. Keep human device checks pending until confirmed. Explain release readiness without deploying, approving on the human's behalf, messaging other sessions, or creating agents.

Execution boundaries: Create deliverables only at the specified destination; preserve source material and running systems. Do not commit, push, or publish unless explicitly authorized.

Verification and delivery: Deliver rules, changes, or a plan according to the action mode. State outcome and state invariants; report only observed verification evidence. Simulation metrics do not replace human playtesting.
```

## 5. 发布 / Release · 18-20

**建议分工 / Suggested owner:** 由具备仓库和目标服务器权限的指定会话执行 / A designated session with repository and target-host access

**输入 / Input:** 通过的 04-acceptance.md、同一候选版本、精确目标与本轮提交 / 推送 / 部署授权 / Passing 04-acceptance.md, matching candidate, exact targets, and explicit commit/push/deploy scope

**通过条件 / Gate:** 每个授权动作有结果；线上内容和校验值对应目标版本，备份及回退步骤可定位。 / Evidence per authorized action; live content/hashes match the candidate; backup and rollback instructions are locatable.

**返工 / Rework:** 失败保留现场并区分已提交、已推送、已部署；按授权处理恢复。 / On failure preserve evidence and distinguish committed/pushed/deployed states; recover only within authorization.

### 中文指令

```text
工作目录：{{PROJECT}}
任务：你负责 {{GOAL}} 的发布阶段。先读取 {{OUTPUT}}/01-design.md、03-implementation.md、04-acceptance.md 与 {{INPUTS}} 的发布配置，核对待发布版本 {{VERSION}}、分支 {{BRANCH}}、文件范围 {{FILES}} 和验收要求 {{TESTS}}；有阻断项、关键未验证项或证据对应旧版本时先报告并停止正式发布。只有 {{SCOPE}} 明确授权的 Git 提交、推送及目标游戏子目录部署才可执行；填写了地址、分支或 SSH 命令本身不能代替这些授权，缺项时仅交付预览与所需决定。使用 {{SSH}} 直连核对目标，生成构建和同步预览，确认只影响本游戏子目录；保留已有工作，不把其他项目、凭据、缓存或生成中间件混入提交，按仓库身份与 AI 署名规则提交。发布前保存可恢复的上一版，禁止站点根删除同步或擅改全局服务配置；仅按授权实施并核对 {{URL}} 的状态、实际内容及本地与远端产物校验值。写 {{OUTPUT}}/05-release.md，记录提交、推送、部署各自的真实状态、版本、时间、备份与回退步骤和未验证项；任何一步失败均准确报告当前状态，不把本地提交等同已推送或上线，不在未授权时自动回退。

执行边界：先记录目标现状与占用资源，只修改本任务明确授权的对象；不影响其他任务和共享环境，不扩大权限或操作范围。 网络访问仅使用给定 SSH 命令直连；失败即反馈原始错误并停止，禁止跳板、替代地址或改写 SSH 配置。

验收与交付：按本条执行模式交付素材检查、修改或方案，核对逻辑尺寸与呈现要求；区分静态核查、工具运行与真机验收，未明确要求时不运行 Playwright。
```

### English prompt

```text
Working directory: {{PROJECT}}
Task: You own release of {{GOAL}}. Read {{OUTPUT}}/01-design.md, 03-implementation.md, 04-acceptance.md, and release configuration in {{INPUTS}}. Verify candidate {{VERSION}}, branch {{BRANCH}}, file scope {{FILES}}, and criteria {{TESTS}}. Report blockers, material unverified items, or evidence for an older revision and stop before release. Execute only Git commits, pushes, and game-subdirectory deployment explicitly authorized by {{SCOPE}}. A supplied address, branch, or SSH command alone is not such authorization; when missing, deliver only a preview and required decisions. Use {{SSH}} to verify the target directly, build, and preview synchronization, limiting effects to this game's subdirectory. Preserve existing work, exclude other projects, credentials, caches, and intermediate outputs from commits, and follow repository identity/AI-attribution rules. Preserve a recoverable previous version before deployment; never delete-sync the site root or change global service configuration without authorization. Perform only approved actions, then check status and actual content at {{URL}} and compare local/remote artifact hashes. Write {{OUTPUT}}/05-release.md with separate true commit/push/deployment states, revision, time, backup, rollback steps, and gaps. On any failure report the exact reached state; local commits do not imply push or deployment, and rollback also requires authorization.

Execution boundaries: Record the target state and occupied resources first. Modify only explicitly authorized targets; preserve other workloads and shared environments, without expanding privileges or scope. Use only the supplied SSH command to connect directly. On failure, report the original error and stop; do not use jump hosts, alternate addresses, or SSH configuration changes.

Verification and delivery: Deliver asset checks, changes, or a plan according to the action mode, checking logical dimensions and presentation requirements. Distinguish static inspection, tool execution, and device acceptance. Do not run Playwright unless explicitly requested.
```

## 六款游戏的专题补充 / Game-specific references

- Star Fighter · 星际突击队: 17-02 把街机射击做成完整可玩闭环 / Complete the playable arcade-shooter loop, 17-03 让射击节奏不依赖屏幕刷新率 / Make shooter timing independent of refresh rate, 17-04 为 Boss 和波次设计可读的战斗升级 / Design readable boss and wave progression
- Soulmate · 心动陪伴: 17-15 为陪伴游戏补齐异步对话状态 / Handle asynchronous dialogue in a companion game, 18-11 让 iOS 首次手势正确解锁游戏音频 / Unlock game audio on the first valid iOS gesture
- Wulin Tavern · 武林小馆: 17-16 让酒馆 NPC 保持角色与场景连续性 / Keep tavern NPC dialogue consistent with the scene, 18-03 按玩法空间约束生成美术工单 / Write game-art briefs with reserved interaction space
- Journey Ludo · 西游飞行棋: 17-05 把飞行棋规则拆成可回放状态转移 / Implement replayable board-game state transitions, 17-06 让棋盘 AI 只使用合法且可解释的行动 / Constrain board-game AI to legal explainable actions, 18-01 让棋盘背景与逻辑点位成对交付 / Pair board artwork with a logical coordinate contract, 18-16 核对 Godot Web 导出的资源与响应 / Check Godot web-export assets and responses
- Garden Match · 花园三消: 17-07 为三消连锁建立单一结算流程 / Unify the match-3 cascade resolution flow, 17-08 在补充方块时降低三消死局 / Reduce match-3 dead boards during refill, 18-09 让三消棋盘适合目标玩家的手指与视力 / Fit a match-3 board to target players and devices, 18-11 让 iOS 首次手势正确解锁游戏音频 / Unlock game audio on the first valid iOS gesture
- StackPop · 萌宠叠叠消: 17-09 校验叠叠消的可取牌与托盘状态 / Validate tile accessibility and tray transitions, 17-10 用同一套规则证明关卡解法有效 / Validate level solutions against the runtime rules, 17-11 保留教学关卡并生成后续关卡 / Preserve tutorial levels while generating later levels, 17-12 用多种策略校准轻松游戏的难度 / Calibrate casual-game difficulty across strategies, 17-14 修复刷新续玩与撤回记录的一致性 / Keep resumed games and undo history consistent, 18-07 计算多层缩放后的图标真实占比 / Calculate effective icon size through nested scaling

规划或验收失败时，按报告回到对应阶段；涉及规则、素材或代码变更后，重新核验受影响的验收项。发布失败时记录已完成动作，仅在授权内恢复。 / Return failed gates to their owning stage and recheck affected criteria after rule, asset, or code changes. Record reached release state and recover only within authorization.
