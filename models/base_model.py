"#!/usr/bin/python3"
import uuid
import datetime
"""Write a class BaseModel that defines all common attributes/methods
for other classes:"""


class BaseModel():
    """BseModel with the principal function to inherit"""
    def __init__(self):
        """The constructor of base of the class BaseModel"""
        self.id = str(uuid.uuid4())

        timeFormat = datetime.datetime.now()
        self.created_at = timeFormat
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat

    def save(self):
        """saves a new version of class and updates the time of update"""
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat

    def __str__(self):
        """str a function to print the class"""
        txt = "[{}] ({}) {}"
        return txt.format(__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """To_dict function to have a dictionary version of data"""
        instance_dict = self.__dict__
        instance_dict.update({"__class__": __class__.__name__})
        instance_dict.update({"created_at": self.created_at.isoformat()})
        instance_dict.update({"updated_at": self.updated_at.isoformat()})

        return instance_dict
