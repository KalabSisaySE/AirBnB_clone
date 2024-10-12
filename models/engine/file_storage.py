#!/usr/bin/python3
"""the json file storage engine module"""
import json


class FileStorage:
    """represents the json file storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds the give `obj` to list of objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        dict_data = {}
        for key, val in FileStorage.__objects.items():
            dict_data[key] = val.to_dict()

        with open(self.__file_path, "w") as file:
            file.write(json.dumps(dict_data))

    def reload(self):
        """deserializes JSON file back to objects"""
        from models.base_model import BaseModel

        json_data = None
        try:
            with open(self.__file_path, "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
            pass

        if json_data:
            for key, val in json_data.items():
                class_name = key.split(".")[0]
                obj = eval(f"{class_name}(**{val})")
                FileStorage.__objects[key] = obj
