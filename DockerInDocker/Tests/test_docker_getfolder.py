from unittest.mock import Mock
import pytest
from DiDfunctions import format_message_folder,get_tarball
from MockVar import mock_client, mock_container

# Global var
file_content =b"File content"

def test_format_message():
    # Example message
    message = '{"DownloadWhat": "ALL", "Container": "my_container_id"}'

    # Mock the expected behavior
    mock_client.containers.get.return_value = mock_container

    # Call the function
    container, command = format_message_folder(message)

    # Assertions
    assert container == mock_container
    assert command == "ALL"

def test_get_tarball_all():
    # Mock the container export output
    mock_container.export.return_value = b"Tarball data"

    # Call the function with "ALL" command
    result = get_tarball(mock_container, "ALL")

    # Assertions
    assert result == b"Tarball data"

def test_get_tarball_single_file():
    # Mock the container get_archive output
    mock_container.get_archive.return_value = (file_content,None)

    # Call the function with a specific file
    result = get_tarball(mock_container, "/path/to/file.txt")

    # Assertions
    assert result == file_content

def test_get_tarball_single_file_none():
    # Mock the container get_archive output
    mock_container.get_archive.return_value = (None,file_content)

    # Call the function with a specific file
    result = get_tarball(mock_container, "/path/to/file.txt")

    # Assertions
    assert result ==None


if __name__ == "__main__":
    pytest.main()