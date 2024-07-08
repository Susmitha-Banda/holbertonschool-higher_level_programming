#!/usr/bin/python3
"""creating a basic flask application"""

from flask import Flask, render_template

# create a flask application instance
app = Flask(__name__)


# define routes and their corresponding view functions
@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')


# run the flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
