import pandas as pd
from src.data_loader import split_features_target

def test_split_features_target():
    df = pd.DataFrame({"label":[0,1], "pixel1":[5,6]})
    X, y = split_features_target(df)
    assert list(X.columns) == ["pixel1"]
    assert y.tolist() == [0,1]
