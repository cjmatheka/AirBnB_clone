#!/usr/bin/env python3

""" File Storage Class """

import json
from datetime import datetime


class FileStorage:
    """Serializes and deserializes objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'."""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with key '<obj class name>.id'.
        Raises an exception if an object with the same key already exists.
        """
        if obj is None:
            raise ValueError("Object not found")

        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            existing_obj = self.__objects[key]
            for attr, value in obj.__dict__.items():
                if attr != 'id' and attr != 'created_at':
                    setattr(existing_obj, attr, value)
            existing_obj.updated_at = datetime.now()  # Update 'updated_at'
        else:
            self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')."""
        try:
            with open(self.__file_path, "w") as f:
                json.dump({key: obj.to_dict()
                           for key, obj in self.__objects.items()}, f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserializes the JSON file to '__objects'."""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = key.split(".")[0]
                    if hasattr(self, class_name):
                        class_instance = getattr(self, class_name)
                        self.__objects[key] = class_instance(**obj_dict)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
