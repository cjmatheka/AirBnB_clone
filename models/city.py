#!/usr/bin/python3

""" City Class """

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City with a name and associated State ID"""
    state_id = ""
    name = ""
