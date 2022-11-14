"""Utilities module"""
import os.path
from enum import Enum
from pathlib import Path
from typing import Optional

import pkg_resources
from hydra import initialize, compose
from importlib_resources import files
from omegaconf import DictConfig

from src.census_project import artifacts
from src.census_project.artifacts import data

# fixme: can this be interpolated?
CONFIG_DIR_NAME = 'conf'


class DataFileKeys(Enum):
    """Enum for Data file name keys, to read from config.
    It is to make sure, that wrong config key is not used.
    """

    RAW = 'raw'
    TRANSFORMED = 'transformed'


def get_data_files_path() -> Path:
    """Get absolute path to data files directory."""

    filename = files(data)
    return Path(filename)


def compose_config() -> DictConfig:
    """
    Helper to get hydra config dictionary.

    Assumes that config module is sources root.
    """

    config_pth = Path('..', CONFIG_DIR_NAME)
    with initialize(config_path=config_pth, version_base=None, job_name='etl'):
        return compose('config')


def get_config(key: Optional[str] = None) -> DictConfig:
    """
    Get config based on key.
    :param key: optional, key to extract sub config from config.
    Defaults to None, and in that case entire composed config is returned.
    :raises: KeyError if key not present in config
    """
    config = compose_config()

    if key is None:
        return config

    return config[key]


def get_data_artifacts_path(filename: str) -> Path:
    """
    Get absolute path to data file, in `artifacts` directory.

    :param filename: File key to be found in config. Must be one of values of
    DataFileKeys enum, otherwise will throw key error.
    """

    data_artefacts_module_path = files(artifacts.data)
    artifact_path = Path(data_artefacts_module_path, filename)
    return artifact_path


def pull_from_dvc(artifact_name: str, path: Path) -> None:
    """
    Pull data from DVC remote repository and it on local filesystem.
    :param artifact_name: name of artifact in remote
    :param path: Path object where data is to be saved on filesystem.
    """
    pass
