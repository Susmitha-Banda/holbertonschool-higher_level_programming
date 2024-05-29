#!/bin.usr/python3
"""The objective of this exercise is to gain experience in
reading data from one format (CSV) and converting it into
another format (JSON) using serialization techniques."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Takes the CSV filename as its parameter
    and writes the JSON data to data.json."""
    try:
        # open the CSV file
        with open(csv_filename, 'r')as csv_file:
            # read the CSV data
            csv_data = csv.DictReader(csv_file)
            data_list = list(csv_data)

        # define the JSON output file
        json_filename = 'data.json'

        # Write the JSON data to the output file
        with open(json_filename, 'w')as json_file:
            json.dump(data_list, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
