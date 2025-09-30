import mlflow
import json
import subprocess
import os
from datetime import datetime

# Configure MLflow to use your local server
mlflow.set_tracking_uri("http://127.0.0.1:8080")
mlflow.set_experiment("basenji_genomics")

def train_with_mlflow():
    with mlflow.start_run(run_name="basenji_heart_training"):
        # Load and log parameters
        with open('models/params_small.json', 'r') as f:
            params = json.load(f)
        
        # Log all parameters (flattened)
        def flatten_dict(d, parent_key='', sep='.'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, str(v)))  # Convert all to string
            return dict(items)
        
        mlflow.log_params(flatten_dict(params))
        mlflow.log_artifact('models/params_small.json')
        
        # Enable auto-logging
        mlflow.keras.autolog()
        
        # Run training
        result = subprocess.run([
            'python',
            'basenji_train.py', 
            '-o', 'models/heart',
            'models/params_small.json',
            'data/heart_l131k'
        ], capture_output=True, text=True)
        
        # Log training output
        with open("training_log.txt", "w") as f:
            f.write(result.stdout)
        mlflow.log_artifact("training_log.txt")
        
        print("Training completed with MLflow tracking!")

# Run it
train_with_mlflow()