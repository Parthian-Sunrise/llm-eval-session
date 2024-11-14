from PIL import Image as PILImage
from IPython.display import display


def display_image(image_path, max_size=400):
    img = PILImage.open(image_path)
    img.thumbnail((max_size, max_size))

    # Display the resized image
    display(img)
