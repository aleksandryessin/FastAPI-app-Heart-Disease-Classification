"""
Module: test_inference.py
Description: This module is used to test the inference module.
"""

import os

from sklearn.base import BaseEstimator
import pandas as pd
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inference import load_model, predict


def test_load_model():
    model_path = os.path.join("models", "model_rf_in_docker.joblib")
    assert isinstance(load_model(model_path), BaseEstimator)


def test_predict():
    model_path = os.path.join("models", "model_rf_in_docker.joblib")
    model = load_model(model_path)
    df = pd.DataFrame(
            {
            "age": [56.0],
            "sex": [1.0],
            "cp": [1.0],
            "trestbps": [130],
            "chol": [240],
            "fbs": [0.0],
            "restecg": [1.0],
            "thalach": [152],
            "exang": [0.0],
            "oldpeak": [0.8],
            "slope": [1.0],
            "ca": [0.0],
            "thal": [2.0]
        }
    )
    assert predict(model, df) == [1]
