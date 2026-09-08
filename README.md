# Sign It

Sign It is a gesture-controlled game inspired by Bob It, combining Python, computer vision, and Unity.

The project uses Python for real-time hand gesture recognition and Unity for game logic, visuals, and gameplay. Hand gestures detected from a live camera feed are transmitted from Python to Unity using a UDP socket. 

# How It Works

The project is divided into two main components:
- hand-python: This directory handles real-time hand tracking and gesture recognition.
    - OpenCV is used to capture live video from a camera.
    - MediaPipe is used to detect and classify hand gestures.
    - Recognized gestures are sent to Unity through a UDP socket.
- hand-unity: This directory contains the Unity game and gameplay logic
    - Receives gesture data from Python
    - Displays the required gesture and manages the game timer.
    - Determines whether the player's gesture matches the expected input. Reduced false positives by requiring the gesture to be confirmed 50 times before defining it as a match.

# Architecture
Camera --> OpenCV --> MediaPipe --> Gesture Recognition (Python) -UDP- > Unity Game 

## How to play
1. Start the game.
2. A target hand gesture is displayed on the left side of the screen.
3. Perform the corresponding gesture in front of the camera. The hand on the right displays the last detected hand signal.
4. Match as many gestures as possible before the timer runs out.

## How to run
### 1. Start the Python Gesture Recognition
Navigate to the Python source directory:
`cd hand-python/src`
Run the gesture recognition script:
`python3 hand-python.py`
This starts the camera feed that begins detecting hand gestures.

### 2. Start the Unity Game
While hand-python.py is running, open the hand-unity project in Unity and start the game.

The Python application will send recognized gestures to the Unity game over UDP.

## Technologies
- Python
- OpenCV: Real-time camera capture and image processing 
- MediaPipe: Hand tracking and gesture recognition
- Unity / C#: Game development and gameplay logic
- UDP Sockets: Communication between Python and Unity

## Project Structure
```
Sign-It/
├── hand-unity/ 
│   ├── Assets/  
│   │   └── Scripts 
│   │       ├── GameManager.cs
│   │       ├── GuideScript.cs
│   │       ├── MenuManager.cs
│   │       ├── PlayerScript.cs
│   │       ├── TimerScript.cs
│   │       └── UdpRecieverScript.cs
│   ├── Packages/ 
│   └── ProjectSettings/
│  
├── hand-python/ 
│   ├── model/     
│   │   └── gesture_recognizer.task
│   └── src
│       ├── hand-python.py
│       └── test/
│           ├── images.jpg
│           ├── server.py
│           └── still-image.py
│  
├── .gitignore                   
└── README.md           
```
