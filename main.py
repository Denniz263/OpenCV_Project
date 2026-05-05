import time
import motion
import camera
import email_alert

print("Surveillance system starting...")
print("Waiting for motion...")

try:
    while True:
        if motion.motion_detected():
            print("Motion detected! Recording...")
            camera.record_clip(duration=10)
            print("E-mail alert sent!")
            email_alert.alert()
            print("Waiting for motion...")
            time.sleep(3)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nSystem stopped.")