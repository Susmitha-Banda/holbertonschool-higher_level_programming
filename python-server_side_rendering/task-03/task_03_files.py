#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    """ renders a HTML template """
    return render_template('index.html')


@app.route('/items')
def items():
    """ renders a HTML template """
    items_list = []

    with open("./data/items.json", 'r') as f:
        rows = json.load(f)
    for key, value in rows.items():
        # print(key)
        # print(value)
        items_list = value

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """ renders a HTML template """
    # get the value and the id of the 'source' parameter from the URL
    source = request.args.get('source')
    id = request.args.get('id')

    # depending on source parameter read and
    # parse data from the correspdoning file
    data = []
    if source == "json":
        data = load_json_data("data/products.json", id)
    elif source == "csv":
        data = load_csv_data("data/products.csv", id)

    return render_template('product_display.html',
                        data=data, source=source, id=id)


# function to load json data
def load_json_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)
        for row in rows:
            key = row['id']

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                product = {}
                for k,v in row.items():
                    product[k] = v
                data.append(product)

    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data


# function to load csv data
def load_csv_data(filename, wanted_id = None):
    """ Load CSV data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as csvfile:
            # using DictReader method to convert each row to a dictionary
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
