import cv2

def resize_image_based_on_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)
    cv2.imshow('face',image)
    # Convert the image to grayscale (for face detection)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize the face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    detected_faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    if len(detected_faces) == 1:
        # If exactly one face is detected
        x, y, w, h = detected_faces[0]  # Get the bounding box of the detected face

        # Extract and resize the area around the detected face (3 times the original size)
        enlarged_face = image[y:y+h, x:x+w]
        enlarged_face = cv2.resize(enlarged_face, None, fx=3, fy=3)

        # Display the enlarged face
        cv2.imshow('Enlarged Face', enlarged_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # If no face or multiple faces are detected, resize the entire image to 400x400
        resized_image = cv2.resize(image, (400, 400))

        # Display the resized image
        cv2.imshow('Resized Image', resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = r'path/to/your/.jpg'
resize_image_based_on_faces(image_path)
