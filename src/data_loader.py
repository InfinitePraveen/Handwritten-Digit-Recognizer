from pathlib import Path
import pandas as pd

def load_mnist_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")
    return pd.read_csv(path)

def split_features_target(df, target="label"):
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
