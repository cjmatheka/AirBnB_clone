#!/usr/bin/python3

""" Review Class """

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review with text, and associated Place ID and User ID"""
    place_id = ""
    user_id = ""
    text = ""
