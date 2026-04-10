---
sidebar_position: 1
title: "消息网关"
description: "在 Telegram、Discord、Slack、WhatsApp 等平台与同一 Hermes 实例对话。"
---

# 消息网关

网关是常驻进程，统一管理聊天平台、会话存储、定时任务与语音回复。

## 支持的平台（节选）

Telegram、Discord、Slack、WhatsApp、Signal、Email、SMS、Home Assistant、Mattermost、Matrix、钉钉、飞书、企业微信、BlueBubbles，以及 OpenAI 兼容前端（通过内置 API Server）。

## 快速启动

```bash
hermes gateway           # 读取当前配置并启动所有已开启平台
```

首启前建议：
1) 在 `.env` 写入各平台 Token（如 `TELEGRAM_BOT_TOKEN`、`DISCORD_BOT_TOKEN`）。
2) 在 `config.yaml` 打开需要的平台开关（网关会只加载开启的适配器）。

## 常用技巧

- 同一会话在本地 CLI 与消息平台共享上下文。
- `display.background_process_notifications` 控制后台进程的推送粒度。
- 语音功能与 TTS 依赖额外密钥，详见英文版 Voice Mode 文档。

## DM Pairing (Alternative to Allowlists) {#dm-pairing-alternative-to-allowlists}

这里保留锚点以兼容文档交叉引用；中文详细说明后续继续补齐。

## Background Sessions {#background-sessions}

消息平台同样支持后台任务与结果回传。

## macOS (launchd) {#macos-launchd}

如果你在 macOS 上以 launchd 方式运行 gateway，可通过这个锚点接收跨页跳转。
