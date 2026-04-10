# Hermes Agent 中文说明

[English README](README.md)

<p align="center">
  <img src="assets/banner.png" alt="Hermes Agent" width="100%">
</p>

[在线文档现已支持中英双语：默认英文 `/docs/`，简体中文 `/docs/zh-Hans/`](https://hermes-agent.nousresearch.com/docs/zh-Hans/)，本文件提供快速概览。

## 项目简介

**Hermes Agent** 是由 [Nous Research](https://nousresearch.com) 打造的自我改进型 AI Agent。

它不仅能调用工具，还具备持续学习闭环：

- 能从任务经验中生成和改进技能
- 会在使用过程中持续沉淀知识和记忆
- 能搜索历史会话并跨会话召回上下文
- 可以逐步建立对用户偏好和行为模式的长期理解

Hermes 可以运行在低成本 VPS、GPU 集群或按需唤醒的无服务器环境中，不必绑定在本地电脑上。你也可以在 Telegram 等聊天平台上和部署在云端的 Agent 直接对话。

支持的模型与提供商包括：

- [Nous Portal](https://portal.nousresearch.com)
- [OpenRouter](https://openrouter.ai)
- [z.ai / GLM](https://z.ai)
- [Kimi / Moonshot](https://platform.moonshot.ai)
- [MiniMax](https://www.minimax.io)
- OpenAI
- 以及你自己的兼容端点

你可以通过 `hermes model` 随时切换模型，不需要改代码，也不会被单一平台锁定。

## 主要特性

| 能力 | 说明 |
|------|------|
| 真正可用的终端界面 | 完整 TUI，支持多行输入、斜杠命令补全、会话历史、中断重定向、工具流式输出 |
| 多平台常驻 | 可通过 CLI、Telegram、Discord、Slack、WhatsApp、Signal 等统一接入 |
| 学习闭环 | 包含记忆、技能自生成、技能自改进、跨会话搜索与总结 |
| 定时自动化 | 内置 cron 调度，可将任务结果发送到任意支持的平台 |
| 子代理与并行 | 支持委托子代理并行执行任务，也可通过 Python/RPC 串联复杂流程 |
| 多运行环境 | 支持 local、Docker、SSH、Daytona、Singularity、Modal 等终端后端 |
| 面向研究 | 支持批量轨迹生成、Atropos RL 环境、轨迹压缩等研究工作流 |

## 快速安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

支持 Linux、macOS、WSL2，以及 Android 的 Termux 环境。

说明：

- Android / Termux：参考官方 [Termux 指南](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
- Windows：不支持原生 Windows，建议先安装 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)

安装完成后：

```bash
source ~/.bashrc
hermes
```

如果你使用的是 `zsh`，把上面的 `source ~/.bashrc` 改成 `source ~/.zshrc`。

## 快速上手

```bash
hermes              # 启动交互式 CLI
hermes model        # 选择模型提供商和模型
hermes tools        # 配置启用的工具
hermes config set   # 设置单项配置
hermes gateway      # 启动消息平台网关
hermes setup        # 运行完整初始化向导
hermes claw migrate # 从 OpenClaw 迁移
hermes update       # 更新到最新版
hermes doctor       # 诊断环境问题
```

完整文档入口：

- https://hermes-agent.nousresearch.com/docs/

## CLI 与消息平台的区别

Hermes 有两个主要入口：

- 直接运行 `hermes`，使用终端交互界面
- 运行 `hermes gateway`，然后通过 Telegram、Discord、Slack、WhatsApp、Signal、Email 等平台与它对话

常见操作对照如下：

| 操作 | CLI | 消息平台 |
|------|-----|----------|
| 开始对话 | `hermes` | 先运行 `hermes gateway setup` 和 `hermes gateway start`，再向机器人发消息 |
| 新建会话 | `/new` 或 `/reset` | `/new` 或 `/reset` |
| 切换模型 | `/model [provider:model]` | `/model [provider:model]` |
| 切换人格 | `/personality [name]` | `/personality [name]` |
| 重试或撤销上一步 | `/retry`、`/undo` | `/retry`、`/undo` |
| 压缩上下文 / 查看用量 | `/compress`、`/usage`、`/insights [--days N]` | `/compress`、`/usage`、`/insights [days]` |
| 浏览技能 | `/skills` 或 `/<skill-name>` | `/skills` 或 `/<skill-name>` |
| 中断当前任务 | `Ctrl+C` 或直接发送新消息 | `/stop` 或直接发送新消息 |
| 平台状态 | `/platforms` | `/status`、`/sethome` |

## 文档导航

所有官方文档位于：

- https://hermes-agent.nousresearch.com/docs/

常用入口：

| 文档 | 内容 |
|------|------|
| [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) | 2 分钟完成安装、配置和首次对话 |
| [CLI Usage](https://hermes-agent.nousresearch.com/docs/user-guide/cli) | CLI 命令、快捷键、人格、会话 |
| [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) | 配置文件、模型提供商、全量选项 |
| [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) | Telegram、Discord、Slack、WhatsApp、Signal 等 |
| [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security) | 命令审批、隔离、权限控制 |
| [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) | 工具系统与工具集 |
| [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | 技能系统、Skills Hub、技能创建 |
| [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | 持久记忆、用户画像与实践建议 |
| [MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) | 通过 MCP 扩展能力 |
| [Cron Scheduling](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | 定时任务与自动投递 |
| [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) | 影响每次会话的项目上下文 |
| [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) | 项目结构、Agent 循环、核心类 |
| [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing) | 开发环境、PR 流程、代码规范 |
| [CLI Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) | CLI 命令与参数总览 |
| [Environment Variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) | 环境变量参考 |

## 从 OpenClaw 迁移

如果你之前在使用 OpenClaw，Hermes 可以自动导入：

- 配置
- 记忆
- 技能
- API Key

首次运行 `hermes setup` 时，会自动检测 `~/.openclaw` 并提示迁移。

你也可以在安装后手动执行：

```bash
hermes claw migrate
hermes claw migrate --dry-run
hermes claw migrate --preset user-data
hermes claw migrate --overwrite
```

可迁移内容包括：

- `SOUL.md`
- `MEMORY.md` 与 `USER.md`
- 用户自定义技能
- 命令审批白名单
- 消息平台配置
- 部分允许导入的 API 密钥
- TTS 相关资源
- 工作区中的 `AGENTS.md`

更多参数可查看：

```bash
hermes claw migrate --help
```

## 参与贡献

欢迎贡献。开发流程可参考官方 [Contributing Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)，或先看仓库内的 [中文贡献说明](CONTRIBUTING_ZH.md)。

开发环境快速开始：

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

如果你还需要 RL / Tinker-Atropos 相关能力：

```bash
git submodule update --init tinker-atropos
uv pip install -e "./tinker-atropos"
```

## 社区

- Discord: https://discord.gg/NousResearch
- Skills Hub: https://agentskills.io
- Issues: https://github.com/NousResearch/hermes-agent/issues
- Discussions: https://github.com/NousResearch/hermes-agent/discussions

## 许可证

本项目使用 MIT License，详见 [LICENSE](LICENSE)。

由 [Nous Research](https://nousresearch.com) 构建。
