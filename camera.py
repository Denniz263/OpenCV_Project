import cv2
import datetime
import os
import time

def record_clip(duration=10, output_dir="recordings"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Camera not found!")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/clip_{timestamp}.mp4"

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

    start = time.time()
    print(f"Recording for {duration} seconds...")
    while time.time() - start < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

    cap.release()
    out.release()
    print(f"Saved: {filename}")