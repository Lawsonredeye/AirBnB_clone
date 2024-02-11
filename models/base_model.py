#!/usr/bin/python3
"""
Module for parent class which would act as the base
class for inheriting sub-classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        # used uuid4 as it has much better security
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        obj_str = datetime.strptime(value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, obj_str)
                    else:
                        setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")
