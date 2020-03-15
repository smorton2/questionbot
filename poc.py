#!/usr/bin/env python

# Imports
import csv
import random
import requests
import os

# Find a random row and return a formatted version of it.
csv_read = open('questionbank.csv')
csv_reader = csv.reader(csv_read, delimiter=',')
row = random.choice(list(csv_reader)[1:])

# Use API token for Slack Bot that I created.
URL = os.environ.get('SLACK_TOKEN')

# Message
message = {"text": f'{row[1]}'}
requests.post(url=URL, json=message)

# ToDo: Some logic to make sure each user only sees a given question once.
