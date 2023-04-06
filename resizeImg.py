import cv2

# load image
img = cv2.imread('/home/accessc/training_images')

# check if image was successfully loaded
if img is not None:
    # resize image
    resized_img = cv2.resize(img, (100, 100))
else:
    print("Error: Image not found or could not be loaded.")
