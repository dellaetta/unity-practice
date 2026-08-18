import cv2
import logging
import time
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

latest_frame = None
 
#################### Functions ############################
def draw_results(result, output_image: mp.Image, timestamp_ms: int):
    global latest_frame
    frame = output_image.numpy_view().copy() # convert numpy into cv frame
    height, width, _ = frame.shape
    
    # draw each detected hand
    for hand_landmarks in result.hand_landmarks:
    
        # convert normalized coordinates to pixels
        points = []

        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

            # draw landmark
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        # MediaPipe hand landmark connections
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),
            (0, 5), (5, 6), (6, 7), (7, 8),
            (0, 9), (9, 10), (10, 11), (11, 12),
            (0, 13), (13, 14), (14, 15), (15, 16),
            (0, 17), (17, 18), (18, 19), (19, 20),
            (5, 9), (9, 13), (13, 17)
        ]

        # draw connections
        for start, end in connections:
            cv2.line(frame, points[start], points[end], (255, 0, 0), 2)
    

    if result.gestures :
        top_gesture = result.gestures[0][0] # get top gesture 

        gesture_name = top_gesture.category_name
        confidence = top_gesture.score

        if gesture_name != "None":
            text = f"{gesture_name} ({confidence:.2f})"
            cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    latest_frame = frame
     

#################### Camera Setup ############################
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # create camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
 
#################### Gesture Recognizer ############################

# get model
base_options = python.BaseOptions(
    model_asset_path= '../models/gesture_recognizer.task'
)

# create a gesture recognizer instance with the live stream mode
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    result_callback=draw_results
)

with vision.GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        # get image from webcam
        ret, frame = cam.read()
        if not ret:
            logging.error("Live image not captured")
            break

        frame = cv2.flip(frame, 1)
        
        # convert to mp formatting
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

        # recognize the hand gesture in the frame
        frame_timestamp_ms = int(time.time() * 1000)
        recognizer.recognize_async(mp_image, frame_timestamp_ms)

        if latest_frame is None:
            latest_frame = frame

        cv2.imshow("Display", latest_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()