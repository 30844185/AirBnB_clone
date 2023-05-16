#!/usr/bin/python3

"""
models for user class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines attributes for an user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
