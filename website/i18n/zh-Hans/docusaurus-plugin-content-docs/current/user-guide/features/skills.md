---
sidebar_position: 2
title: "技能系统"
description: "渐进披露的知识单元，兼容 agentskills.io 规范，可由 Agent 自动生成与改进。"
---

# 技能系统

技能是可按需加载的知识文件，遵循 **渐进披露**，以降低上下文成本。全部存放在 `~/.hermes/skills/`，包含：

- 预置技能：首次安装时复制。
- Hub 安装技能：来自 agentskills.io 或其他来源。
- Agent 自创技能：任务中自动生成/更新。

## 使用技能

- 在对话中直接引用技能名或路径，Agent 会按需加载。
- 也可启动时预加载：`hermes chat --skill path/to/skill.md`
- 支持外部技能目录，适合团队共享。

## 管理技能

- `hermes skills`：浏览/启用/禁用技能
- `hermes tools` 中的 `skills` toolset 需保持开启
- 对齐规范参考 [技能规范](https://agentskills.io/specification)（英文）
