from unittest.mock import Mock
import pytest
from DiDfunctions import format_message_remove, remove_container
from MockVar import mock_client, mock_container


def test_format_message():
    # Example message
    message = {"Container": "my_container_id"}

    # Mock the expected behavior
    mock_client.containers.get.return_value = mock_container

    # Call the function
    container, command = format_message_remove(message)

    # Assertions
    assert container == mock_container
    assert command == ""

def test_remove_container():
    # Mock the container removal response
    mock_container.remove.return_value = {"message": "Container removed"}

    # Call the function
    result = remove_container("my_container_id")

    # Assertions
    assert result == {"message": "Container removed"}

# Add more tests as needed

if __name__ == "__main__":
    pytest.main()