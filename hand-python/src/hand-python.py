import cv2
import logging
import time
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# create the camera
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # create camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

def print_result(result, output_image: mp.Image, timestamp_ms: int):
    if result.gestures:
        top_gesture = result.gestures[0][0].category_name
        if top_gesture != "None":
            print(top_gesture)
    #print('gesture recognition result: {}'.format(result))
    
# get the model
base_options = python.BaseOptions(
    model_asset_path= '../models/gesture_recognizer.task'
)

# create a gesture recognizer instance with the live stream mode
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    result_callback=print_result
)

with vision.GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        # get image from webcam
            ret, frame = cam.read()
            if not ret:
                logging.error("Live image not captured")
                break
        
            # display webcam
            cv2.imshow("Display", frame)

            # convert to mp formatting
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

            # recognize the hand gesture in the frame
            frame_timestamp_ms = int(time.time() * 1000)
            recognizer.recognize_async(mp_image, frame_timestamp_ms)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cam.release()
cv2.destroyAllWindows()