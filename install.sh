
#!/bin/bash

# Install required packages
pip install opencv-python
pip install opencv-contrib-python

# Run the facial recognition script
python /home/accessc/facrec/scripts/facial_recognition.py

# Remove the downloaded face detection model
rm /home/accessc/facrec/models/haarcascade_frontalface_default.xml
