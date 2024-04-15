import cv2, mss, pyautogui
import numpy as np

def main():
    # Set screen capture properties
    monitor_number = 1  # Change this to the monitor you want to capture (0, 1, 2, ...)
    monitor = get_monitor(monitor_number)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('recorded_video.mp4', fourcc, 30, (monitor['width'], monitor['height']))

    if not out.isOpened():
        print("Error: Failed to open VideoWriter.")
        return

    with mss.mss() as sct:
        while True:
            # Capture frame-by-frame
            processed_frame = np.array(sct.grab(monitor))

            # Perform real-time analysis on the frame (placeholder example)
            #processed_frame = process_frame(frame)

            # Write the processed frame to the video file
            out.write(processed_frame)

            # Display the processed frame
            cv2.imshow('Processed Frame', processed_frame)

            # Check for 'q' key to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release VideoWriter object and close OpenCV windows
    out.release()
    cv2.destroyAllWindows()

def get_monitor(monitor_number):
    with mss.mss() as sct:
        monitors = sct.monitors
        if monitor_number < len(monitors):
            return monitors[monitor_number]
        else:
            print("Error: Monitor number out of range.")
            exit()

def process_frame(frame):
    # Placeholder example: Convert frame to grayscale
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return processed_frame

if __name__ == "__main__":
    main()

