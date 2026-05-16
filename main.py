import time
import motion
import camera
import email_alert

print("Surveillance system starting...")
time.sleep(10)
print("System ready.")

print("Waiting for motion...")

try:
    while True:
        if motion.motion_detected():
            print("Motion detected! Recording...")
            camera.record_clip()
            print("E-mail alert sent!")
            email_alert.alert()
            print("Waiting for motion...")
            time.sleep(5) #Pauza intre filmari daca se detecteaza miscare
        else:
            print("No motion detected.")
        time.sleep(1) #De cate ori se actualizeaza senzorul si da output

except KeyboardInterrupt:
    print("\nSystem stopped.")
    motion.cleanup()