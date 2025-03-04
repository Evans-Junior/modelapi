import pandas as pd
from models.meditron_model import run_meditron_health_assistant
from config.settings import DATASET_PATH

df = pd.read_csv(DATASET_PATH)

for index, row in df.iterrows():
    sensor_data = row[:-1].to_dict()  
    
    print(f"Processing sample {index}...")
    health_advice = run_meditron_health_assistant(sensor_data=sensor_data)
    print("Health advice:", health_advice)
    
    df.loc[index, 'health_advice'] = health_advice

df.to_csv("data/processed_dataset.csv", index=False)
print("Processing completed. Results saved.")
