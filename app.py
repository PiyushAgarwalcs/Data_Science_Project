from src.Data_Science_Project.logger import logging
from src.Data_Science_Project.exception import CustomException

from src.Data_Science_Project.components.data_ingestion import DataIngestion
from src.Data_Science_Project.components.data_ingestion import DataIngestionConfig

from src.Data_Science_Project.components.data_transformation import DataTransformation
from src.Data_Science_Project.components.data_transformation import DataTransformationConfig

from src.Data_Science_Project.components.model_trainer import ModelTrainer
from src.Data_Science_Project.components.model_trainer import ModelTrainerConfig

import sys
import os

# Check MLflow configuration
def check_mlflow_config():
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    username = os.getenv("MLFLOW_TRACKING_USERNAME")
    password = os.getenv("MLFLOW_TRACKING_PASSWORD")
    
    logging.info(f"MLflow Tracking URI: {tracking_uri}")
    logging.info(f"MLflow Username: {username}")
    logging.info(f"MLflow Password: {'Set' if password else 'Not set'}")
    
    if not all([tracking_uri, username, password]):
        logging.warning("MLflow environment variables not properly configured!")
        logging.warning("Run setup_mlflow.py or setup_mlflow.bat to configure MLflow for DagsHub")
        return False
    return True


if __name__ == "__main__":
    logging.info("Starting the application...")

    # Check MLflow configuration
    if not check_mlflow_config():
        logging.error("MLflow not properly configured. Please set up environment variables first.")
        sys.exit(1)

    try:
        # Use the training pipeline instead of individual components
        from src.Data_Science_Project.pipelines.training_pipeline import run_training_pipeline
        
        logging.info("🚀 Running complete training pipeline...")
        r2_score = run_training_pipeline()
        
        print(f"🎉 Training pipeline completed successfully!")
        print(f"📊 Best model R² score: {r2_score:.4f}")
        print(f"📁 Check artifacts/ folder for saved models")
        print(f"📈 View experiments in DagsHub MLflow")

    except Exception as e:
        logging.error("Training pipeline failed")
        raise CustomException(e, sys) from e

  