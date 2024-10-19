#!/usr/bin/python3
"""the json file storage engine module"""
import json


class FileStorage:
    """represents the json file storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns all objects or only classes of given type"""
        if cls:
            if isinstance(cls, str):
                class_name = cls
            else:
                class_name = cls.__name__
            objs = {}
            for key, val in FileStorage.__objects.items():
                if key.startswith(class_name):
                    objs[key] = val

            return objs

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
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

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

    def delete(self, obj=None):
        """deletes the given object from the storage"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
