"""Utilities module"""
from enum import Enum
from pathlib import Path

from hydra import initialize, compose
from importlib_resources import files
from omegaconf import DictConfig

from src.census_project.artefacts import data


def get_data_files_path():
    """Get absolute path to data files directory."""

    filename = files(data)
    return Path(filename)


def pull_from_dvc(artifact_name: str, path: Path) -> None:
    """
    Pull data from DVC remote repository and it on local filesystem.
    :param artifact_name: name of artifact in remote
    :param path: Path object where data is to be saved on filesystem.
    """
    pass


class DataFileKeys(Enum):
    """Enum for Data file name keys, to read from config.
    It is to make sure, that wrong config key is not used.
    """

    RAW = 'raw'
    TRANSFORMED = 'transformed'


def get_config() -> DictConfig:
    """Helper to get hydra config dictionary."""

    with initialize(config_path='conf', job_name='etl'):
        return compose('config')


def get_data_config() -> DictConfig:
    """Helper to get only `data` entries from config."""

    config = get_config()
    return config['data']
