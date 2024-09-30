"""
Run main scrypt.
"""


"""
Application main service
"""

import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
import pandas as pd

from src.inference import load_model, predict


app = Flask(__name__)

MODEL_PATH = os.path.join("models", "model_rf_in_docker.joblib")
MODEL = load_model(MODEL_PATH)


@app.route("/")
def helthcheck():
    return "Heart-desease classification service is running!"


@app.route("/predict", methods=["POST"])
def prediction():
    """
    Function to predict the iris species

    Returns
    -------
    prediction
        The predicted iris species
    """
    try:
        data = request.json
        df = pd.DataFrame(data, index=[0])
        df = df.reset_index(drop=True)
        pred_raw = predict(MODEL, df)
        classes = [0, 1]
        prediction = classes[pred_raw[0]]
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})
