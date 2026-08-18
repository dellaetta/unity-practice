import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# get the model
base_options = python.BaseOptions(
    model_asset_path= '../models/gesture_recognizer.task'
)

# create a gesture recognizer instance with the image mode
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
)

with vision.GestureRecognizer.create_from_options(options) as recognizer:

    # get the image
    mp_image = mp.Image.create_from_file('./images.jpg')

    # proccess it through recognizer
    result = recognizer.recognize(mp_image)

    # get the image in cv2
    cv_image = cv2.imread('./images.jpg')
    height, width, _ = cv_image.shape

    # draw each detected hand
    for hand_landmarks in result.hand_landmarks:

        # convert normalized coordinates to pixels
        points = []

        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

            # draw landmark
            cv2.circle(cv_image, (x, y), 5, (0, 255, 0), -1)

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
            cv2.line(cv_image, points[start], points[end], (255, 0, 0), 2)

    # get detected gesture
    if result.gestures:
        top_gesture = result.gestures[0][0]

        gesture_name = top_gesture.category_name
        confidence = top_gesture.score

        text = f"{gesture_name} ({confidence:.2f})"

        cv2.putText(cv_image, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        print(gesture_name)


cv2.imshow("Gesture Recognition", cv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

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