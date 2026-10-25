# PromptBook

一本可离线使用的 Codex / Claude 双语指令手册。

[在线使用](https://g.ismayday.com/tools/promptbook/) · [GitHub](https://github.com/kevinchenkai/promptbook)

**216 个场景 · 12 类任务 · 39 个标签 · 中文 / English**

## 使用

用浏览器打开 [`index.html`](index.html)，无需安装依赖或连接模型。

1. 从上手指南或搜索中选择任务场景。
2. 填写项目、目标、输入资料等参数。
3. 选择中文或英文，核对执行边界与验收要求后复制到目标会话。

支持全文搜索、分类与标签筛选、参数预览、收藏、模板下载和打印；另有 24 条入门推荐与 8 条常用流程。

参数只在当前打开期间保留。收藏使用浏览器本地存储；更换浏览器、文件位置或清理数据后可能需要重新收藏。导出收藏不包含填写的参数。

## 文件结构

```text
promptbook/
├── index.html             # 独立的网页成品 / Web 默认入口
├── index.template.html    # 页面结构
├── ui.css                 # 页面样式
├── ui.js                  # 本地搜索、填参、复制、收藏等交互
├── recipes/               # 12 类双语指令，每类 18 条
├── handbook.json          # 公开模板数据，不包含个人聊天摘录
├── build.py               # Python 构建脚本
├── .gitignore
└── README.md
```

`index.html` 已内置全部数据、脚本和样式，可单独复制或托管。正常构建使用本目录内的文件，不依赖个人历史记录目录、父仓库或 AI 服务。

## 本地构建与预览

在此目录使用 Python 3.9 或更新版本：

```bash
python3 build.py
python3 -m http.server 8000 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8000/`。停止预览时按 `Ctrl+C`。

构建脚本会检查指令数量、重复项及中英文参数对应关系，并重新生成 `handbook.json` 和 `index.html`。JavaScript 语法可额外用 `node --check ui.js` 检查；浏览或 Python 构建不要求安装 Node.js。

### 编辑指令

编辑 `recipes/01.txt` 至 `recipes/12.txt`，每行一条，使用 `¦` 分隔七个字段：

```text
中文标题¦English title¦模式¦原始关键词标签¦来源检索词¦中文任务正文¦English task text
```

参数采用 `{{PROJECT}}` 一类命名占位符；中英文必须使用同一组参数。公共执行边界、验收要求、参数说明及标签归一化在 `build.py` 中维护。

模式：`R` 只读分析、`P` 先出方案、`E` 本地执行、`M` 远端执行、`D` 生成交付物、`C` 明确的 Git 操作。

公开构建只输出通用模板，不包含个人聊天摘录、会话标识或具体连接信息。原始聊天日志、完整历史导出及账号凭据不属于本项目；本地 `.local/` 目录不会提交到 Git。

## 内容说明

模板由历史任务场景精选改写，不是历史原句的逐字翻译。公开版不包含历史摘录，也不代表模型效果认证。模板已核对参数结构与页面主要交互，未对全部模板逐条进行模型效果 A/B 测试。

远端相关模板要求按给定地址直连；SSH 失败时反馈错误并停止，不擅自使用跳板或替代路径。

## 仓库与发布

- 项目名：**PromptBook**。
- GitHub：`kevinchenkai/promptbook`。
- 静态站点入口：`index.html`；可将该文件单独作为发布内容。
- 无后端、API key、服务器程序或前端打包依赖。
- 网站：`https://g.ismayday.com/tools/promptbook/`。
- Web 端仅发布生成的 `index.html`，不上传 Git 元数据、编辑源文件或本地历史记录。
- 更新方式：修改模板 → `python3 build.py` → 检查成品 → 提交代码 → 上传新的 `index.html`；现有静态站点无需新增后端服务。

## 提示词写作参考

- [OpenAI · Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [OpenAI · Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
