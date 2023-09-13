#!/usr/bin/python3

""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     download videos from youtube
"""

from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=wDeH4WEEzc0')\
    .streams.filter(progressive=True, file_extension='mp4').first().download()
