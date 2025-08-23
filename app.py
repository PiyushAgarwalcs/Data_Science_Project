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
        # data_transformation_config = DataTransformationConfig()

        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        # logging.info(f"Train data saved at: {train_data_path}")
        # logging.info(f"Test data saved at: {test_data_path}")

        
        # data_transformation_config = DataTransformationConfig()

        data_transformation = DataTransformation()
        train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)


        ## Model Training
        model_trainer = ModelTrainer()
        r2 = model_trainer.initiate_model_trainer(train_arr, test_arr)
        print(f"Model training completed. R² score: {r2}")


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys) from e

  