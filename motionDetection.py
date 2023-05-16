import cv2
import numpy as np
import psycopg2

# Connect to PostgreSQL DB
conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")
cursor = conn.cursor()

# Fetch RTSP feed URL, detection area, and threshold from the database
cursor.execute("SELECT rtsp_url, detection_area, threshold FROM camera_streams")
camera_streams = cursor.fetchall()

# Motion detection parameters
motion_threshold = 1000  # Adjust this value based on your needs
motion_area_threshold = 1000  # Adjust this value based on your needs

# Process each camera stream
for camera_stream in camera_streams:
    rtsp_url = camera_stream[0]
    detection_area = camera_stream[1]
    threshold = camera_stream[2]

    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Failed to open RTSP stream:", rtsp_url)
        continue

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for motion detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform background subtraction
        # Use appropriate background subtraction method based on your scenario
        # e.g., cv2.createBackgroundSubtractorMOG2(), cv2.createBackgroundSubtractorKNN()
        # background_subtractor = cv2.createBackgroundSubtractor...

        # Apply background subtraction to the grayscale frame
        # motion_mask = background_subtractor.apply(gray)

        # Perform motion detection by analyzing the motion mask
        motion_pixels = np.sum(motion_mask // 255)

        if motion_pixels > motion_threshold:
            if motion_pixels > motion_area_threshold:
                # Perform additional checks for motion in a specific area
                # e.g., using contours, bounding boxes, or other techniques
                # If the motion meets the desired conditions, record and send an alert

                # Record and send alert to the client PC
                # Implement your code here to store and send the alert

    cap.release()

# Close the database connection
cursor.close()
conn.close()
