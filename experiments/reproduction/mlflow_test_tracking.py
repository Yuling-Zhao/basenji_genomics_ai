import mlflow
import json
import subprocess
import os
from datetime import datetime

# Configure MLflow to use your local server
mlflow.set_tracking_uri("http://127.0.0.1:8080")
mlflow.set_experiment("basenji_genomics")

def test_with_mlflow():
    with mlflow.start_run(run_name="basenji_heart_testing") as run:
        # Load and log parameters (same as training)
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
                    items.append((new_key, str(v)))
            return dict(items)
        
        mlflow.log_params(flatten_dict(params))
        mlflow.log_artifact('models/params_small.json')
        
        # Log test configuration
        mlflow.log_params({
            "test.ensemble_rc": True,
            "test.ensemble_shifts": "1,0,-1",
            "test.target_indices": "0,1,2",
            "test.model_path": "models/heart/model_best.h5"
        })
        
        # Run testing
        print("Running basenji_test.py...")
        result = subprocess.run([
            'python', 'basenji_test.py',
            '--ai', '0,1,2',
            '-o', 'output/heart_test',
            '--rc',
            '--shifts', '1,0,-1',
            'models/params_small.json',
            'models/heart/model_best.h5',
            'data/heart_l131k'
        ], capture_output=True, text=True)
        
        # Log test output
        with open("test_log.txt", "w") as f:
            f.write(result.stdout)
            if result.stderr:
                f.write("\nSTDERR:\n")
                f.write(result.stderr)
        mlflow.log_artifact("test_log.txt")
        
        # Parse and log test metrics from acc.txt
        acc_file = "output/heart_test/acc.txt"
        if os.path.exists(acc_file):
            mlflow.log_artifact(acc_file)
            
            # Parse accuracy metrics and log to MLflow
            with open(acc_file, 'r') as f:
                lines = f.readlines()
                # Skip header line
                for line in lines[1:]:
                    parts = line.strip().split('\t')
                    if len(parts) >= 3:
                        index = parts[0]
                        pearsonr = float(parts[1])
                        r2 = float(parts[2])
                        identifier = parts[3] if len(parts) > 3 else f"target_{index}"
                        
                        # Log metrics for each target
                        mlflow.log_metric(f"test_pearsonr_{identifier}", pearsonr)
                        mlflow.log_metric(f"test_r2_{identifier}", r2)
                        mlflow.log_metric(f"test_pearsonr_target_{index}", pearsonr)
                        mlflow.log_metric(f"test_r2_target_{index}", r2)
            
            print(f"Logged metrics from {acc_file}")
        
        # Log all test artifacts
        test_output_dir = "output/heart_test"
        if os.path.exists(test_output_dir):
            # Log entire test output directory
            mlflow.log_artifacts(test_output_dir, "test_output")
            
            # Log specific important plots
            plot_dirs = ['pr', 'roc', 'scatter', 'violin']
            for plot_dir in plot_dirs:
                plot_path = os.path.join(test_output_dir, plot_dir)
                if os.path.exists(plot_path):
                    mlflow.log_artifacts(plot_path, f"test_plots/{plot_dir}")
        
        # Log model file
        if os.path.exists("models/heart/model_best.h5"):
            mlflow.log_artifact("models/heart/model_best.h5", "model")
        
        print(f"Testing completed! Run ID: {run.info.run_id}")
        print(f"Test results logged to MLflow")
        print(f"Artifacts: {test_output_dir}")

# Run the test
if __name__ == "__main__":
    test_with_mlflow()