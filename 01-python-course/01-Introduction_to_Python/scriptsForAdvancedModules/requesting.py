#!/usr/bin/python3

""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     to print date and time from api using restful api
"""

import requests
response = requests.get(
    'http://worldtimeapi.org/api/timezone/Africa/Cairo')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data["datetime"])
