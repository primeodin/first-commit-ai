from first_commit_ai.cli import build_parser, main
from first_commit_ai.client import ChatClient


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


def test_no_args_prints_tip_and_exits_zero(capsys):
    code = main([])
    captured = capsys.readouterr()
    assert code == 0
    assert "Tip: Run with --mock" in captured.out
    assert "README.md" in captured.out


def test_help_epilog_shows_flow(capsys):
    p = build_parser()
    try:
        p.parse_args(["--help"])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "clone   ->" in captured.out
    assert "install ->" in captured.out
    assert "mock    ->" in captured.out
    assert "real    ->" in captured.out
