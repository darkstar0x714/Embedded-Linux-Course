#!/usr/bin/python3
"""
   Author        :     Amir W. Fathy
   Date          :     22 sep 2023
   Description   :     program to send email when ever the laptop get opened with device name and mac
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import platform


def get_macAddress():
    return ':'.join(['{:02x}'.format(
        (uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])


def get_laptop_name():
    try:
        system_info = platform.uname()
        return system_info.node
    except Exception as e:
        return str(e)


# follow this instruction at
# https://support.google.com/accounts/answer/185833?visit_id=638310176658822463-1199609109&p=InvalidSecondFactor&rd=1
sender_email = 'xxxxxx@gmail.com'
receiver_email = 'xxxxxx@gmail.com'
password = 'xxxx xxxx xxxx xxxx'.replace(
    " ", "")  # 16 char from google app sign-in
subject = 'your laptop is on'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

body = f'This is an email sent from Python to tell you that your laptop is on laptop name is : {get_laptop_name()} with mac address {get_macAddress()}'
message.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.gmail.com'
port = 587
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)

    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')
finally:
    server.quit()
