import os
from time import sleep
from gpiozero import Button

button = Button(17)

print 'BatCam Activated'
button.wait_for_press()
# Full 40 minute capture 90fps 640x480 5 minute chunks
os.system("raspivid -hf -vf -w 640 -h 480 -fps 90 -t 3600000 -sg 300000 -o /home/pi/pinoir/bat%04d.h264")
# 45 minute capture 720p 49fps
#os.system("raspivid -hf -vf -w 1296 -h 730 -fps 49 -t 2705000 -sg 300000 -o /home/pi/pinoir/bat%04d.h264")
# Test 1 minute capture 90fps 640x480 20 second chunks
#os.system("raspivid -hf -vf -w 640 -h 480 -fps 90 -t 60000 -sg 20000 -o /home/pi/pinoir/bat%04d.h264")

print 'BatCam Video Captured'

time.sleep(10)

print 'Converting video 01. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0001.h264  /home/pi/pinoir/bat0001.mp4")
print 'Converting video 02. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0002.h264  /home/pi/pinoir/bat0002.mp4")
print 'Converting video  03. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0003.h264  /home/pi/pinoir/bat0003.mp4")
print 'Converting video 04. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0004.h264  /home/pi/pinoir/bat0004.mp4")
print 'Converting video 05. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0005.h264  /home/pi/pinoir/bat0005.mp4")
print 'Converting video 06. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0006.h264  /home/pi/pinoir/bat0006.mp4")
print 'Converting video 07. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0007.h264  /home/pi/pinoir/bat0007.mp4")
print 'Converting video  08. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0008.h264  /home/pi/pinoir/bat0008.mp4")
print 'Converting video 09. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0009.h264  /home/pi/pinoir/bat0009.mp4")
print 'Converting video 10. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0010.h264  /home/pi/pinoir/bat0010.mp4")
print 'Converting video 11. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0011.h264  /home/pi/pinoir/bat0011.mp4")
print 'Converting video 12. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0012.h264  /home/pi/pinoir/bat0012.mp4")
print 'Converting video  13. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0013.h264  /home/pi/pinoir/bat0013.mp4")
print 'Converting video 14. Please wait...'
os.system("MP4Box -add /home/pi/pinoir/bat0014.h264  /home/pi/pinoir/bat0014.mp4")

print 'Video conversion complete'
time.sleep(2)
 
print 'Check out those mp4s'
time.sleep(2)



