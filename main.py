from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
with open("pipeline_model.pkl", "rb") as f:
    pipeline = pickle.load(f)


# Request Body Model
class PredictionInput(BaseModel):
    Gender: int
    Age: float
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float


@app.get("/")
def home():
    return {"message": "Calories Prediction API Running"}


@app.post("/predict")
def predict(data: PredictionInput):

    sample = pd.DataFrame({
        "Gender": [data.Gender],
        "Age": [data.Age],
        "Height": [data.Height],
        "Weight": [data.Weight],
        "Duration": [data.Duration],
        "Heart_Rate": [data.Heart_Rate],
        "Body_Temp": [data.Body_Temp]
    })

    result = pipeline.predict(sample)[0]

    return {
        "predicted_calories": float(result)
    }