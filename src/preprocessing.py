import numpy as np
from PIL import Image, ImageOps

def normalize_pixels(X):
    return np.asarray(X, dtype="float32") / 255.0

def reshape_images(X):
    arr = np.asarray(X)
    return arr.reshape(-1, 28, 28, 1)

def prepare_image(image):
    image = image.convert("L")
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    arr = np.asarray(image, dtype="float32") / 255.0
    return arr.reshape(1, 28, 28, 1)
