import uvicorn
import time
import logging
from fastapi import FastAPI
from models.meditron_model import run_meditron_health_assistant  # Import your model function

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Health Assistant API is running!"}

@app.post("/predict/")
async def get_health_advice(sensor_data: dict = None, symptoms: str = None, question: str = None):
    """
    API endpoint to get health advice from the Meditron model.
    - Accepts sensor data, symptoms, or a question.
    - Returns model-generated health advice.
    """
    logging.info("Received request, processing...")

    # Indicate the model is "thinking"
    start_time = time.time()
    response_message = "Processing request... Please wait."

    # Call the Meditron model
    health_advice = run_meditron_health_assistant(sensor_data, symptoms, question)
    
    end_time = time.time()
    processing_time = round(end_time - start_time, 2)

    logging.info(f"Model finished processing in {processing_time} seconds.")

    return {
        "status": "success",
        "processing_time": f"{processing_time} seconds",
        "response": health_advice
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
