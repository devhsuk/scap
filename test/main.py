import time, mss, cv2, ffmpeg
import numpy as np

# Screen resolution
SCREEN_WIDTH = 1920  # Update with your screen resolution
SCREEN_HEIGHT = 1080

def main():
    # FFmpeg command for screen capturing
    ffmpeg_cmd = (
        ffmpeg
        .input('desktop', format='gdigrab', s=f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}', framerate=60)
        .output('pipe:', format='rawvideo', pix_fmt='bgr24')
        .run_async(pipe_stdout=True)
    )

    # Initialize screen capture
    with mss.mss() as sct:
        while True:
            # Capture frame from FFmpeg output
            in_bytes = ffmpeg_cmd.stdout.read(SCREEN_WIDTH * SCREEN_HEIGHT * 3)
            if not in_bytes:
                break
            frame = np.frombuffer(in_bytes, np.uint8).reshape((SCREEN_HEIGHT, SCREEN_WIDTH, 3))

            # Process the frame
            processed_frame = frame #process_frame(frame)

            # Display the processed frame
            cv2.imshow('Processed Frame', processed_frame)
            cv2.waitKey(1)

def process_frame(frame):
    # Placeholder example: Convert frame to grayscale
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return processed_frame

if __name__ == "__main__":
    main()

