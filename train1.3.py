import cv2
import os
import numpy as np

# Define the directory containing the training images
train_dir = 'training_images/'

# Define the size of the images used for training (in pixels)
img_size = (100, 100)

# Define the path to the classifier XML file
classifier_path = './haarcascade_frontalface_default.xml'

# Define the name of the output file for the trained recognizer
output_path = './recognizer.yml'

# Create the face detection classifier
face_cascade = cv2.CascadeClassifier(classifier_path)

# Initialize the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Initialize a list to hold the training images
training_images = []

# Initialize a list to hold the corresponding labels for each training image
labels = []

# Loop through the training directory and load each image
for subdir, dirs, files in os.walk(train_dir):
    for file in files:
        # Load the image and convert it to grayscale
        img = cv2.imread(os.path.join(subdir, file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the face in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Loop through the detected faces and add them to the training images list with the appropriate label
        for (x, y, w, h) in faces:
            face_img = cv2.resize(gray[y:y+h, x:x+w], img_size)
            label = subdir.split('/')[-1]
            if label.isdigit():
                training_images.append(face_img)
                labels.append(int(label))

# Train the recognizer using the training images and labels
recognizer.train(training_images, np.array(labels))

# Save the trained recognizer to a file
recognizer.save(output_path)
