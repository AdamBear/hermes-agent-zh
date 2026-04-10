"""Lightweight runtime i18n helpers for Hermes CLI and gateway."""

from __future__ import annotations

import os
from typing import Any


SUPPORTED_LOCALES = ("en", "zh")
DEFAULT_LOCALE = "en"

_ACTIVE_LOCALE: str | None = None


_TRANSLATIONS: dict[str, dict[str, str]] = {
    "zh": {
        "category.Session": "会话",
        "category.Configuration": "配置",
        "category.Tools & Skills": "工具与技能",
        "category.Info": "信息",
        "category.Exit": "退出",
        "meta.usage": "用法",
        "meta.alias_for": "别名，对应",
        "meta.alias": "别名",
        "command.new.description": "开始一个新会话（新的会话 ID 与历史）",
        "command.clear.description": "清屏并开始一个新会话",
        "command.history.description": "显示会话历史",
        "command.save.description": "保存当前对话",
        "command.retry.description": "重试上一条消息（重新发送给 agent）",
        "command.undo.description": "移除上一轮用户与助手的往返消息",
        "command.title.description": "为当前会话设置标题",
        "command.branch.description": "从当前会话分叉（探索另一条路径）",
        "command.compress.description": "手动压缩会话上下文",
        "command.rollback.description": "列出或恢复文件系统检查点",
        "command.stop.description": "终止所有后台进程",
        "command.approve.description": "批准待确认的危险命令",
        "command.deny.description": "拒绝待确认的危险命令",
        "command.background.description": "在后台运行一个提示词",
        "command.btw.description": "使用当前会话上下文提一个临时旁支问题（无工具、不持久化）",
        "command.queue.description": "把提示加入下一轮队列（不打断当前执行）",
        "command.status.description": "显示会话信息",
        "command.profile.description": "显示当前 profile 名称和 home 目录",
        "command.sethome.description": "把当前聊天设为 home channel",
        "command.resume.description": "恢复一个已命名的历史会话",
        "command.config.description": "显示当前配置",
        "command.model.description": "切换当前会话模型",
        "command.provider.description": "显示可用 provider 和当前 provider",
        "command.personality.description": "设置预定义人格",
        "command.statusbar.description": "切换上下文/模型状态栏",
        "command.verbose.description": "循环切换工具进度显示：off -> new -> all -> verbose",
        "command.yolo.description": "切换 YOLO 模式（跳过所有危险命令审批）",
        "command.reasoning.description": "管理推理强度与显示方式",
        "command.skin.description": "显示或切换界面皮肤/主题",
        "command.language.description": "显示或切换显示语言",
        "command.voice.description": "切换语音模式",
        "command.tools.description": "管理工具：/tools [list|disable|enable] [name...]",
        "command.toolsets.description": "列出可用工具集",
        "command.skills.description": "搜索、安装、查看或管理技能",
        "command.cron.description": "管理定时任务",
        "command.reload-mcp.description": "从配置中重新加载 MCP 服务器",
        "command.browser.description": "将浏览器工具连接到你本地的 Chrome CDP",
        "command.plugins.description": "列出已安装插件及其状态",
        "command.commands.description": "浏览所有命令和技能（分页）",
        "command.help.description": "显示可用命令",
        "command.usage.description": "显示当前会话的 token 用量和速率限制",
        "command.insights.description": "显示用量洞察和分析",
        "command.platforms.description": "显示网关/消息平台状态",
        "command.paste.description": "检查剪贴板中的图片并附加到下一条提示",
        "command.image.description": "为下一条提示附加本地图像文件",
        "command.update.description": "将 Hermes Agent 更新到最新版本",
        "command.quit.description": "退出 CLI",
        "ui.available_commands_header": "(^_^)? 可用命令",
        "ui.skill_commands": "技能命令",
        "ui.installed": "已安装",
        "ui.active": "已启用",
        "ui.tip_chat": "提示：直接输入消息即可与 Hermes 对话",
        "ui.tip_multiline": "多行输入：按 Alt+Enter 换行",
        "ui.tip_attach_image": "附加图片：/image {path}，或直接在提示开头写本地图像路径",
        "ui.tip_paste_image": "粘贴图片：Alt+V（或 /paste）",
        "ui.welcome_default": "欢迎使用 Hermes Agent！直接输入消息，或使用 /help 查看命令。",
        "ui.type_help": "输入 /help 查看可用命令",
        "ui.unknown_command": "未知命令：{command}",
        "ui.ambiguous_command": "命令不明确：{command}",
        "ui.did_you_mean": "你是想输入：{choices}？",
        "ui.gateway_commands": "Hermes 命令",
        "ui.gateway_skill_commands": "技能命令",
        "ui.gateway_more": "还有 {count} 个。使用 `/commands` 查看完整分页列表。",
        "ui.gateway_commands_title": "命令列表",
        "ui.gateway_no_commands": "没有可用命令。",
        "ui.gateway_usage_commands": "用法：`/commands [page]`",
        "ui.gateway_prev": "上一页",
        "ui.gateway_next": "下一页",
        "ui.gateway_unknown_command": "未知命令 `/{command}`。输入 /commands 查看可用命令，或去掉前导斜杠后重新发送，将其作为普通消息处理。",
        "ui.language_current": "当前语言：{language}",
        "ui.language_available": "可用语言：{languages}",
        "ui.language_usage": "用法：/language [en|zh|status]",
        "ui.language_saved": "显示语言已设置为：{language}（已保存）",
        "ui.language_set": "显示语言已设置为：{language}",
        "ui.language_unknown": "未知语言：{language}",
        "ui.language_name.en": "English",
        "ui.language_name.zh": "中文",
    }
}


def normalize_locale(locale: str | None) -> str:
    """Normalize user/config locale values into the supported short codes."""
    if not locale:
        return DEFAULT_LOCALE
    raw = str(locale).strip().lower().replace("_", "-")
    if raw in {"zh", "zh-cn", "zh-hans", "zh-sg"}:
        return "zh"
    if raw in {"en", "en-us", "en-gb"}:
        return "en"
    return DEFAULT_LOCALE


def set_active_locale(locale: str | None) -> str:
    """Set the process-wide active locale and return the normalized value."""
    global _ACTIVE_LOCALE
    _ACTIVE_LOCALE = normalize_locale(locale)
    return _ACTIVE_LOCALE


def get_configured_locale(config: dict[str, Any] | None = None) -> str:
    """Read the preferred display language from config/env."""
    if config is not None:
        display = config.get("display", {}) if isinstance(config, dict) else {}
        return normalize_locale(display.get("language"))

    env_locale = os.getenv("HERMES_DISPLAY_LANGUAGE")
    if env_locale:
        return normalize_locale(env_locale)

    try:
        from hermes_cli.config import read_raw_config

        raw = read_raw_config()
        if isinstance(raw, dict):
            return normalize_locale((raw.get("display") or {}).get("language"))
    except Exception:
        pass
    return DEFAULT_LOCALE


def get_active_locale(config: dict[str, Any] | None = None) -> str:
    """Return the active locale, falling back to config/env."""
    if config is not None:
        return get_configured_locale(config)
    return _ACTIVE_LOCALE or get_configured_locale()


def init_locale_from_config(config: dict[str, Any] | None = None) -> str:
    """Initialize the active locale from config/env."""
    return set_active_locale(get_configured_locale(config))


def tr(key: str, default: str | None = None, *, locale: str | None = None, **kwargs: Any) -> str:
    """Translate *key* for the active locale, with optional format kwargs."""
    loc = normalize_locale(locale) if locale else get_active_locale()
    text = _TRANSLATIONS.get(loc, {}).get(key, default if default is not None else key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


def command_description(name: str, default: str, *, locale: str | None = None) -> str:
    """Return a translated command description."""
    return tr(f"command.{name}.description", default, locale=locale)


def category_label(name: str, *, locale: str | None = None) -> str:
    """Return a translated category label."""
    return tr(f"category.{name}", name, locale=locale)


def language_label(locale: str | None = None) -> str:
    """Return a user-facing language name."""
    normalized = normalize_locale(locale or get_active_locale())
    if normalized == "zh":
        return tr("ui.language_name.zh", "中文", locale=normalized)
    return tr("ui.language_name.en", "English", locale=normalized)
