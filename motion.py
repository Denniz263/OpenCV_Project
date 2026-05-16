import RPi.GPIO as GPIO

motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)

def motion_detected():
    return GPIO.input(motionPin) == 1

def cleanup():
    GPIO.cleanup()
    print("GPIO cleaned up")