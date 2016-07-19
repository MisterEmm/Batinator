# Batinator
Code from the Batinator project, a slow motion night vision Raspberry Pi bat camera.

The Batinator is a portable Raspberry Pi that uses a PinoIR (No Infrared Filter) camera module to record video in the dark at 90 frames per second, 640x480 resolution. It features a 48 LED illuminator lamp on top and the power is provided by a 12v drill battery. 

Full details of the Batinator build are available at http://www.instructables.com/id/The-Raspberry-Pi-Batinator

The YouTube video is at https://www.youtube.com/watch?v=Ota2V3bVvAw

#Batinator.py

This file does the recording, waiting for a button connected to GPIO17 to be pressed. 

Huge thanks to the Average Man for sharing this code initially, all I've added is some code to split the video files into manageable 5 minute chunks. The original code and tutorial are well worth a look at http://www.averagemanvsraspberrypi.com/2015/07/raspberry-pi-camera-module-slow-motion-video.html 

There are a couple of commented out examples in Batonator.py that show how you can change the video resolution and recording time, if you're interested in what's possible the combinations are documented at https://www.raspberrypi.org/blog/new-camera-mode-released/ 

#Convert.py

This file converts the captured h.264 files into the more manageable .mp4 format, the resulting files view really well using VLC Player and can be easily edited with Windows Movie Maker. The code in Convert.py is again really simple and could be incorporated at the end of Batinator.py, it was best for me to keep them separate as I normally disconnect the Pi from battery power as soon as possible after capturing (the battery seems OK up to about 3 hours). 

Check out my other Raspberry Pi and Upcycled Retro Technology projects at http://www.instructables.com/member/MisterM/?show=INSTRUCTABLES
