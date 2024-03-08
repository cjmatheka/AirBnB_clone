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
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]  # Extract class name
                    if class_name in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
                        self.__objects[key] = eval(class_name)(**value)  # Dynamically create instances

        except (FileNotFoundError, json.JSONDecodeError):
            pass
