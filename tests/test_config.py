from src.config import IMAGE_SIZE, NUM_CLASSES

def test_config():
    assert IMAGE_SIZE == (28, 28)
    assert NUM_CLASSES == 10
