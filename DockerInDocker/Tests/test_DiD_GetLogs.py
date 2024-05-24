from unittest.mock import Mock
import pytest
from DiDfunctions import format_message_logs, get_container_logs
from MockVar import mock_client, mock_container


def test_format_message():
    # Example message
    message = '{"Container": "my_container_id"}'

    # Mock the expected behavior
    mock_client.containers.get.return_value = mock_container

    # Call the function
    container, command = format_message_logs(message)

    # Assertions
    assert container == mock_container
    assert command == ""

def test_get_container_logs():
    # Mock the container logs
    mock_container.logs.return_value = b"Container logs"

    # Call the function
    result = get_container_logs(mock_container)

    # Assertions
    assert result['container_id'] == mock_container.id
    assert result['logs'] == "Container logs"


if __name__ == "__main__":
    pytest.main()
