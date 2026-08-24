# Handwritten Digit Recognizer

A beginner-friendly Data Science project that classifies handwritten digits (0–9) using a neural network built with **Keras/TensorFlow** and the **MNIST** dataset.

## Project Highlights
- Kaggle MNIST data in CSV format
- Simple notebooks covering data loading, EDA, preprocessing, model training, and evaluation
- Keras neural network for 10-class digit classification
- Flask web app with a browser drawing canvas and image upload
- Prediction confidence and probability chart
- Basic tests and configuration files
- GitHub Actions workflow for project checks

## Dataset

This project uses the **MNIST in CSV** dataset published on Kaggle by Dariel Dato-on.

Dataset page:
https://www.kaggle.com/oddrationale/mnist-in-csv

The dataset contains:
- `mnist_train.csv`: 60,000 labeled images
- `mnist_test.csv`: 10,000 labeled images
- Each image is 28 × 28 grayscale pixels
- The first column is `label`; the remaining 784 columns are pixel values from 0–255
- The dataset page lists the license as CC0 / Public Domain.

Source: Kaggle dataset documentation.

## Skills
- Python
- Pandas and NumPy
- Data Cleaning and EDA
- Neural Networks
- Keras / TensorFlow
- Image preprocessing
- Model evaluation
- Flask
- HTML, CSS and JavaScript

## Notebook Workflow
1. `01_data_loading.ipynb` – load the Kaggle CSV files and inspect the dataset
2. `02_eda.ipynb` – explore class distribution and visualize handwritten digits
3. `03_preprocessing.ipynb` – normalize pixels and prepare train/validation data
4. `04_model_training.ipynb` – build and train a Keras neural network
5. `05_evaluation.ipynb` – evaluate accuracy, confusion matrix and sample predictions

## Web App

The Flask application supports:
- Drawing a digit on a canvas
- Uploading a 28×28-compatible digit image
- Automatic grayscale and resize preprocessing
- Keras prediction
- Confidence score
- Class probability visualization

After training, place the saved model at:

`models/mnist_digit_model.keras`

Run:

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Kaggle Download

Using the Kaggle CLI, download the dataset and place the CSV files in `data/raw/`.

Example:

```bash
kaggle datasets download -d oddrationale/mnist-in-csv -p data/raw --unzip
```

## Repository Structure

```text
Handwritten-Digit-Recognizer/
├── app.py
├── requirements.txt
├── notebooks/
├── src/
├── templates/
├── static/
├── tests/
├── docs/
├── config/
├── data/
├── models/
└── scripts/
```

## Author

**Praveen Kumar**

GitHub: https://github.com/InfinitePraveen  
LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## Disclaimer
The dataset is not included in this repository because of its size. Download it directly from Kaggle.
