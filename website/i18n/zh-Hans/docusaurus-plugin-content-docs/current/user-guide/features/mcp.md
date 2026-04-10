---
sidebar_position: 4
title: "MCP（Model Context Protocol）"
description: "通过 MCP 连接外部工具服务，并按需向 Hermes 暴露可用能力。"
---

# MCP（Model Context Protocol）

MCP 让 Hermes 可以连接外部工具服务，无论这些服务运行在本地还是远程，都不需要先为每个能力手写原生工具。它很适合接入代码库、数据库、浏览器栈以及内部 API。

## 能做什么

- 同时连接本地 `stdio` 和远程 `HTTP` MCP 服务
- 在启动时自动发现并注册工具
- 按服务端过滤可暴露的工具，降低安全风险

## 快速配置

在 `~/.hermes/config.yaml` 的 `mcp.servers` 节中添加服务，例如：

```yaml
mcp:
  servers:
    local-files:
      transport: stdio
      command: node path/to/server.js
      enabled: true
      allowed_tools: ["readFile", "listDirectory"]
```

启动后执行：

```bash
hermes chat --toolsets "mcp,web,terminal"
```

MCP 工具会随着会话一起加载；如果你希望限制某个会话能看到哪些工具，可以继续在配置里细分。

## 以 MCP Server 运行 Hermes {#running-hermes-as-an-mcp-server}

这里保留与英文文档一致的兼容锚点，确保站内链接和跨语言跳转都能正确命中。后续可以在这个小节下补充更完整的中文说明。
