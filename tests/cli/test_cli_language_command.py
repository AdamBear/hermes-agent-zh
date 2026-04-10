from unittest.mock import MagicMock, patch

from cli import HermesCLI
from hermes_cli.commands import rebuild_lookups
from hermes_cli.i18n import get_active_locale, set_active_locale


def _make_cli():
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.config = {"display": {"language": "en"}}
    cli_obj.console = MagicMock()
    cli_obj.agent = None
    cli_obj.conversation_history = []
    cli_obj.session_id = None
    cli_obj._pending_input = MagicMock()
    return cli_obj


def test_language_command_switches_locale_and_saves():
    cli_obj = _make_cli()
    previous = get_active_locale()
    try:
        with patch("builtins.print") as mock_print, patch("cli.save_config_value", return_value=True) as mock_save:
            cli_obj._handle_language_command("/language zh")
        mock_save.assert_called_once_with("display.language", "zh")
        assert cli_obj.config["display"]["language"] == "zh"
        assert get_active_locale() == "zh"
        printed = " ".join(str(call) for call in mock_print.call_args_list)
        assert "中文" in printed
    finally:
        set_active_locale(previous)
        rebuild_lookups()


def test_language_command_status_prints_current_language():
    cli_obj = _make_cli()
    previous = get_active_locale()
    try:
        set_active_locale("en")
        rebuild_lookups()
        with patch("builtins.print") as mock_print:
            cli_obj._handle_language_command("/language status")
        printed = " ".join(str(call) for call in mock_print.call_args_list)
        assert "Current language" in printed
    finally:
        set_active_locale(previous)
        rebuild_lookups()
