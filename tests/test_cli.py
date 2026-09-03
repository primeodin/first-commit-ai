from first_commit_ai.cli import build_parser, main
from first_commit_ai.client import DEFAULT_SYSTEM, ChatClient


def test_mock_chat_is_deterministic():
    client = ChatClient(mock=True)
    out = client.chat("hi")
    assert out.startswith("[mock]")
    assert "hi" in out


def test_parser_requires_prompt():
    p = build_parser()
    args = p.parse_args(["hello world", "--mock"])
    assert args.prompt == "hello world"
    assert args.mock is True


def test_main_mock_exits_zero(capsys):
    code = main(["--mock", "ship it"])
    captured = capsys.readouterr()
    assert code == 0
    assert "[mock]" in captured.out
    assert "ship it" in captured.out


def test_missing_key_without_mock_fails(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    client = ChatClient.from_env(mock=False)
    try:
        client.chat("hi")
        assert False, "expected RuntimeError"
    except RuntimeError as exc:
        assert "OPENAI_API_KEY" in str(exc)


def test_system_flag_overrides_default(capsys):
    code = main(["--mock", "--system", "Answer like a shop dad", "What is git?"])
    out = capsys.readouterr().out
    assert code == 0
    assert "Answer like a shop dad" in out
    assert "What is git?" in out


def test_parser_system_default_none():
    args = build_parser().parse_args(["hi", "--mock"])
    assert args.system is None


def test_help_mentions_mock_and_system():
    p = build_parser()
    help_text = p.format_help()
    assert "--mock" in help_text
    assert "--system" in help_text
    assert "Ollama" in help_text or "OPENAI" in help_text
