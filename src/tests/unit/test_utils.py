"""
Unit test for project utilities
"""
import pytest

from src.census_project.modules.utils import get_config


# todo: remember to include other config keys
@pytest.mark.parametrize('test_input_key', ['data'])
def test_get_config(test_input_key):
    config = get_config()
    assert config.get(test_input_key) is not None
