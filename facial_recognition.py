#!/usr/bin/env python

import os
import cv2
import urllib.request

# Define the URL for the face detection model
model_url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'

# Define the name of the face detection model file
model_file = 'haarcascade_frontalface_default.xml'

# Define the installation directory for the face detection model file
model_dir = os.path.join(os.getcwd(), 'models')

# Define the installation directory for the script
script_dir = os.path.join(os.getcwd(), 'scripts')

# Create the directories if they don't exist
os.makedirs(model_dir, exist_ok=True)
os.makedirs(script_dir, exist_ok=True)

# Download the face detection model file
urllib.request.urlretrieve(model_url, os.path.join(model_dir, model_file))

# Create the facial recognition script
script = f"""
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('{os.path.join(model_dir, model_file)}')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Create a loop to read frames from the camera and detect faces
while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a circle around each detected face
    for (x, y, w, h) in faces:
        cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+h)/4), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Facial Recognition', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
"""

# Save the script to a file
with open(os.path.join(script_dir, 'facial_recognition.py'), 'w') as f:
    f.write(script)

# Make the script executable
os.chmod(os.path.join(script_dir, 'facial_recognition.py'), 0o755)

# Create the installer script
script = f"""
#!/bin/bash

# Install required packages
pip install opencv-python
pip install opencv-contrib-python

# Run the facial recognition script
python {os.path.join(script_dir, 'facial_recognition.py')}

# Remove the downloaded face detection model
rm {os.path.join(model_dir, model_file)}
"""

# Save the installer script to a file
with open('install.sh', 'w') as f:
    f.write(script)

# Make the installer script executable
os.chmod('install.sh', 0o755)

# Run the installer script
os.system('./install.sh')
