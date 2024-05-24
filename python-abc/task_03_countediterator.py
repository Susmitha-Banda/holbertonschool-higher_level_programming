#!/usr/bin/python3
"""Creating a class named CountedIterator that extends
the built-in iterator obtained from the iter function.
The CountedIterator should keep track of the number of
items that have been iterated over. Specifically,
you will need to override the __next__ method to
increment a counter each time an item is fetched."""


class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        # This is required to make CountedIterator iterable
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")

    def get_count(self):
        return self.count
