#!/usr/bin/python3
"""this module is about creating an abstract class named VerboseList
that extends the Python list class. This custom class should print
a notification message every time an item is added
(using the append or extend methods) or
removed (using the remove or pop methods).
"""


class VerboseList(list):
    def append(self, item):
        """Override the append method to add an item and print a message."""
        super().append(item)  # Call the original append method
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Override the extend method to extend
        the list and print a message."""
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Override the remove method to remove an item and print a message."""
        super().remove(item)  # Call the original remove method
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Override the pop method to pop an item and print a message."""
        # Step 1: Accessing the item to be popped
        item = self[index]  # Get the item to be popped

        # Step 2: Printing a message about the operation
        print(f"Popped [{item}] from the list.")

        # Step 3: Calling the original pop method and returning the popped item
        return super().pop(index)
