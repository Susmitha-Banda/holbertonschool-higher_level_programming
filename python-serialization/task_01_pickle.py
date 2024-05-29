#!/usr/bin/env python3
"""serialize and deserialize custom Python
objects using the pickle module"""

import pickle


class CustomObject:
    """CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the object’s attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """This method will take a filename as its parameter.
        Using the pickle module, it will serialize the current instance
        of the object and save it to the provided filename."""

        try:
            with open(filename, "wb")as f:
                pickle.dump(self, f)
        except (FileNotFoundError, IOError) as e:
            # Handle file-related errors, such as file not found or I/O errors
            print(f"Error saving object to file: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """This class method will take a filename as its parameter.
        Using the pickle module, it will load and return an instance
        of the CustomObject from the provided filename."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"{e}")
            return None
