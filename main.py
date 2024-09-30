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
    return "Heart-desease prediction service is running!"

# {
#             "age": [56.0],
#             "sex": [1.0],
#             "cp": [1.0],
#             "trestbps": [130],
#             "chol": [240],
#             "fbs": [0.0],
#             "restecg": [1.0],
#             "thalach": [152],
#             "exang": [0.0],
#             "oldpeak": [0.8],
#             "slope": [1.0],
#             "ca": [0.0],
#             "thal": [2.0]
# }
# should return 1


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


def main():
    print("Main scrypt is running.")

if __name__ == '__main__':
    main()
