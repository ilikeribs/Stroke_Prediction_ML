from pydantic import BaseModel

class Patient(BaseModel):

    gender: str
    age: float
    hypertension: float
    heart_disease: float
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str 
