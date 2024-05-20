#!/usr/bin/python3

""" function represents a text with 2 new lines """


def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :

    Args:
    - text (str): The input text to be processed

    Raises:
    - TypeError: If text is not a string

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']

    char = 0
    while char < len(text):
        print(text[char], end="")
        if text[char] in separators:
            print("\n")
            while text[char + 1] == " ":
                char += 1
        char += 1
