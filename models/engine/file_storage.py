#!/usr/bin/python3

""" File Storage Class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    # Mapping of class names to corresponding classes
    CLASS_MAPPING = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def all(self):
        """Returns the dictionary '__objects'."""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with key '<obj class name>.id'."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')."""
        with open(self.__file_path, "w") as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'."""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = key.split(".")[0]
                    if class_name in self.CLASS_MAPPING:
                        class_instance = self.CLASS_MAPPING[class_name]
                        self.__objects[key] = class_instance(**obj_dict)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
