# Udacity Project: Deploying a Machine Learning Model

This repository contains a project for Udacity Machine Learning DevOps Engineer nanodegree:
Deploying a Machine Learning Model on Heroku with FastAPI.

The project consists of the following stages:

1. ETL process:
2. Model Training and Validation
3. REST API
4. CI\CD

## Project structure

The `tree` program generates the project structure.

```sh
$ tree -P "*.py" -I "__*|dist|*egg-info" -L 3

.
├── main.py
├── sanitycheck.py
├── setup.py
└── src
    ├── census_project
    │   ├── conf
    │   ├── data
    │   ├── etl.py
    │   ├── ml
    │   ├── model
    │   └── train_model.py
    └── tests
        ├── component
        ├── conf
        ├── integration
        └── unit
```

Source code, tests, and artifacts (data, inference artifacts) are in the `src` directory.
Artifacts are not committed to the git repository; instead, they are stored externally in the S3 bucket and referred to with the [Data Version Control(DVC)][1] system.

The project uses [hydra framework][2] to manage the application's configuration.

The `src/`census_project contains the `ml` module for training and validating the inference model, built with the [scikit-learn machine learning library][3].

<!--  todo: make sure tests are described-->
The `src/tests` include test suites for the project. Tests are divided into unit, component, and integration test suites.

<!-- todo: add a description of API -->

[1]: https://dvc.org/
[2]: https://hydra.cc/docs/intro/
[3]: https://scikit-learn.org/stable/

## ETL Process

The ETL process module

- Get the raw data,
- Store the "raw" data in a remote data repository,
- Retrieve "raw" data from a remote data repository,
- Process "raw" data to prepare it for model building as "clean" data,
- Store the "clean" data in the data repository

## Model Training and Validation

### Model Card

#### Model Details

#### Intended Use

#### Metrics

#### Data

#### Bias

## REST API

## CI/CD
