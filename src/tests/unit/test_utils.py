"""
Unit test for project utilities
"""
import pytest

from src.census_project.modules.utils import compose_config, get_config, get_data_artifacts_path


@pytest.mark.parametrize('test_input_key', ['data'])
def test_compose_config(test_input_key):
    config = compose_config()
    assert config.get(test_input_key) is not None


@pytest.mark.parametrize('key,expected_keys', [
    (None, {'data'}),
    ('data', {'source_url', 'raw', 'transformed', 'timeout'})
])
def test_get_config(key, expected_keys):
    """
    The `get_config` function should create a dictionary with sub config, that
    contain expected keys.
    """

    config = get_config(key)
    assert expected_keys.issubset(config.keys())


# todo: change parameters to dvc files
@pytest.mark.parametrize('test_filename', ['__init__.py', 'transformed.csv'])
def test_get_data_artifacts_path(test_filename):
    """Path to data artefact should be an existing file."""

    file_path = get_data_artifacts_path(test_filename)
    assert file_path.exists()
    assert file_path.is_file()

