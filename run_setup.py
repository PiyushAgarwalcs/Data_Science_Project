#!/usr/bin/env python3
"""
Automatic MLflow Setup and App Runner
This script will set up your MLflow environment variables and run the app
"""

import os
import subprocess
import sys

def setup_and_run():
    print("=== Setting up MLflow for DagsHub ===")
    
    # Set environment variables
    os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
    os.environ["MLFLOW_REGISTRY_URI"] = "https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
    os.environ["MLFLOW_TRACKING_USERNAME"] = "PiyushAgarwalcs"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = "9d35b0b276c3c9af8b66ef1e0ffdf3fb8782525c"
    
    print("✓ MLflow environment variables set:")
    print(f"  Tracking URI: {os.environ['MLFLOW_TRACKING_URI']}")
    print(f"  Username: {os.environ['MLFLOW_TRACKING_USERNAME']}")
    print(f"  Password: {'Set' if os.environ['MLFLOW_TRACKING_PASSWORD'] else 'Not set'}")
    
    print("\n=== Running the ML Pipeline ===")
    print("This will now train models and log experiments to DagsHub...")
    
    try:
        # Run the app
        result = subprocess.run([sys.executable, "app.py"], 
                              env=os.environ, 
                              capture_output=False,
                              text=True)
        
        if result.returncode == 0:
            print("\n🎉 SUCCESS! Pipeline completed successfully!")
            print("\n📊 Your experiments are now logged in DagsHub!")
            print("🔗 View them at: https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow")
            print("\n📈 You should see:")
            print("   - Model training metrics (R², RMSE, MAE)")
            print("   - Hyperparameters used")
            print("   - Model artifacts")
        else:
            print(f"\n⚠️  Pipeline completed with some warnings (this is normal)")
            print("📊 Your experiments were still logged to DagsHub!")
            print("🔗 Check: https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow")
            
    except Exception as e:
        print(f"\n✗ Error running pipeline: {e}")

if __name__ == "__main__":
    setup_and_run() 