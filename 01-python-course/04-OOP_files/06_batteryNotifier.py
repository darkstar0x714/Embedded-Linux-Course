#!/usr/bin/python3
"""
   Author        :     Amir W. Fathy
   Date          :     22 sep 2023
   Description   :     simple program to send notification when battery is low
"""

import psutil
from plyer import notification
import time


while True:
    battery = psutil.sensors_battery()
    percentage = battery.percent if battery else None
    if percentage <= 20:
        title = "Battery is low"

        if percentage is not None:
            message = f"your battery level is {percentage:.0f}"
        else:
            message = f"your battery level is un Reachable"

        notification.notify(
            title=title,
            message=message,
            app_name="06_batteryNotifyer",)
    time.sleep(300)
