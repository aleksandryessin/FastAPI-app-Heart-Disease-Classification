"""
Main pipeline for the project
"""

import joblib
from loguru import logger
import sys
import os
import pandas as pd

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.train import train_model, evaluate_model
from src.preprocessing import load_data, split_data


def test_main():
    df = load_data()
    train, test = split_data(df)
    assert isinstance(test, pd.DataFrame)
    logger.info("Training model")
    model = train_model(train)
    logger.info("Model accuracy is bigger 0.9:")

    assert evaluate_model(model, test)>=0.9
