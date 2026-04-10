---
sidebar_position: 1
title: "快速上手"
description: "2 分钟完成安装、选择模型、发起首次对话，并了解常用命令。"
---

# 快速上手

## 1. 安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc   # 或 ~/.zshrc
```

## 2. 选择模型与工具

```bash
hermes model        # 选择提供商与模型（支持 Nous Portal / OpenRouter / OpenAI 等）
hermes tools        # 启用或停用工具集
hermes setup        # 一次性完成模型、工具、网关等配置
```

## 3. 开始对话

```bash
hermes              # 交互式 CLI
hermes chat -q "你好"  # 单次问答
```

常用参数：
- `--model` / `--provider`：临时指定模型或提供商
- `--toolsets web,terminal`：只开启指定工具集
- `--skill <path>`：预加载某个技能

## 4. 进一步体验

- `hermes gateway`：启动消息网关，让 Telegram/Discord/Slack 与同一个 Agent 对话
- `hermes update`：更新到最新版本
- `hermes doctor`：诊断环境问题

下一步可阅读 [CLI 界面](/user-guide/cli) 与 [配置](/user-guide/configuration)。
