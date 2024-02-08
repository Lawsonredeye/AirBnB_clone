#!/usr/bin/python3
"""
class module that serves as a storage for our
airbnb web application which can be called at
any time using json
"""
import json


class FileStorage:
    """
    class storage to store all instances that would be created
    for all instances

    Args:
        __file_path : path to file
        __object: dictionary for storing key and values
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary values like a getter
        """
        return self.__objects

    def new(self, obj):
        """
        Creates/ instanciate the class object name with the class object
        id and then pass the value (obj) into the key of the __object dict

        Args:
            obj: value to be added to the __object attribute
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves all instances created into a json format and
        dumps into a file which it can be called from when needed.
        Creates a file if it doesnt exist
        """
        with open("file.json", "w+", encoding="utf-8") as f:
            json.dump(self.__file_path, f)

    def reload(self):
        """
        Deserialize the JSON string inside of the __objects attribute
        and then doesnt pass an error if the file is not in existence
        """
        if self.__file_path is not None:
            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    self.__objects = json.load(f)
            except FileNotFoundError:
                pass