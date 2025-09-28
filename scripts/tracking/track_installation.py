"""
Step 3: Track the complete installation process
"""
import mlflow
import subprocess
import sys
from datetime import datetime

def track_complete_installation():
    mlflow.set_tracking_uri("http://127.0.0.1:8080")
    mlflow.set_experiment("environment_setup")
    
    with mlflow.start_run(run_name="complete_basenji_environment"):
        mlflow.log_param("based_on", "basenji_requirements")
        mlflow.log_param("adapted_for", "mac_cpu")
        mlflow.log_param("timestamp", datetime.now().isoformat())
        
        # Log the original requirements for reference
        original_reqs = """astropy, cooler, cooltools, h5py, joblib, intervaltree, 
        matplotlib, natsort, networkx, numpy, pandas, pillow, pybigwig, pysam, 
        pybedtools, qnorm, seaborn, scikit-learn, scipy, statsmodels, tabulate"""
        mlflow.log_param("original_basenji_requirements", original_reqs)
        
        # Test all imports
        packages_to_test = [
            "numpy", "pandas", "scipy", "sklearn", "matplotlib", "seaborn",
            "h5py", "pyBigWig", "pysam", "cooler", "astropy", "joblib",
            "networkx", "PIL", "statsmodels", "mlflow", "tensorflow"
        ]
        
        results = {}
        for package in packages_to_test:
            try:
                if package == "PIL":
                    imported = __import__("PIL")
                else:
                    imported = __import__(package)
                
                version = getattr(imported, '__version__', 'unknown')
                results[package] = {"status": "success", "version": version}
                mlflow.log_metric(f"{package}_success", 1)
                print(f"✅ {package} v{version}")
                
            except ImportError as e:
                results[package] = {"status": "failed", "error": str(e)}
                mlflow.log_metric(f"{package}_success", 0)
                print(f"❌ {package}: {e}")
        
        # Calculate success rate
        success_count = sum(1 for r in results.values() if r["status"] == "success")
        success_rate = success_count / len(packages_to_test)
        
        mlflow.log_metric("overall_success_rate", success_rate)
        mlflow.log_param("packages_tested", len(packages_to_test))
        mlflow.log_param("packages_successful", success_count)
        
        print(f"\n📊 Overall: {success_count}/{len(packages_to_test)} packages successful ({success_rate:.1%})")
        
        if success_rate > 0.9:
            print("🎉 Environment setup successful!")
        else:
            print("⚠️ Some packages failed to install")
        
        return success_rate > 0.9

if __name__ == "__main__":
    if 'basenji_genomics_ai' not in sys.executable:
        print("Please activate environment first: conda activate basenji_genomics_ai")
    else:
        track_complete_installation()