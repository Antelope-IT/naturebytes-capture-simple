from gpiozero import MotionSensor
from signal import pause
from picamera import PiCamera
from datetime import datetime
from signal import pause

# The PIR sensor lead is connected to GPIO27 = Board 13
sensor_pin = 27


# This set the MotionSensor with default settings with pull down as per original code
pir = MotionSensor(sensor_pin)
camera = PiCamera()

def capture():
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S-%f")
    camera.capture('/images/img-%s.png' %timestamp)

pir.when_motion = capture

pause()
