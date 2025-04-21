import torchvision
from torchvision import transforms
from PIL import Image

# Create a custom transform to remove the copyright banner
class RemoveCopyrightBanner(object):
    def __call__(self, img):
        # Get the width and height of the image
        width, height = img.size
        # Crop the image to remove the bottom 20 pixels (the copyright banner)
        return img.crop((0, 0, width, height - 20))
