The Batinator

Code from the Batinator project, a portable slow motion night vision Raspberry Pi bat camera.

The Batinator is a portable Raspberry Pi that uses a PinoIR (No Infrared Filter) camera module to record video in the dark at 90 frames per second, 640x480 resolution. It features a 48 LED illuminator lamp on top and the power is provided by a 12v rechargeable drill battery.

Full details of the Batinator build are at XXXXXXXXX

The YouTube video is at XXXXXXXXXXXXXXX

Batinator.py

This file waits for a button connected to GPIO17 to be pressed and then begins recording, saving the captured h.264 video files in 5 minute chunks. Huge thanks to the Average Man for sharing the original code and tutorial (http://www.averagemanvsraspberrypi.com/2015/07/raspberry-pi-camera-module-slow-motion-video.html) - all I changed was the chunking - an hour captured takes 3 hours to play back so I was happier with lots of short files!

I've left a couple of my "go-to" capture settings commented out in the script, so you can see where to change the resolution and frame rate if you want to experiment, more info on working combinations is at https://www.raspberrypi.org/blog/new-camera-mode-released/

I did also amend /etc/rc.local to make this script run on startup, I just added in the line...

python /home/pi/pinoir/Batinator.py &

...on a new line above the exit() at the end of the script.

Convert.py

This file converts the captured h.264 video files into .mp4 format, making them easier to view and edit. I found VLC player good for viewing and had no problems editing with Windows Movie Maker.

The code in Convert.py could easily be held in the same script as Batinator.py, it just works best for me to keep them separate. I usually try to take the Pi off battery power as soon as it's finished recording, then plug in the mains to do the converting and viewing. Convert.py could do with a loop as well!

Check out my other Raspberry Pi and Upcycled Retro Technology projects at