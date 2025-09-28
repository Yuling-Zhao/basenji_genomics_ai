"""
Step 1: MLflow tracking for project creation process
"""
import mlflow
import os
import subprocess
from datetime import datetime

def track_project_creation():
    # Set up MLflow tracking
    mlflow.set_tracking_uri("http://127.0.0.1:8080")
    mlflow.set_experiment("project_creation")
    
    with mlflow.start_run(run_name="initial_project_setup"):
        # Log basic project info
        mlflow.log_param("project_name", "basenji_genomics_ai")
        mlflow.log_param("purpose", "postdoc_application_showcase")
        mlflow.log_param("timestamp", datetime.now().isoformat())
        mlflow.log_param("setup_phase", "directory_structure")
        
        # Get current directory info
        current_dir = os.getcwd()
        mlflow.log_param("project_path", current_dir)
        
        # Log the created directory structure
        structure_result = subprocess.run(["find", ".", "-type", "d"], 
                                        capture_output=True, text=True)
        mlflow.log_text(structure_result.stdout, "project_structure.txt")
        
        # Count directories created
        dir_count = len([line for line in structure_result.stdout.split('\n') if line.strip()])
        mlflow.log_metric("directories_created", dir_count)
        
        print(f"✅ Project structure created with {dir_count} directories")
        print("📁 Directory structure saved to MLflow")
        
        return True

if __name__ == "__main__":
    # Start MLflow server first if not running
    print("Make sure MLflow server is running: mlflow server --host 127.0.0.1 --port 8080")
    track_project_creation()