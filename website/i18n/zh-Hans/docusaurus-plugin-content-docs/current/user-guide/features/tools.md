---
sidebar_position: 1
title: "工具与工具集"
description: "Hermes 内置工具概览、工具集启用方式与终端后端选择。"
---

# 工具与工具集

Hermes 内置覆盖搜索、浏览器自动化、终端执行、文件编辑、记忆、委托、语音、消息推送等工具。工具按 **toolset** 归类，可按平台与会话选择性启用。

## 启用/禁用

```bash
hermes tools                # 交互式开启/关闭工具集
hermes chat --toolsets web,terminal,skills
```

- CLI 与网关共享同一工具配置，但可按平台定制。
- 危险命令默认需要审批，参见安全设置。

## 运行后端

终端工具支持 Local / Docker / SSH / Daytona / Singularity / Modal，多端可并存。切换后端会改变命令执行位置，但不影响对话与工具列表。

更多细节（完整工具表、参数、工具集定义）可暂参考英文版文档。
