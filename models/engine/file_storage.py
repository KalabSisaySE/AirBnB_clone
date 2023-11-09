#!/usr/bin/python
"""the `file_storage` module
defines the class `FileStorage`"""
import json
import os


class FileStorage:
    """serlializes/deserializes instance and json file"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """instantiates a new `FileStorage` engine"""

    def all(self):
        """returns the dictionary of stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """inserts `obj` into stored objects with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes stored objects to JSON file"""
        json_data = {}
        for k, v in FileStorage.__objects.items():
            json_data.update({k: v.to_dict()})
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(json_data))

    def reload(self):
        """deserializes a JSON file to stored objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                from models.base_model import BaseModel
                json_data = json.loads(f.read())
                for k, v in json_data.items():
                    class_name = k.split(".")[0]
                    FileStorage.__objects.update(
                        {k: locals()[class_name](**v)}
                    )
