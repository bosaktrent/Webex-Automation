#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sample Python script that creats a new room, adds a user, and sends a message.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
__author__ = "Trent Bosak <tbosak@cisco.com>"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import requests
import pandas as pd

def createRoom(roomName):
    # Creates a new room with the name stored in roomName
    url = "https://api.ciscospark.com/v1/rooms"
    payload = {
        'title': roomName
    }
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': token              # Personal access token
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()["id"]

def addUsers(user_emails, roomId):
    # Adds new users stored in user_emails
    for user_email in user_emails.index:
        url = "https://api.ciscospark.com/v1/memberships"
        payload = {
            'roomId': roomId,
            'personEmail': user_email
            }
        headers = {
            'Authorization': token,         # Personal access token
            'Content-Type': "application/x-www-form-urlencoded",
            }
        requests.request("POST", url, data=payload, headers=headers)

def sendMessage(message, roomId):
    # Sends a message to the new room
    url = "https://api.ciscospark.com/v1/messages"
    payload = {
        'roomId': roomId,
        'text': message
    }
    headers = {
        'Authorization': token,             # Personal access token
        'Content-Type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

def displayDoc():
    # Displays documentation
    indent = 4
    print(
        __doc__,
        "Author:",
        " " * indent + __author__,
        __copyright__,
        "Licensed Under: " + __license__,
        sep="\n"
        )

def main():
    filename = 'email_addresses.xlsx'       # File containing email_addresses
    room_name = "My New Room"               # New room name
    message = "Welcome!"                    # Message to send to new room
    user_emails = pd.read_excel(filename, sheet_name='Sheet1', index_col='Email Address')
    roomId = createRoom(room_name)          # Creates a new room and returns roomId
    addUsers(user_emails, roomId)           # Adds new user to room
    sendMessage(message, roomId)            # Sends message to new room
    displayDoc()

if __name__ == '__main__':
    token = "Bearer {}"                     # Personal access token
    main()
