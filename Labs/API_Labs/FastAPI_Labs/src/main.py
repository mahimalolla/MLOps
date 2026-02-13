from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from predict import predict_data, predict_proba_data

app = FastAPI()

class IrisData(BaseModel):
    petal_length: float
    sepal_length: float
    petal_width: float
    sepal_width: float

class IrisResponse(BaseModel):
    response: int

class IrisProbaResponse(BaseModel):
    predicted_class: int
    probabilities: List[float]
    confidence: float

@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status": "healthy"}

@app.post("/predict", response_model=IrisResponse)
async def predict_iris(iris_features: IrisData):
    try:
        features = [[
            iris_features.sepal_length, iris_features.sepal_width,
            iris_features.petal_length, iris_features.petal_width
        ]]
        prediction = predict_data(features)
        return IrisResponse(response=int(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_proba", response_model=IrisProbaResponse)
async def predict_iris_proba(iris_features: IrisData):
    try:
        features = [[
            iris_features.sepal_length, iris_features.sepal_width,
            iris_features.petal_length, iris_features.petal_width
        ]]
        proba = predict_proba_data(features)[0]   # array of 3 probs
        pred_class = int(proba.argmax())
        confidence = float(proba[pred_class])

        return IrisProbaResponse(
            predicted_class=pred_class,
            probabilities=[float(p) for p in proba],
            confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
