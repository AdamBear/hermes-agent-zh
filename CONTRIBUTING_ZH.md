# 参与贡献

[English Version](CONTRIBUTING.md)

欢迎为 Hermes Agent 贡献代码、文档和反馈。

## 贡献方式

- 提交 bug 报告和功能建议
- 改进文档与示例
- 修复缺陷
- 增加测试
- 开发新功能、工具、平台适配或技能

## 开发环境

推荐先阅读官方开发文档：

- 英文开发指南：https://hermes-agent.nousresearch.com/docs/developer-guide/contributing
- 中文文档首页：https://hermes-agent.nousresearch.com/docs/zh-Hans/

快速开始：

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

如果你需要 RL / Tinker-Atropos 相关能力：

```bash
git submodule update --init tinker-atropos
uv pip install -e "./tinker-atropos"
```

## 提交前建议

- 保持改动范围聚焦，避免把无关重构混进同一个提交
- 为新增功能或修复补充对应测试
- 如果修改了用户可见行为，请同步更新文档
- 如果新增了命令、帮助文案或关键页面，建议同时补中英文内容

## 中文化相关约定

- 命令名、代码标识、路径、环境变量保持英文
- 说明性文案、帮助文本、用户引导可以提供中文版本
- Docusaurus 中文站使用 `zh-Hans`
- 新增高频文档时，优先同步中文入口页和核心使用页

## 提交 PR

- 清楚描述改动内容、动机和影响范围
- 列出你做过的验证步骤
- 如果改动较大，建议附上截图、终端输出或测试结果摘要

更多细节以英文 [CONTRIBUTING.md](CONTRIBUTING.md) 和官方开发文档为准。
