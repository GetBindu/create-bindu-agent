from unittest.mock import MagicMock, patch

from {{cookiecutter.project_slug}}.main import handler


def test_handler():
    """Test that handler accepts messages and returns a RunOutput."""
    messages = [{"role": "user", "content": "Hello, how are you?"}]

    # Mock the agent.run response
    mock_response = MagicMock()
    mock_response.run_id = "test-run-id"
    mock_response.status = "COMPLETED"

    with patch("{{cookiecutter.project_slug}}.main.agent.run", return_value=mock_response):
        result = handler(messages)

    # Check that we get a result back
    assert result is not None

    # Check that the result has expected attributes from agno RunOutput
    assert hasattr(result, "run_id")
    assert hasattr(result, "status")
    assert result.run_id == "test-run-id"
    assert result.status == "COMPLETED"
