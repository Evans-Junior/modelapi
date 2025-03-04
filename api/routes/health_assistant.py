from fastapi import APIRouter
from models.meditron_model import run_meditron_health_assistant

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to the Health Assistant API"}

@router.post("/get_advice/")
def get_health_advice(sensor_data: dict = None, symptoms: str = None, question: str = None):
    response = run_meditron_health_assistant(sensor_data, symptoms, question)
    return {"health_advice": response}
