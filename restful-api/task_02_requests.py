#!/bin.usr/python3
"""Utilize the requests library to send HTTP requests and process responses."""

import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        for data in response.json():
            print(data['title'])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        # Parse JSON response into a list of dictionaries using
        # list comprehension
        posts = [{'id': data['id'], 'title': data['title'],
                  'body': data['body']} for data in response.json()]

    # Specify fieldnames for the CSV header
    fieldnames = ['id', 'title', 'body']
    # Open CSV file in write mode
    with open("posts.csv", 'w', newline='', encoding='utf-8') as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write each post as a row in the CSV file
        for post in posts:
            writer.writerow(post)
