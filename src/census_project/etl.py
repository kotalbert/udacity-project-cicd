"""
ETL getting data for analysis
"""

import subprocess
from enum import Enum
from pathlib import Path

import pkg_resources
import requests
from hydra import initialize, compose
from omegaconf import DictConfig


class DataFileKeys(Enum):
    """Enum for Data file name keys, to read from config.
    It is to make sure, that wrong config key is not used.
    """

    raw = 'raw'
    transformed = 'transformed'


def get_config() -> DictConfig:
    """Helper to get hydra config dictionary."""

    with initialize(config_path='conf', job_name='etl'):
        return compose('config')


def get_data_file_path(file_key: str) -> Path:
    """
    Get absolute path to data file, based on data config keys.

    :param file_key: File key to be found in config. Must be one of values of
    DataFileKeys enum, otherwise will throw key error.
    """

    cfg = get_config()['data']

    filename = pkg_resources.resource_filename(cfg['local_path'],
                                               cfg[file_key])
    return Path(filename)


def extract() -> None:
    """Pull the raw data from Internet."""

    cfg = get_config()['data']
    r = requests.get(cfg['source_url'])

    if not r.ok:
        r.raise_for_status()

    with open(get_data_file_path(DataFileKeys.raw.value), 'wb') as f:
        f.write(r.content)


def transform() -> None:
    """Transform raw data.

    Read raw data from file, transform and write new to output file.
    Transformations:
        * Trim white spaces

    """

    with open(get_data_file_path(DataFileKeys.raw.value), 'r') as f:
        text = f.read().replace(' ', '')

    with open(get_data_file_path(DataFileKeys.transformed.value), 'w') as f:
        f.write(text)


def load():
    """
    Put transformed data to dvc repo.
    Need to call subprocess, as dvc api is supporting only read operations.
    """

    subprocess.run(['dvc', 'add',
                    get_data_file_path(DataFileKeys.transformed.value)])
    subprocess.run(['dvc', 'push'])
