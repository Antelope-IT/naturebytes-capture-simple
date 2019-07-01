# NatureBytes-Capture-Simple
This repository contains the source code for the naturebytes-capture-simple Docker container. Its an initial proof of concept for the [NatureBytes wildlife Camera](http://naturebytes.org). I started the project when I had problems running the raspbian image downloaded from the [NatureBytes site](http://naturebytes.org) on my RPi 3+A. At the time the image did not appear to support the RPi3+A. This project is another learning vehicle for me to learn about Docker, Python, Raspberry Pi and things vaguely IoT. 

The Dockerfile builds an image that works with the [NatureBytes wildlife Camera](http://naturebytes.org). 
It takes a photo each time the PIR detects motion and writes the image as a png file to a USB flash drive mounted on the volume /images. It is an extremely simple implementation (hence the name) and therefore has the potiential to fill a flash drive quite quickly; even under the best conditions. 

The image runs a simple python script capture-simple.py which takes a photograph each time the motion sensor detects motion. The script is based on the 'Basic Recipe' for the [MotionSensor](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor)  in the GPIOZERO library and the 'Basic Recipe' for the [Camera](https://picamera.readthedocs.io/en/release-1.13/recipes1.html) in the PICamera library. As with the 'Basic Recipe' code I've used the Pause method from Signal library to keep the container running until it is stopped. As such the functionailty is very simple; it has only a fraction of the functionality of the original Naturebytes solution - no overlays, ability to upload or logging. As such if you are looking for a fully featured solution you would be better using the NatureBytes code.  

Health Warning
==============
Please be aware that this docker image has had little testing and I'm new to Python. I have created this source code by following many "Getting started with..." articles. You are welcome to use this code and to learn from my mistakes, however I make no guarantees as to its functionality or suitability. 

Build
---------
```
docker build \
  --tag=naturebytes-capture-simple \
  .  
  
```

Usage
---------
```
docker run \
  -d \
  --device /dev/gpiomem \
  --device /dev/vchiq \
  --name < your_container_name_here > \
  -v < mount_point_for_storing_images >:/images \
  naturebytes-capture-simple

```
Publish
-------
```
To be Published ...
```

Future
======
This is the most basic implementation, future developments should include the ability to configure the camera for different operating conditions and operating modes; burst, stream, ring buffer. As a remote device it should also be able to report its status and as noted above there is little preventing the app from filling the drive with images until it crashes with a free space error it should therefore be possible to set some configurable limit as to the maximum space available for image storage. Following further testing I expect other desirable feature and functions will be identified.
