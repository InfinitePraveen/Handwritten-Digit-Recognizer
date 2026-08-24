from pathlib import Path
import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from PIL import Image
from src.preprocessing import prepare_image
from src.predictor import DigitPredictor

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.getenv("MODEL_PATH", str(BASE_DIR / "models" / "mnist_digit_model.keras"))

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_UPLOAD_MB", "5")) * 1024 * 1024

predictor = DigitPredictor(MODEL_PATH)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": predictor.is_loaded})

@app.post("/predict")
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image was uploaded."}), 400
    file = request.files["image"]
    if not file.filename:
        return jsonify({"error": "Please select an image."}), 400

    try:
        image = Image.open(file.stream)
        pixels = prepare_image(image)
        result = predictor.predict(pixels)
        return jsonify(result)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG", "0") == "1")
