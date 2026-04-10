---
sidebar_position: 2
title: "安装"
description: "在 Linux、macOS、WSL2 或 Termux 快速安装 Hermes Agent。"
---

# 安装

推荐使用一行脚本完成安装，全程约 1–2 分钟。

## 快速安装

```bash
# Linux / macOS / WSL2 / Android (Termux)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

- Termux 会自动走针对 Android 的依赖与编译流程，额外细节见 [Termux 指南](/getting-started/termux)。
- 原生 Windows 暂不支持，请在 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) 内执行上述命令。

安装结束后重新加载 Shell：

```bash
source ~/.bashrc   # zsh 用户改为 source ~/.zshrc
```

## 手动检查

- 验证：`hermes --help` / `hermes version`
- 模型配置：`hermes model`
- 工具配置：`hermes tools`
