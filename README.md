# json_db

<p align="center">
    <img src="./assets/icon.png" alt="arc-accounts logo" width="200" height="200">
</p>

![Version Badge](https://img.shields.io/badge/version-0.0.0-gold)
[![CI](https://github.com/FreddyWordingham/json_db/actions/workflows/ci.yml/badge.svg)](https://github.com/FreddyWordingham/json_db/actions/workflows/ci.yml)
![Coverage Badge](https://img.shields.io/badge/test_coverage-80%25-brightgreen)
![Complexity Badge](https://img.shields.io/badge/complexity-A-cyan)
![Maintainability Badge](https://img.shields.io/badge/maintainability-100%25-blue)

An in-memory database using .json files, akin to MongoDB for lightweight, RAM-based data handling.

## Installation

Clone this repository, and set the current directory to the root of the repository:

```bash
git clone git@github.com:FreddyWordingham/json_db.git
cd json_db
```

Install the package and its dependencies:

```bash
poetry env use python3.10
poetry install
```

To ensure code quality and consistency, please set up Git hooks when you start working on the project:

```bash
sh ./ci/setup_hooks.sh
```

This will run the pre-commit checks before pushing your changes to GitHub.
