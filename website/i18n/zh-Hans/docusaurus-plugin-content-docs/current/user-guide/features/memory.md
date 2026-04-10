---
sidebar_position: 3
title: "持久记忆"
description: "MEMORY.md / USER.md 的工作方式与更新方法，帮助 Hermes 记住你的偏好与环境。"
---

# 持久记忆

Hermes 通过两份短文本保持跨会话记忆：

| 文件 | 作用 | 默认位置 |
| --- | --- | --- |
| **MEMORY.md** | Agent 的工作笔记，记录环境约定、学到的技巧 | `~/.hermes/memories/` |
| **USER.md** | 用户画像，语气偏好、常用工具、禁忌 | `~/.hermes/memories/` |

会话开始时会读取快照注入系统提示，Agent 可在任务中调用 `memory` 工具自我更新。

## 使用建议

- 定期让 Agent 总结当前项目写入 MEMORY.md。
- 变更沟通偏好时更新 USER.md，或在对话中直接说明。
- 开启 FTS5 会话搜索后，历史对话也会参与记忆召回。
