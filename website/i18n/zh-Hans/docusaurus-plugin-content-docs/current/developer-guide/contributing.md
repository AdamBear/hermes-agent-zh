---
sidebar_position: 4
title: "贡献指南"
description: "如何为 Hermes 提交代码：开发环境、优先级、测试与提交流程。"
---

# 贡献指南

感谢参与 Hermes！下面是最短路径的贡献说明。

## 开发环境

```bash
source venv/bin/activate
pip install -e .[dev]
```

建议在 PR 前至少跑一次核心测试：

```bash
python -m pytest tests/test_model_tools.py -q
python -m pytest tests/test_cli_init.py -q
```

## 优先处理方向

1. Bug 修复（崩溃、错误行为、数据丢失）
2. 跨平台兼容（macOS、各类 Linux、WSL2）
3. 安全与健壮性（审批、防注入、错误处理）
4. 性能与可靠性优化
5. 通用技能与工具（优先技能，其次才是新工具）

## 提交流程

- 遵循现有代码风格与 typing 约定。
- 不要修改对话缓存 / 破坏提示缓存的行为。
- 相关文档与示例同步更新（本页即为中文骨架，可持续补充）。
- 提交 PR 前附带变更摘要与测试结果。
