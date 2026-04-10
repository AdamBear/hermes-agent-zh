---
sidebar_position: 2
title: "配置"
description: "config.yaml、.env、模型与提供商设置的中文概览。"
---

# 配置

所有配置位于 `~/.hermes/`，支持多配置文件与环境变量。

## 目录速览

```text
~/.hermes/
├── config.yaml   # 主配置（显示、模型、工具、音频等）
├── .env          # API 密钥与私密变量
├── auth.json     # OAuth 凭证（如 Nous Portal）
├── SOUL.md       # Agent 人设 / 语气
├── memories/     # MEMORY.md、USER.md
├── skills/       # 技能目录
```

## 常用命令

- `hermes config edit`：在编辑器中打开 config.yaml
- `hermes config set key value`：直接写入单项配置
- `hermes model`：交互式选择提供商与模型
- `hermes tools`：启用/禁用工具集

## 配置提示

- 默认尊重 `HERMES_HOME`，可通过 Profile 机制隔离多套配置。
- 需要语音/网关功能时，请在 `.env` 写入相关 API Key（如 TTS、Telegram Bot Token）。

## Context Compression {#context-compression}

此页目前是精简中文概览，保留这个锚点以兼容现有交叉链接。完整参数与行为说明请暂时参考英文原文。

## Auxiliary Models {#auxiliary-models}

如果你需要为视觉、摘要或网页提取等辅助任务单独指定模型，请先参考英文版详细配置。

## Website Blocklist {#website-blocklist}

站点黑名单相关说明后续会继续补全，这里先保留锚点兼容链接。
