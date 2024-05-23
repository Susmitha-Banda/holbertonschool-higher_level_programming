#!/usr/bin/python3
"""this module is about creating an abstract class named Animal using the ABC
package."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """this is an abstract class Animal"""
    @abstractmethod
    def sound(self):
        """abstract method for making a sound"""
        pass


class Dog(Animal):
    """this is a dog subclass of Animal"""
    def sound(self):
        """sound method of dog class"""
        return ("Bark")


class Cat(Animal):
    """this is a cat subclass of Animal"""
    def sound(self):
        """sound method of cat class"""
        return ("Meow")
