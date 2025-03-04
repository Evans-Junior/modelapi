import os

MEDITRON_MODEL_NAME = os.getenv("MEDITRON_MODEL_NAME", "meditron")
HEALTH_ASSISTANT_ROLE = "You are a medical assistant AI. Provide accurate health advice."
DATASET_PATH = "data/balanced_dataset.csv"
