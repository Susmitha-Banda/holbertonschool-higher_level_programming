#!/usr/bin/python3
"""Creating a class named CountedIterator that extends
the built-in iterator obtained from the iter function.
The CountedIterator should keep track of the number of
items that have been iterated over. Specifically,
you will need to override the __next__ method to
increment a counter each time an item is fetched."""


class CountedIterator:
    '''A custom iterator that counts items iterated over.'''

    def __init__(self, iterable):
        '''Initializing with an iterable and setting up the iterator
        and counter.'''
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """It tries to fetch the next item using next(self.iterator)."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")

    def get_count(self):
        """returns the current count of items iterated """
        return self.count
