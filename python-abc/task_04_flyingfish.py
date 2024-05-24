#!/usr/bin/python3
"""Construct a FlyingFish class that inherits from both a
Fish class and a Bird class. Within FlyingFish, override
methods from both parents. The goal is to comprehend multiple
inheritance and how Python determines method resolution order.
"""


class Fish:
    """defines a fish class"""
    def swim(self):
        """creating a swim method"""
        print("The fish is swimming")

    def habitat(self):
        """creating a habitat method"""
        print("The fish lives in water")


class Bird:
    """defines a bird class"""
    def fly(self):
        """creating a fly method"""
        print("The bird is flying")

    def habitat(self):
        """creating a habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Construct a FlyingFish class that inherits
    from both Fish and Bird"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
