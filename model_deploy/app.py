import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from patient import Patient
import pandas as pd
import joblib
import json

app = FastAPI()
classifier = joblib.load("stroke_predictor.joblib", 'r')

class PatientJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Patient):
            return obj.model_dump()
        return super().default(obj)

@app.get('/')
def index():
    return {'message': "Welcome to the Stroke Predictor"}

@app.post('/predict', response_class=JSONResponse)
def predict_stroke(payload: Patient):
    try:
        df = pd.DataFrame([payload.model_dump()])
        pred = classifier.predict(df)
        result = {"Stroke risk": pred.tolist()[0]}  
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
