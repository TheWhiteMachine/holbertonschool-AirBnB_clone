"#!/usr/bin/python3"
"""a"""
import uuid
import datetime

class BaseModel():
    """BseModel"""
    def __init__(self, id=uuid.uuid4(), created_at=None, updated_at=None):
        """the constructor"""
        self.id = str(id)

        timeFormat = datetime.datetime.now()
        self.created_at = timeFormat.isoformat()
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat.isoformat()

    def save(self):
        """save"""
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat.isoformat()

    def __str__(self):
        """str"""
        txt = "[{}] (<{}>) <{}>"
        return txt.format(BaseModel.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """To_dict"""

        return {"__class__": __class__.__name__,"id": self.id, "created_at": self.created_at, "updated_at": self.updated_at}
    