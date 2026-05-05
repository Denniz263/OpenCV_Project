from gpiozero import MotionSensor

pir = MotionSensor(12)

def motion_detected():
    return pir.motion_detected