from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "mnist_digit_model.keras"
IMAGE_SIZE = (28, 28)
NUM_CLASSES = 10
