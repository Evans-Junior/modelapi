import subprocess
from config.settings import MEDITRON_MODEL_NAME, HEALTH_ASSISTANT_ROLE

def run_meditron_health_assistant(sensor_data=None, symptoms=None, question=None):
    prompt = HEALTH_ASSISTANT_ROLE

    if sensor_data:
        input_data = f"Sensor data: {sensor_data}. Please analyze and provide health advice."
    elif symptoms:
        input_data = f"Symptoms: {symptoms}. Please provide possible causes and suggestions."
    elif question:
        input_data = f"Question: {question}. Please provide a detailed response."
    else:
        input_data = "No sensor data or symptoms provided. Please describe the patient's condition for advice."

    full_prompt = prompt + "\n" + input_data

    try:
        command = f"echo '{full_prompt}' | ollama run {MEDITRON_MODEL_NAME}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running Meditron model: {e.stderr}"
