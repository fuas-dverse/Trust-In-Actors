import json
from unittest.mock import Mock
import pytest
from DiDfunctions import format_message_command, proccess_command_container

# Mock the client and container objects for testing
mock_client = Mock()
mock_container = Mock()

def test_format_message():
    # Example message
    message = '{"Command": "run", "Container": "my_container_id"}'

    # Mock the expected behavior
    mock_client.containers.get.return_value = mock_container

    # Call the function
    container, command = format_message_command(message)

    # Assertions
    assert command == "run"

def test_proccess_command_container():
    # Mock the container exec_run output
    mock_container.exec_run.return_value = (None, b"Command executed successfully")

    # Call the function with a sample action
    result = proccess_command_container(mock_container, "echo Hello, World!")

    # Assertions
    assert result == "Command executed successfully"



if __name__ == "__main__":
    pytest.main()