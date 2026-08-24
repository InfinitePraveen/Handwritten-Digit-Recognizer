#!/usr/bin/env bash
set -e
mkdir -p data/raw
kaggle datasets download -d oddrationale/mnist-in-csv -p data/raw --unzip
