"""
Unit tests for etl module
"""
import pandas as pd
import pytest
from pandas import DataFrame

from src.census_project.modules.etl import extract, transform, load
from src.census_project.modules.utils import DataFileKeys, get_data_file_path


def test_get_file_path():
    """Getting path by config key should return correct file name."""

    actual = get_data_file_path(DataFileKeys.RAW.value).name
    expected = 'census.csv'

    assert expected == actual


def test_extract(data_path):
    """Extract should pull raw 'census.csv' to data path."""

    csv = 'census.csv'
    data_filename = data_path.joinpath(csv)
    data_filename.unlink(missing_ok=True)
    extract()

    assert data_path.joinpath(csv).exists()


def test_transform(data_path):
    """Transform step should create 'transformed.csv' in data path."""

    csv = 'transformed.csv'
    data_filename = data_path.joinpath(csv)
    data_filename.unlink(missing_ok=True)
    extract()
    transform()

    assert data_path.joinpath(csv).exists()


@pytest.fixture
def transformed_data_df():
    """Fixture to get clean/transformed data."""

    extract()
    transform()

    return pd.read_csv(get_data_file_path('transformed'))


def test_transform_df_shape(transformed_data_df):
    """Transformed data should be a data frame and have expected shape (not empty)."""

    assert isinstance(transformed_data_df, DataFrame)
    assert transformed_data_df.shape[0] > 0
    assert transformed_data_df.shape[1] >= 15


@pytest.mark.parametrize('expected_var_name',
                         ['age', 'workclass', 'fnlgt', 'education',
                          'education-num', 'marital-status', 'occupation',
                          'relationship'])
def test_transform_column_names(transformed_data_df, expected_var_name):
    """Extracted data should contain expected variable name."""

    assert expected_var_name in list(transformed_data_df.columns)


def test_load():
    """ETL process should run and complete without errors."""

    extract()
    transform()
    load()
