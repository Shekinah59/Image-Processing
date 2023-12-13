from PIL import Image
import os


def resize_image(input_image_path, sizes, output_folder):
    with Image.open(input_image_path) as img:
        original_width, original_height = img.size

        resized_images = []

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Resize the image to different sizes and save
        for i, size in enumerate(sizes):
            resized_img = img.resize(size)
            resized_images.append(resized_img)

            # Save the resized image
            output_path = os.path.join(output_folder, f"resized_{i + 1}_{size[0]}x{size[1]}.jpg")
            resized_img.save(output_path)

            # Display the resized image
            resized_img.show(title=f"Resized to {size}")

        # Return the resized images along with the original image
        return resized_images


# Replace 'path/to/your/image.jpg' with the actual path to your image file
input_image_path = r'path/to/your/image.jpg'

# Define sizes for resizing
sizes = [(800, 800), (400, 400), (200, 200), (100, 100)]

# Replace 'path/to/your/' with the actual path to save the resized images
output_folder = r'path/to/your/'

# Call the function to resize and save the images
resized_images = resize_image(input_image_path, sizes, output_folder)
