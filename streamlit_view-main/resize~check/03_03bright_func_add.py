# convert jpg to png and size 640x640 filling with padding

from PIL import Image, ImageEnhance
import os

# Define a function to adjust image brightness
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Path to the directory containing your JPG images
jpg_dir = './data/Training/image/TS_B5'

# Path to the directory where you want to save the PNG images
png_dir = './data/Training/image/TS_B5_png_bright'

# Desired size for the PNG images (640x640)
target_size = (640, 640)

# Brightness factor (1.0 -> no change in brightness)
brightness_factor = 1.5  

# Check if the output directory exists, and create it if not
if not os.path.exists(png_dir):
    os.makedirs(png_dir)

# Iterate through the JPG files in the input directory
for jpg_file in os.listdir(jpg_dir):
    if jpg_file.endswith(".jpg"):
        # Open the JPG image
        img = Image.open(os.path.join(jpg_dir, jpg_file))

        # Calculate the resizing dimensions while maintaining aspect ratio
        img.thumbnail(target_size)

        # Create a new blank image with the target size
        new_img = Image.new("RGB", target_size, (0, 0, 0))

        # Calculate the position to center the image
        left = (target_size[0] - img.width) // 2
        top = (target_size[1] - img.height) // 2

        # Paste the resized image onto the blank image
        new_img.paste(img, (left, top))

        # Apply brightness
        new_img = adjust_brightness(new_img, brightness_factor)

        # Create the output PNG file name
        png_file = os.path.splitext(jpg_file)[0] + ".png"

        # Save the PNG image to the output directory
        new_img.save(os.path.join(png_dir, png_file), "PNG")

print("Conversion and resizing with padding completed.")