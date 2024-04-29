# JSON-DB

<p align="center">
    <img src="./assets/icon.png" alt="json-db logo" width="200" height="200">
</p>

![Version Badge](https://img.shields.io/badge/version-0.0.0-gold)
[![CI](https://github.com/FreddyWordingham/json-db/actions/workflows/ci.yml/badge.svg)](https://github.com/FreddyWordingham/json-db/actions/workflows/ci.yml)
![Coverage Badge](https://img.shields.io/badge/test_coverage-80%25-brightgreen)
![Complexity Badge](https://img.shields.io/badge/complexity-A-cyan)
![Maintainability Badge](https://img.shields.io/badge/maintainability-100%25-blue)

An in-memory database using .json files, akin to MongoDB for lightweight, RAM-based data handling.

## Overview

This package exports the `JSONDatabase` class which can be used to operate a database of JSON documents in memory.

### Load a Database

Load a Database from a file by providing a mapping of collections to classes, and the path to the database file:

```python
from pathlib import Path

from json_db import JSONDatabase

MAPPING = {
    "users": User,
    "projects": Project,
}
database_path = Path("path/to/database.json")


db = JSONDatabase.load(MAPPING, database_path)
```

### Use the Database

Any of the collections defined in the mapping can be accessed as attributes of the Database object:

```python
users = db.users
```

Access specific documents in a collection by their ID:

```python
user_id = "someuserid

user = users.get(user_id)
```

### Save the Database

Save a Database to a .json file by providing the path to the database file:

```python
db.save(database_path)
```

## Installation

Clone this repository, and set the current directory to the root of the repository:

```bash
git clone git@github.com:FreddyWordingham/json-db.git
cd json-db
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
