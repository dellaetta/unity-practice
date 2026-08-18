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