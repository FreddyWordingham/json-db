from pathlib import Path
from typing import Dict, Type
import json

from pydantic import BaseModel
from typeguard import typechecked


class JSONDatabase:
    @typechecked
    def __init__(self, mapping: Dict[str, Type[BaseModel]]):
        self._mapping = set(mapping.keys())
        for key in mapping.keys():
            setattr(self, key, {})

    @typechecked
    @staticmethod
    def load(mapping: Dict[str, Type[BaseModel]], path: Path) -> "JSONDatabase":
        json_str = path.read_text()
        data_dict = json.loads(json_str)

        database = JSONDatabase(mapping)
        for key, collection in data_dict.items():
            record_type = mapping.get(key)
            if record_type:
                records = {
                    id: record_type.model_validate(record)
                    for id, record in collection.items()
                }
                setattr(database, key, records)

        return database

    @typechecked
    def save(self, path: Path):
        data_dict = {}
        for key in self._mapping:
            collection = getattr(self, key)
            data_dict[key] = {
                id: (
                    record.model_dump_json()
                    if isinstance(record, BaseModel)
                    else record
                )
                for id, record in collection.items()
            }

        json_str = json.dumps(data_dict, indent=4)
        path.write_text(json_str)
