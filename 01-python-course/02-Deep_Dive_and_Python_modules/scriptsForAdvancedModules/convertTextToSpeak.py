#!/usr/bin/python3

""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     to convert text to speech 
"""

from gtts import gTTS
import vlc

myobj = gTTS(text='صباح الفل يا كبير', lang='ar', slow=True)

myobj.save("welcome.mp4")

p = vlc.MediaPlayer("./welcome.mp4")
p.play()

while True:
    pass
