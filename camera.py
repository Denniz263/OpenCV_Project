import cv2
import datetime
import os

def record_clip(duration = 10, output_dir="recordings"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Camera not found!")
        exit(1)
        return
    
    fps= cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps is None:
        fps = 60.0


    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    filename = f"{output_dir}/clip_{timestamp}.mp4"

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    print(f"Recording for {duration} seconds...")
    
    total_frames = int(duration * fps)
    captured = 0
    
    while captured < total_frames:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            captured += 1
    cap.release()
    out.release()
   
    print(f"Saved: {filename}")