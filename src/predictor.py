from pathlib import Path
import numpy as np

class DigitPredictor:
    def __init__(self, model_path):
        self.model_path = Path(model_path)
        self.model = None
        self.is_loaded = False
        self._load()

    def _load(self):
        if not self.model_path.exists():
            return
        from tensorflow import keras
        self.model = keras.models.load_model(self.model_path)
        self.is_loaded = True

    def predict(self, image_array):
        if not self.is_loaded:
            raise FileNotFoundError(
                f"Model not found. Train the model first and save it to {self.model_path}"
            )
        probabilities = self.model.predict(image_array, verbose=0)[0]
        digit = int(np.argmax(probabilities))
        confidence = float(probabilities[digit])
        return {
            "digit": digit,
            "confidence": confidence,
            "probabilities": [float(x) for x in probabilities],
        }
