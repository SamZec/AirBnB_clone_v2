#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """
            Init for inherited
        """
        super().__init__(*args, **kwargs)
    if getenv('HBNB_TYPE_STORAGE') != db:
        @property
        def cities(self):
            """This is the property setter for cities
            Return:
            all object in list
            """
            get_all = models.storage.all("City").values()
            return [obj for obj in get_all if obj.state_id == self.id]
