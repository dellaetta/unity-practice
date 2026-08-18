import cv2
import logging
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load the input image from an image file.
mp_image = mp.Image.create_from_file('./images.jpg')

base_options = python.BaseOptions(
    model_asset_path= '../models/gesture_recognizer.task'
)

# Create a gesture recognizer instance with the image mode:
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
)

with vision.GestureRecognizer.create_from_options(options) as recognizer:
    result = recognizer.recognize(mp_image)

    top_gesture = result.gestures[0][0].category_name
    hand_landmarks = result.hand_landmarks

    print(top_gesture)

"""
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # create camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

while True:

    # get image from webcam
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break

    # display webcam
    cv2.imshow("Display", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()
"""