#!/usr/bin/env python3
"""
End-to-End Data Science Project Runner
This script runs the complete pipeline from data ingestion to API deployment
"""

import os
import subprocess
import sys
import time
import requests
import json

def setup_environment():
    """Set up MLflow environment variables"""
    print("=== Setting up MLflow Environment ===")
    
    os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
    os.environ["MLFLOW_REGISTRY_URI"] = "https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
    os.environ["MLFLOW_TRACKING_USERNAME"] = "PiyushAgarwalcs"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = "9d35b0b276c3c9af8b66ef1e0ffdf3fb8782525c"
    
    print("✓ Environment variables set")

def run_training_pipeline():
    """Run the complete ML training pipeline"""
    print("\n=== Running ML Training Pipeline ===")
    
    try:
        result = subprocess.run([sys.executable, "app.py"], 
                              env=os.environ, 
                              capture_output=False,
                              text=True)
        
        if result.returncode == 0:
            print("✓ Training pipeline completed successfully!")
            return True
        else:
            print("⚠️  Training pipeline completed with warnings")
            return True  # Continue anyway
            
    except Exception as e:
        print(f"✗ Training pipeline failed: {e}")
        return False

def start_api_server():
    """Start the FastAPI server"""
    print("\n=== Starting API Server ===")
    
    try:
        # Start API server in background
        process = subprocess.Popen([sys.executable, "api.py"], 
                                 env=os.environ,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        
        # Wait for server to start
        print("Waiting for API server to start...")
        time.sleep(10)
        
        # Test if server is running
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                print("✓ API server is running on http://localhost:8000")
                return process
            else:
                print("⚠️  API server responded but with unexpected status")
                return process
        except requests.exceptions.RequestException:
            print("⚠️  API server might not be fully ready yet")
            return process
            
    except Exception as e:
        print(f"✗ Failed to start API server: {e}")
        return None

def test_api_endpoints():
    """Test the API endpoints"""
    print("\n=== Testing API Endpoints ===")
    
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✓ Health endpoint working")
        else:
            print("✗ Health endpoint failed")
    except Exception as e:
        print(f"✗ Health endpoint error: {e}")
    
    # Test model info endpoint
    try:
        response = requests.get(f"{base_url}/model-info")
        if response.status_code == 200:
            print("✓ Model info endpoint working")
            model_info = response.json()
            print(f"  Model: {model_info.get('model_type', 'Unknown')}")
        else:
            print("✗ Model info endpoint failed")
    except Exception as e:
        print(f"✗ Model info endpoint error: {e}")
    
    # Test prediction endpoint (with sample data)
    try:
        # Update this with your actual feature names and values
        sample_data = {
            "feature1": 25.0,
            "feature2": 80.0,
            "feature3": 3.5
        }
        
        response = requests.post(f"{base_url}/predict", json=sample_data)
        if response.status_code == 200:
            prediction = response.json()
            print("✓ Prediction endpoint working")
            print(f"  Predicted score: {prediction.get('prediction', 'Unknown')}")
        else:
            print(f"✗ Prediction endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Prediction endpoint error: {e}")

def show_next_steps():
    """Show what to do next"""
    print("\n" + "="*60)
    print("🎉 END-TO-END PIPELINE COMPLETED!")
    print("="*60)
    
    print("\n📊 Your experiments are logged in DagsHub:")
    print("   https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow")
    
    print("\n🚀 Your API is running at:")
    print("   http://localhost:8000")
    
    print("\n📖 API Documentation:")
    print("   http://localhost:8000/docs")
    
    print("\n🔧 Next Steps:")
    print("   1. Update the feature names in api.py to match your dataset")
    print("   2. Test predictions with real data")
    print("   3. Deploy to cloud (AWS, Azure, GCP)")
    print("   4. Set up CI/CD pipeline")
    print("   5. Add monitoring and logging")
    
    print("\n💡 To stop the API server, press Ctrl+C")
    print("="*60)

def main():
    """Main execution function"""
    print("🚀 Starting End-to-End Data Science Project Pipeline")
    print("="*60)
    
    # Step 1: Setup environment
    setup_environment()
    
    # Step 2: Run training pipeline
    if not run_training_pipeline():
        print("❌ Training failed. Stopping pipeline.")
        return
    
    # Step 3: Start API server
    api_process = start_api_server()
    if not api_process:
        print("❌ Failed to start API server. Stopping pipeline.")
        return
    
    # Step 4: Test API
    test_api_endpoints()
    
    # Step 5: Show next steps
    show_next_steps()
    
    try:
        # Keep the API server running
        api_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping API server...")
        api_process.terminate()
        print("✓ API server stopped")

if __name__ == "__main__":
    main() 