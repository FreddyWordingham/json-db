from pathlib import Path
from typing import Dict, Type
import json
import os

from pydantic import BaseModel
from typeguard import typechecked
import pytest

from json_db import JSONDatabase


# Define sample Pydantic models.
class User(BaseModel):
    id: int
    name: str


class Project(BaseModel):
    id: int
    title: str


# Fixture for the path to the JSON file.
@pytest.fixture
@typechecked
def json_file_path() -> Path:
    # Create a temporary directory for the JSON file.
    os.makedirs("tmp", exist_ok=True)
    return Path(os.path.join("tmp", "test_database.json"))


# Fixture for the database mapping.
@pytest.fixture
@typechecked
def db_mapping() -> Dict[str, Type[BaseModel]]:
    return {
        "users": User,
        "projects": Project,
    }


# Fixture for creating a JSONDatabase instance.
@pytest.fixture
@typechecked
def database(db_mapping: Dict[str, Type[BaseModel]]):
    return JSONDatabase(db_mapping)


# Test initialising JSONDatabase.
@typechecked
def test_init_database(db_mapping: Dict[str, Type[BaseModel]]):
    db = JSONDatabase(db_mapping)

    assert hasattr(db, "users")
    assert hasattr(db, "projects")


# Test loading JSONDatabase.
@typechecked
def test_load_database(db_mapping: Dict[str, Type[BaseModel]], json_file_path: Path):
    sample_data = {
        "users": {
            "1": {"id": 1, "name": "John Doe"},
        },
        "projects": {
            "101": {"id": 101, "title": "Alpha Project"},
        },
    }
    json_file_path.write_text(json.dumps(sample_data))

    db = JSONDatabase.load(db_mapping, json_file_path)

    assert isinstance(db.users["1"], User)
    assert db.users["1"].name == "John Doe"
    assert isinstance(db.projects["101"], Project)
    assert db.projects["101"].title == "Alpha Project"


# Test accessing data from JSONDatabase.
@typechecked
def test_access_data(database: JSONDatabase):
    user = User(id=2, name="Jane Smith")
    project = Project(id=102, title="Beta Project")
    database.users["2"] = user
    database.projects["102"] = project

    assert database.users["2"].name == "Jane Smith"
    assert database.projects["102"].title == "Beta Project"


# Test saving JSONDatabase.
@typechecked
def test_save_database(json_file_path: Path, database: JSONDatabase):
    database.users["3"] = User(id=3, name="Alice Jones")
    database.projects["103"] = Project(id=103, title="Gamma Project")
    database.save(json_file_path)

    saved_data = json.loads(json_file_path.read_text())
    assert saved_data["users"]["3"] == r"""{"id":3,"name":"Alice Jones"}"""
    assert saved_data["projects"]["103"] == r"""{"id":103,"title":"Gamma Project"}"""
