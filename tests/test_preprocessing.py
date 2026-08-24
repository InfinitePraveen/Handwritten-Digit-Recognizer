import numpy as np
from PIL import Image
from src.preprocessing import normalize_pixels, reshape_images, prepare_image

def test_normalize_pixels():
    x = np.array([[0, 255]], dtype=np.uint8)
    out = normalize_pixels(x)
    assert out.min() == 0
    assert out.max() == 1

def test_reshape_images():
    x = np.zeros((2, 784))
    assert reshape_images(x).shape == (2, 28, 28, 1)

def test_prepare_image():
    image = Image.new("L", (100, 100), color=255)
    assert prepare_image(image).shape == (1, 28, 28, 1)
