#!/usr/bin/env python3
"""In this exercise we’ll explore serialization
and deserialization using XML as an alternative format to JSON."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """This will take a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML
    and save it to the given filename."""

    # Create a root element, e.g., <data>
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.Element(key)  # Create a child element for each key
        child.text = str(value)  # Set the text content of the child element
        root.append(child)  # Append the child element to the root

    tree = ET.ElementTree(root)  # Create an ElementTree object
    with open(filename, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)
        # Write to file


def deserialize_from_xml(filename):
    tree = ET.parse(filename)  # Parse the XML file into an ElementTree object
    root = tree.getroot()  # Get the root element

    data = {}
    for child in root:
        data[child.tag] = child.text
        # Populate the dictionary with tag and text content

    return data
