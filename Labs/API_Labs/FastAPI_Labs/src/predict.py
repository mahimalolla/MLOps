import joblib

MODEL_PATH = "../model/iris_model.pkl"

def _load_model():
    return joblib.load(MODEL_PATH)

def predict_data(X):
    model = _load_model()
    return model.predict(X)

def predict_proba_data(X):
    model = _load_model()
    if not hasattr(model, "predict_proba"):
        raise ValueError("Model does not support probability predictions.")
    return model.predict_proba(X)
