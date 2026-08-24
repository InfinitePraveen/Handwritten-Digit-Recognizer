# Changelog

All notable changes to the **Handwritten Digit Recognizer** project are documented in this file.

The project follows a simple changelog format based on the principles of semantic versioning.

---

## [1.0.0] - 2026-08-24

### Added

#### Data Science Pipeline

* Added MNIST handwritten digit recognition project.
* Added Kaggle MNIST CSV dataset integration.
* Added training dataset support through `mnist_train.csv`.
* Added test dataset support through `mnist_test.csv`.
* Added data loading utilities.
* Added pixel normalization.
* Added 28×28 image reshaping and preprocessing.
* Added training and validation data splitting.

#### Exploratory Data Analysis

* Added MNIST class distribution analysis.
* Added handwritten digit visualization.
* Added sample image inspection.
* Added notebook-based exploratory workflow.

#### Machine Learning

* Added Keras/TensorFlow neural network.
* Added 256-neuron hidden layer.
* Added 128-neuron hidden layer.
* Added ReLU activation functions.
* Added Dropout regularization.
* Added Softmax output layer for 10 digit classes.
* Added Adam optimizer.
* Added sparse categorical cross-entropy loss.
* Added early stopping during training.
* Added trained model:
  `models/mnist_digit_model.keras`

#### Evaluation

* Added model accuracy evaluation.
* Added classification report.
* Added confusion matrix.
* Added sample prediction visualization.
* Added prediction confidence analysis.

#### Web Application

* Added Flask web application.
* Added browser-based digit drawing canvas.
* Added image upload functionality.
* Added automatic image preprocessing.
* Added digit prediction API.
* Added prediction confidence display.
* Added probability visualization for digits 0–9.
* Added `/health` endpoint.
* Added responsive frontend styling.
* Added GitHub profile link.
* Added LinkedIn profile link.

#### Notebooks

* Added `01_data_loading.ipynb`.
* Added `02_eda.ipynb`.
* Added `03_preprocessing.ipynb`.
* Added `04_model_training.ipynb`.
* Added `05_evaluation.ipynb`.

#### Testing

* Added preprocessing tests.
* Added data loader tests.
* Added configuration tests.
* Added Flask application tests.
* Added utility function tests.

#### Documentation

* Added comprehensive `README.md`.
* Added setup documentation.
* Added notebook workflow documentation.
* Added web application documentation.
* Added model architecture documentation.
* Added dataset card.
* Added API documentation.
* Added `CONTRIBUTING.md`.
* Added `CHANGELOG.md`.

#### Project Configuration

* Added `.gitignore`.
* Added `.env.example`.
* Added Python dependency configuration.
* Added development dependency configuration.
* Added Makefile.
* Added model configuration.
* Added application configuration.

#### Automation

* Added GitHub Actions workflow.
* Added Linux dataset download script.
* Added Windows dataset download script.
* Added application startup script.

### Dataset

The project uses the **MNIST in CSV** dataset available through Kaggle.

Dataset characteristics:

* Training images: 60,000
* Test images: 10,000
* Image size: 28 × 28 pixels
* Pixel features: 784
* Classes: 10
* Classes: digits `0` through `9`
* Target column: `label`

### Model

The initial model is a fully connected neural network consisting of:

```text
Input: 28 × 28 × 1
        ↓
Flatten
        ↓
Dense: 256 neurons + ReLU
        ↓
Dropout
        ↓
Dense: 128 neurons + ReLU
        ↓
Dropout
        ↓
Dense: 10 neurons + Softmax
```

### Project Structure

The initial release establishes the following major directories:

```text
data/
models/
notebooks/
src/
templates/
static/
tests/
docs/
config/
scripts/
```

---

## [Unreleased]

### Planned

Potential future improvements include:

* CNN-based MNIST classifier.
* Improved image preprocessing for user-drawn digits.
* Data augmentation.
* More detailed model comparison.
* Better error analysis.
* Additional web application features.
* Prediction history.
* Improved mobile interface.
* Model performance benchmarking.
* Docker support.
* Production deployment configuration.

---

## Versioning

### 1.0.0

This is the initial stable project release containing the complete Data Science workflow, trained model, testing infrastructure, documentation, and Flask web application.

---

## Author

**Praveen Kumar**

GitHub: https://github.com/InfinitePraveen

LinkedIn: https://www.linkedin.com/in/infinitepraveen/
