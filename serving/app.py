from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/student_perf_model.joblib")

@app.get("/")
def home():
    return {
        "message": "Student Performance Prediction API Running"
    }

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "risk_probability": round(float(probability), 2)
    }