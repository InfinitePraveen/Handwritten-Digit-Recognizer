# Contributing to Handwritten Digit Recognizer

Thank you for your interest in contributing to **Handwritten Digit Recognizer**! Contributions, improvements, bug reports, documentation updates, and new ideas are welcome.

## Project Overview

This project uses a Keras/TensorFlow neural network to recognize handwritten digits from the MNIST dataset. It also includes a Flask web application that allows users to draw or upload a digit and receive a prediction.

## Getting Started

### 1. Fork the Repository

Fork the repository on GitHub and clone your fork:

```bash
git clone https://github.com/InfinitePraveen/Handwritten-Digit-Recognizer.git
cd Handwritten-Digit-Recognizer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset

Download the MNIST CSV dataset from Kaggle and place:

```text
mnist_train.csv
mnist_test.csv
```

inside:

```text
data/raw/
```

The project README contains the dataset source and download instructions.

## Development Workflow

Run the notebooks in this order:

```text
01_data_loading.ipynb
02_eda.ipynb
03_preprocessing.ipynb
04_model_training.ipynb
05_evaluation.ipynb
```

The trained model should be saved as:

```text
models/mnist_digit_model.keras
```

## Running the Web Application

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The application allows users to draw a digit or upload an image for prediction.

## Running Tests

Run the complete test suite with:

```bash
pytest -q
```

Before submitting a contribution, make sure existing tests pass.

## Code Style

Please follow these guidelines:

* Use clear and descriptive variable names.
* Keep functions focused on a single responsibility.
* Add comments where logic may not be immediately obvious.
* Follow standard Python conventions.
* Avoid unnecessary dependencies.
* Keep notebooks simple and readable.
* Do not commit unnecessary generated files.
* Do not commit API keys, passwords, or private credentials.

## Adding or Modifying Notebooks

When modifying a notebook:

1. Keep the notebook focused on its specific task.
2. Explain important steps with Markdown cells.
3. Avoid unnecessarily complicated code.
4. Use reproducible random seeds where appropriate.
5. Keep visualizations clear.
6. Verify that the notebook executes successfully from start to finish.

## Machine Learning Contributions

For changes to the model:

* Clearly document the change.
* Explain why the change improves the project.
* Compare the new model with the existing baseline.
* Report relevant evaluation metrics.
* Check that the web application remains compatible with the saved model.

Examples of useful contributions include:

* Improved preprocessing
* Better model architectures
* Improved validation strategy
* Additional evaluation metrics
* Error analysis
* Improved image preprocessing
* CNN-based experimentation

## Web Application Contributions

For changes to the Flask application:

* Keep frontend and backend code organized.
* Test both drawing and image-upload prediction.
* Make sure the `/health` endpoint continues to work.
* Handle invalid uploads gracefully.
* Maintain responsive behavior on different screen sizes.

## Commit Messages

Use concise and descriptive commit messages.

Recommended format:

```text
type: short description
```

Examples:

```text
feat: add CNN digit recognition model
fix: handle invalid image uploads
docs: improve model documentation
test: add predictor tests
style: improve responsive layout
refactor: simplify image preprocessing
chore: update project dependencies
```

## Pull Requests

Before opening a pull request:

* Ensure the project runs correctly.
* Run the test suite.
* Check modified notebooks.
* Update documentation when necessary.
* Explain what changed and why.
* Keep pull requests focused on a specific improvement.

A good pull request should include:

### Description

Briefly describe the changes.

### Motivation

Explain the problem or improvement addressed.

### Testing

Mention the tests or notebooks used to verify the changes.

### Screenshots

For UI changes, include screenshots when useful.

## Reporting Issues

When reporting a bug, include:

* Operating system
* Python version
* TensorFlow/Keras version
* Steps to reproduce the issue
* Expected behavior
* Actual behavior
* Relevant error messages

For web application issues, also mention whether the problem occurs with drawing, image upload, or both.

## Dataset and Model Files

The project uses the MNIST dataset from Kaggle.

Large generated files should only be committed when they are intentionally required by the project. Avoid committing temporary datasets, notebook checkpoints, caches, or unrelated model artifacts.

## Code of Conduct

Please be respectful and constructive when communicating with other contributors. Contributions should focus on improving the project and helping other learners understand the workflow.

## License

By contributing to this project, you agree that your contributions will be distributed under the project's **MIT License**.

## Author

**Praveen Kumar**

GitHub: https://github.com/InfinitePraveen

LinkedIn: https://www.linkedin.com/in/infinitepraveen/

Thank you for contributing! 🚀
