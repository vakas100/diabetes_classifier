from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pickle
import uvicorn

app = FastAPI(title='Diabetes Classifier')

model = pickle.load(open('../model.pkl','rb'))
scaler = pickle.load(open('../scaler.pkl','rb'))


class DiabetesInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

@app.get('/')
def home():
    return {
        "message":"Diabetes Classifier is running"
    }

@app.post('/predict')
def predict(data: DiabetesInput):
    input_data = np.array([[
        data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness, data.Insulin,
        data.BMI, data.DiabetesPedigreeFunction, data.Age
        ]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]

    return{
        "prediction": int(prediction),
        "result": "diabetic" if prediction == 1 else "non-diabetic"
    }

if __name__ == "__main__":
    uvicorn.run('main:app',reload=True)


