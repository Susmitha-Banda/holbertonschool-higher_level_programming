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
    lines = []
    line_start = 0

    for i in range(len(text)):
        if text[i] in separators:
            lines.append(text[line_start:i+1].strip())
            lines.append('')  # Add two new lines
            line_start = i + 1

    # Add the last segment of text
    if line_start < len(text):
        lines.append(text[line_start:].strip())

    # Print each line with no leading or trailing spaces
    for idx, line in enumerate(lines):
        if line:
            print(line)  # Print each line
            if idx % 2 == 0:  # Check if line is a separator line
                print()  # Print extra newline after separator lines
