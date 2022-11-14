import pytest

from src.census_project.modules.utils import get_data_files_path


@pytest.fixture
def data_path():
    """
    Fixture: a Path object to data artifact directory.
    Data directory is found in package structure, using importlib resources module."""

    return get_data_files_path()
