#!/usr/bin/env python3
"""
MLflow Configuration Setup Script for DagsHub
Run this script to set up your MLflow environment variables
"""

import os
import getpass

def setup_mlflow_config():
    print("=== MLflow Configuration Setup for DagsHub ===\n")
    
    # Set tracking URI
    tracking_uri = "https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
    os.environ["MLFLOW_TRACKING_URI"] = tracking_uri
    os.environ["MLFLOW_REGISTRY_URI"] = tracking_uri
    
    print(f"✓ MLflow Tracking URI set to: {tracking_uri}")
    
    # Get username
    username = input("Enter your DagsHub username: ").strip()
    if username:
        os.environ["MLFLOW_TRACKING_USERNAME"] = username
        print(f"✓ Username set to: {username}")
    
    # Get password/token
    password = getpass.getpass("Enter your DagsHub access token: ").strip()
    if password:
        os.environ["MLFLOW_TRACKING_PASSWORD"] = password
        print("✓ Access token set")
    
    print("\n=== Configuration Complete ===")
    print("You can now run your ML pipeline and experiments will be tracked in DagsHub!")
    print("\nNote: These environment variables are only set for the current session.")
    print("To make them permanent, you can:")
    print("1. Create a .env file with these variables")
    print("2. Set them in your system environment")
    print("3. Run this script before each session")
    
    return True

if __name__ == "__main__":
    setup_mlflow_config() 