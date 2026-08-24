@echo off
if not exist data\raw mkdir data\raw
kaggle datasets download -d oddrationale/mnist-in-csv -p data\raw --unzip
