"#!/usr/bin/python3"
import uuid
import datetime
"""Write a class BaseModel that defines all common attributes/methods
for other classes:"""


class BaseModel():
    """BseModel with the principal function to inherit"""
    def __init__(self, id=uuid.uuid4(), created_at=None, updated_at=None):
        """the constructor of base"""
        self.id = str(id)

        timeFormat = datetime.datetime.now()
        self.created_at = timeFormat
        timeFormat = datetime.now()
        self.updated_at = timeFormat

    def save(self):
        """saves a new version of class and updates the time of update"""
        timeFormat = datetime.now()
        self.updated_at = timeFormat

    def __str__(self):
        """str a function to print the class"""
        txt = "[{}] ({}) <{}>"
        return txt.format(BaseModel.__name__, self.id, self.__dict__)

    def to_dict(self):
        """To_dict function to have a dictionary version of data"""

        self.__dict__.update({"__class__": BaseModel.__name__})
        self.__dict__.update({"created_at": self.created_at.isoformat()})
        self.__dict__.update({"updated_at": self.updated_at.isoformat()})

        return self.__dict__
