#!/usr/bin/python3

"""
Base class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base model class defining common attributes and methods for other models.
    """
    storage = None

    @classmethod
    def set_storage(cls, storage):
        """
        Class method to set the storage object.
        """
        cls.storage = storage

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.
        Handles both regular initialization and reconstruction from a dictionary.
        """

        if kwargs:
            # Initialize from a dictionary (deserialization)
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        # Convert ISO format strings back to datetime objects
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            # Regular initialization
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        if self.__class__.storage:
            self.__class__.storage.save()

            # If it's a new instance, add it to the storage
            if self.id is None:
                self.__class__.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        model_dict = self.__dict__.copy()  # Get all instance attributes
        model_dict["__class__"] = self.__class__.__name__  # Add class name
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
