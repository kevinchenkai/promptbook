# PromptBook

**A practical, bilingual prompt handbook for Codex and Claude.**

[Use the handbook](https://g.ismayday.com/tools/promptbook/) · [简体中文](README.zh-CN.md) · [Contribute](CONTRIBUTING.md) · [Sources](docs/SOURCES.md)

[![Validate handbook](https://github.com/kevinchenkai/promptbook/actions/workflows/validate.yml/badge.svg)](https://github.com/kevinchenkai/promptbook/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-245e68.svg)](LICENSE)

**300 task templates · 16 categories · 47 tags · Chinese / English**

Search a developer task, fill in the relevant context, and copy an instruction that states the goal, action boundaries, and acceptance criteria. The interface is primarily Chinese; every prompt has a complete English version that can be used independently.

![PromptBook handbook preview](assets/preview.png)

## Start using it

1. [Open the website](https://g.ismayday.com/tools/promptbook/), or save the repository's [`index.html`](index.html) locally and open it in a browser (use GitHub's **Download raw file** button).
2. Search by task, keyword, or template ID; filter by category, tag, or action mode.
3. Fill in the working directory, goal, evidence, and other parameters.
4. Choose **中文** or **English**, check the boundaries and acceptance criteria, then copy into your Codex or Claude session.

No account, API key, backend, model connection, package install, or build is required to read the handbook. `index.html` embeds all styles, scripts, data, and public source references. It works offline.

## What makes a template useful

- **Tasks rather than personas:** concrete inputs, bounded work, and inspectable outcomes.
- **Six action modes:** read-only analysis, planning, local edits, remote changes, deliverable creation, and explicit Git actions.
- **Reusable parameters:** bilingual previews, copy, TXT download, printing, favorites, and JSON export.
- **A starting path:** 24 recommended templates and 8 common workflows.
- **Traceable additions:** original templates and open-source method references are distinguished; references link to exact commits and licenses.

A template does not create tool access or grant permission to an external system. Use the mode that matches the action you intend to authorize. For simple tasks, remove context already established in your session instead of sending unnecessary instructions.

## Task coverage

| ID | Category | Templates |
| --- | --- | ---: |
| 01 | Working with an agent | 18 |
| 02 | Research and planning | 18 |
| 03 | Implementation and refactoring | 18 |
| 04 | Debugging and review | 18 |
| 05 | Git, sync and archiving | 18 |
| 06 | SSH, networking and macOS | 18 |
| 07 | GPU environments and services | 18 |
| 08 | Training operations | 18 |
| 09 | Models, data and experiments | 18 |
| 10 | Images, video and assets | 18 |
| 11 | Documents and knowledge | 18 |
| 12 | Frontend and product work | 18 |
| 13 | Security, privacy and access | 21 |
| 14 | APIs, databases and data engineering | 21 |
| 15 | Testing, quality and delivery | 21 |
| 16 | Agents, tools and context | 21 |

The original 216 templates retain their IDs and bodies. The 84 additions cover security/access, APIs/data engineering, testing/delivery, and agent/tool/context workflows.

## Privacy and storage

Search and parameter substitution run in your browser, with no analytics or runtime network requests. Filled values stay in memory while the page is open. Favorites use browser local storage; exports contain original templates, **not filled parameters**. Storage behavior can differ for local files, browser profiles, and site origins.

Public files contain no original private chat excerpts, session identifiers, or assistant replies. The historical scenarios have been rewritten into general templates. Do not enter credentials into the handbook.

## Build and preview

Requires **Python 3.9+**, standard library only. Node.js is optional for syntax checking.

```bash
git clone https://github.com/kevinchenkai/promptbook.git
cd promptbook
python3 build.py
python3 build.py --check
node --check ui.js
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. `--check` writes nothing and fails if generated outputs are stale. Builds use local repository sources; they need no personal history archive, external prompt repository, or model service.

```text
index.html                 Self-contained public handbook
index.template.html        Page structure and metadata
ui.css / ui.js             Styles and browser interactions
recipes/01.txt … 16.txt     Bilingual editorial source records
handbook.json              Generated public prompt data
references.json            Pinned sources and prompt mappings
build.py                   Standard-library builder and validator
docs/SOURCES.md            Research and editorial decisions
licenses/                  Retained upstream license notices
.github/                   Validation workflow and contribution templates
```

Edit a recipe, rebuild, and follow [CONTRIBUTING.md](CONTRIBUTING.md). Append records to preserve existing IDs used by favorites and workflows. The content date is editorial metadata rather than the build machine's clock, so builds are reproducible across days.

## Sources and quality

This edition combines rewritten real-world task scenarios with new original templates and method references from [Fabric](https://github.com/danielmiessler/Fabric), [Prompt Catalog](https://github.com/KevinRabun/prompt-catalog), and [OpenAI Cookbook](https://github.com/openai/openai-cookbook). See [the exact files, versions, license checks, and rejected approaches](docs/SOURCES.md). No complete external prompt collection is imported.

Structural validation checks unique IDs/titles/bodies, bilingual parameter parity, source mappings, and generated-file freshness. Browser checks cover core handbook interactions. **The 300 templates have not all been evaluated in model A/B tests.** Suitability still depends on your context, model, tools, and permissions. This project is independent of OpenAI and Anthropic.

## Hosting and license

Publish the generated `index.html` on any static host. This project's canonical site is [g.ismayday.com/tools/promptbook/](https://g.ismayday.com/tools/promptbook/). Repository metadata includes developer-tool and prompt-library topics for discovery; the page includes search and social-sharing metadata.

Original project material is **[MIT licensed](LICENSE)**. Referenced upstream MIT notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and `licenses/`. Contributions and useful new scenarios are welcome through [issues](https://github.com/kevinchenkai/promptbook/issues) and pull requests.
