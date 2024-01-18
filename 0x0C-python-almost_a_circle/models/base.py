#!/usr/bin/python3
"""The base class"""
import json


class Base:
    """class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes an instance id

        Args:
            id (int, optional): The id of the instance. If not provided, a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries into a JSON string.

        Args:
            list_dictionaries : A list of dictionaries to convert to JSON.

        Returns:
            str: The JSON string representation of the list of dictionaries.

        Raises:
            ValueError: If the input list is empty.
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
        
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a json file.

        Args:
            list_objs (list): A list of objects to save.

        Returns:
            None
        """
        with open(f'{cls.__name__}.json', "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(json_list)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a JSON string into a Python object.

        Args:
            json_string (str): The JSON string to deserialize.

        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents an instance of the class.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of the class.

        Args:
            **dictionary: The attributes of the instance as keyword arguments.

        Returns:
            The newly created instance.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            else:
                dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads all objects of the class from a json file.

        Returns:
            A list of objects of the class. If the file does not exist or is empty, an empty list is returned.
        """
        try:
            with open(f'{cls.__name__}.json', "r", encoding="utf-8") as f:
                json_string = f.read()
                instance_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**instance_dict) for instance_dict in instance_dicts]
                return instances
        except FileNotFoundError:
            return []
