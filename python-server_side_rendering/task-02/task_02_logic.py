#!/usr/bin/python3
"""creating a dynamic template with loops and condition
in Flask using jinja's templating"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get('items', [])

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
