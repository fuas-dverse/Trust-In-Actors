import json
from unittest.mock import Mock
import pytest
from DiDfunctions import proccess_run_container,format_message_running
from MockVar import mock_client, mock_container

def test_format_message():
    # Example message
    message = '{"Action": "start", "Container": "my_container_id"}'

    # Mock the expected behavior
    mock_client.containers.get.return_value = mock_container

    # Call the function
    container, command = format_message_running(message)

    # Assertions
    assert container == mock_container
    assert command == "start"

def test_proccess_run_container():
    # Mock the container status
    mock_container.status = "paused"

    # Call the function with "start" action
    result = proccess_run_container(mock_container, "start")
    assert result == "Container started"

    # Call the function with "pause" action
    result = proccess_run_container(mock_container, "pause")
    assert result == "Container paused"

    # Call the function with unsupported action
    result = proccess_run_container(mock_container, "invalid_action")
    assert result == "This action is not supported"

# Add more tests as needed

if __name__ == "__main__":
    pytest.main()
