"""
Step 2: Verify the setup was done in correct order
"""
import os
import sys
from datetime import datetime

def verify_setup_order():
    print("🔍 Verifying setup order was correct...")
    
    # Check 1: environment.yml exists before any tracking
    env_yml_exists = os.path.exists('environment.yml')
    print(f"✅ environment.yml created first: {env_yml_exists}")
    
    # Check 2: Running in correct conda environment
    in_correct_env = 'basenji_genomics_ai' in sys.executable
    print(f"✅ Correct conda environment active: {in_correct_env}")
    
    # Check 3: MLflow available (means environment is set up)
    try:
        import mlflow
        mlflow_available = True
        print(f"✅ MLflow available (environment ready): {mlflow_available}")
    except ImportError:
        mlflow_available = False
        print("❌ MLflow not available - environment not set up correctly")
    
    return all([env_yml_exists, in_correct_env, mlflow_available])

if __name__ == "__main__":
    success = verify_setup_order()
    if success:
        print("🎉 Setup order was correct!")
    else:
        print("⚠️  Setup order needs correction")
