---
sidebar_position: 1
title: "CLI 界面"
description: "终端内使用 Hermes：启动方式、常用参数、会话与快捷操作。"
---

# CLI 界面

Hermes 的 CLI 是完整的 TUI，支持多行输入、斜杠命令补全、会话历史、流式工具输出和中断/重定向。

## 启动方式

```bash
hermes                  # 默认交互模式
hermes chat -q "Hi"     # 单次问答
hermes chat --model anthropic/claude-3-7-sonnet-2025-02-19
hermes chat --provider nous        # 临时切换提供商
hermes chat --toolsets "web,terminal,skills"
```

## 实用提示

- `Ctrl+C`：中断当前请求；再次按可退出。
- `Ctrl+R`：搜索历史消息。
- 斜杠命令：输入 `/` 查看可用命令（与网关保持一致）。
- 在对话中可直接让 Agent 运行 shell、编辑文件或调用浏览器工具，终端输出会流式回显。

更多选项与键位说明见英文版 CLI 文档，中文补充将持续完善。

## Background Sessions {#background-sessions}

CLI 支持后台任务会话；这里保留锚点以兼容交叉链接。
