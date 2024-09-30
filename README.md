# Heart-Disease-Classification

FasAPI classification problem.

## Version

1.2.5


## Quick start

1. `git clone https://github.com/aleksandryessin/FastAPI-app-Heart-Disease-Classification.git`
2. Run locally the notebook to explore the dataset and baseline model classification:
    - run **notebook** to see the results and then follow the next steps:

    ```bash
    export PYTHONPATH=$(pwd)
    ```
    ```bash
    export FLASK_APP=main.py
    ```
    ```bash
    source .bashrc
    ```
    ```bash
    pytest (or with report: pytest --cov=src --cov-report=html)
    ```
    ```bash
    flask run
    ```
3. 🔥 Run it with `docker-compose`:

    ```bash
    docker-compose up --build -d
    ```
    or

    ```bash
    docker-compose build --no-cache && docker-compose up -d
    ```

## Data example (for testing it in e.g. Postman)

This data input should return **1st class** of the prediction:

```
data_example = {
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
```

You can observe the **Postman** results example in **images**.
