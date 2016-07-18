import os
from time import sleep
from gpiozero import Button

button = Button(17)

print 'Batinator Activated'
button.wait_for_press()
# Full 60 minute capture 90fps 640x480 5 minute chunks
os.system("raspivid -hf -vf -w 640 -h 480 -fps 90 -t 3600000 -sg 300000 -o /home/pi/pinoir/bat%04d.h264")
# 45 minute capture 720p 49fps
#os.system("raspivid -hf -vf -w 1296 -h 730 -fps 49 -t 2705000 -sg 300000 -o /home/pi/pinoir/bat%04d.h264")
# Test 1 minute capture 90fps 640x480 20 second chunks
#os.system("raspivid -hf -vf -w 640 -h 480 -fps 90 -t 60000 -sg 20000 -o /home/pi/pinoir/bat%04d.h264")

print 'Batinator Video Captured'



