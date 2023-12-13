# Image Processing

## Task 1: Image Resizing based on Detected Faces

This Python script utilizes OpenCV (cv2) for detecting faces in an image and resizing the image based on the number of detected faces.

### Description

The script takes an input image and performs the following tasks:

- Loads the image using OpenCV.
- Detects faces in the image using a Haar Cascade classifier for frontal face detection.
- Based on the number of detected faces:
  - If exactly one face is detected, it enlarges the area around the face by three times its original size.
  - If no face or multiple faces are detected, it resizes the entire image to 400x400 pixels.
- Displays the result of the processing.

### Usage

To use the script, follow these steps:

- Install OpenCV in your Python environment if you haven't already:
  - pip install opencv-python
- Replace the `image_path` variable in the script with the path to your desired image.
- Run the script using a Python interpreter.

### Requirements

- Python 3.x
- OpenCV (cv2)

## Task 2: Resize The Image To Multiple Sizes

This Python script utilizes the Pillow library (Image module) to resize an image to multiple sizes and save the resized images to a specified output folder.

### Description

The script performs the following tasks:

- Opens an input image using Pillow's `Image.open()` method.
- Resizes the image to different sizes specified in the `sizes` list.
- Saves the resized images to a specified output folder.
- Displays the resized images for visualization.

### Usage

To use the script, follow these steps:

- Install the Pillow library in your Python environment if you haven't already:
  - pip install pillow
- Replace the `input_image_path` variable in the script with the path to your desired input image.
- Adjust the `sizes` list to specify the different sizes to which you want to resize the image.
- Replace the `output_folder` variable in the script with the path to the folder where you want to save the resized images.
- Run the script using a Python interpreter.

### Requirements

- Python 3.x
- Pillow library (Image module)
