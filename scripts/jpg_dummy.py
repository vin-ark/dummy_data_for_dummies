from PIL import Image
import random

# Define image size
width = random.randint(200, 400)
height = random.randint(200, 400)

# Create a new image
img = Image.new("RGB", (width, height), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

# Generate random pixel values
pixels = img.load()
for i in range(img.width):
    for j in range(img.height):
        pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Save the image
img.save("dummy_image.jpg")
