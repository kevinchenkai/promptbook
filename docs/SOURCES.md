# Sources and editorial decisions / 来源与编辑取舍

Open-source references reviewed: **2026-10-24**. User-task edition updated: **2026-10-29**. PromptBook is an independent project. Names below identify references, not endorsements.

## What the library contains

- **216 existing templates**: editorial rewrites of recurring engineering task scenarios. Public files contain reusable instructions only, without private chat excerpts, session IDs, account details, or assistant replies.
- **84 additions**: newly authored bilingual templates for security, API/data work, testing/delivery, and agent/tool workflows. Some use the organizational methods below; the remainder are original additions.
- **60 additions in the 2026-10-29 edition**: 36 dedicated game templates and 24 workflow templates. Recent user instructions were reviewed for October 24–29 (America/Los_Angeles); game coverage also uses earlier GameAI sessions and user-authored requirements. Automatic injections, wrapped model calls, heartbeat messages, and quoted assistant receipts are excluded as instruction sources. See [edition notes](UPDATES.md).
- Every template includes a goal, named parameters, an action mode, boundaries, and verification requirements. These are writing and execution conventions, not measured model-performance guarantees.
- `references.json` records the exact file, commit, license, relationship, and mapped prompt IDs for adopted open-source methods. `handbook.json` embeds those references for offline viewing.

## Adopted open-source methods

| Source and pinned version | License checked | What was used | Prompt IDs |
| --- | --- | --- | --- |
| [Fabric: STRIDE threat model](https://github.com/danielmiessler/Fabric/blob/f16de16827ae23e4bb9aa35c2e4b690d40c5907c/data/patterns/create_stride_threat_model/system.md) | MIT | Asset, trust-boundary and data-flow inventory; realistic threats and verifiable mitigations | 13-01 |
| [Fabric: code review](https://github.com/danielmiessler/Fabric/blob/f16de16827ae23e4bb9aa35c2e4b690d40c5907c/data/patterns/review_code/system.md) | MIT | Prioritized findings with evidence, impact and remediation | 13-21 |
| [Prompt Catalog: security](https://github.com/KevinRabun/prompt-catalog/blob/631e9a62f3fb4b32b5ed9f362c1e16c9d675db4e/instructions/guardrails/security.instructions.md) | MIT | Input boundaries, authorization, credential protection and adverse-input checks | 13-02, 13-03, 13-07, 13-18 |
| [Prompt Catalog: accuracy](https://github.com/KevinRabun/prompt-catalog/blob/631e9a62f3fb4b32b5ed9f362c1e16c9d675db4e/instructions/guardrails/accuracy.instructions.md) | MIT | Verify actual interfaces and sources; separate evidence from inference | 14-01, 16-08, 16-09, 16-16 |
| [OpenAI Cookbook: Codex prompting guide](https://github.com/openai/openai-cookbook/blob/8495326b6f1b7cec94e7f5e393a4045e328a268e/examples/gpt-5/codex_prompting_guide.ipynb) | MIT | Outcome, relevant context, bounded implementation, verification and continuation | 16-04, 16-10, 16-12, 16-21 |

**Relationship: method reference, original wording.** PromptBook did not import these prompt files or translate them line by line. The source is not evidence that an upstream author wrote or tested our templates. Third-party notices and exact license copies are retained in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and [licenses/](../licenses/).

固定“思考时长”、要求输出隐藏思考过程、虚构工具能力、无条件执行与旧模型专用参数均未采用。授权规则依据当前任务编写，不直接继承上游模板中的权限假设。

## Other repositories reviewed

| Repository | License finding | Editorial decision |
| --- | --- | --- |
| [f/prompts.chat](https://github.com/f/prompts.chat/tree/61ed3b1bc838290561aaa8cce03d00d4d449b7aa), formerly awesome-chatgpt-prompts | [Dual license](https://github.com/f/prompts.chat/blob/61ed3b1bc838290561aaa8cce03d00d4d449b7aa/LICENSE): site code/content MIT; prompt data such as `prompts.csv` CC0-1.0 | Reviewed security and QA role prompts. No text imported; broad personas and terminal simulators were not suitable for this task-oriented engineering handbook. Do not label the entire corpus MIT. |
| [Anthropic interactive prompting tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | No explicit license identified during this review | Reading reference only. No copying, translation, or prompt import. Do not infer permission from public visibility. |

No repository was bulk-imported. License decisions apply to the reviewed version and scope; contributors must check licenses again when adding material.

## Official writing references

- [OpenAI: Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — clear instructions, relevant context, diverse input/output examples, and evaluation. Relevant to the handbook format and 16-07. No official text or examples copied.
- [OpenAI: Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) — keep guidance concise and applicable; avoid unnecessary context and duplicated constraints. This article discusses a specific model; PromptBook does not assume the same behavior for all models.

## 中文说明

本库不是原始会话导出，也不是上游提示词合集的镜像。新增条目针对实际开发场景重新编写；有明确参考的方法会保留仓库、文件、固定 commit、许可与对应编号。未明确许可的项目只作阅读参考。

“结构检查通过”表示参数、编号和构建一致性通过，不表示已对全部 360 条进行模型 A/B 测试。页面交互检查也不等同于每条任务已经在真实生产环境执行。
