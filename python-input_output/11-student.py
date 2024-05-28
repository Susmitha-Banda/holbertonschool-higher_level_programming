#!/usr/bin/python3
"""
Defines a student by their first name, last name, and age.
"""


class Student:
    """
    Initializes a Student instance with the given attribute

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with the data from a JSON-like dictionary.

        Args:
            json(dict): A dictionary where keys
            are attribute names and values are attribute values"""
        for key, value in json.items():
            setattr(self, key, value)
