#!/usr/bin/python3
""" function to replace words in templates """

import sys
import logging
import os


def generate_invitations(template, attendees):
    # chceck if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # check if attendees is a list of dictionaries
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated")
        return

    # check is attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # procecess each attendee
    for i, attendee in enumerate(attendees, start=1):
        # replace placeholders with actual data
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # generate output file name
        output_file = f"output_{i}.txt"

        # write the processed template to the output file
        try:
            with open(output_file, 'w') as file:
                file.write(invitation)
        except IOError as e:
            print(f"Error: Could not write to file {output_file}. {e}")
