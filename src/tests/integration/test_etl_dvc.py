"""Integration test suite: test how components integrate with one another and other systems"""
from src.census_project.modules.utils import pull_from_dvc


def test_dvc_pull():
    """DVC pull should create a file on filesystem."""

    pull_from_dvc()