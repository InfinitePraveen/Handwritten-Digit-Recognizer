# Model

The baseline model is a dense neural network:
- Flatten 28×28×1 image
- Dense 256 ReLU
- Dropout
- Dense 128 ReLU
- Dropout
- Dense 10 Softmax

This is intentionally simple rather than using a CNN.
