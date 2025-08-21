from src.Data_Science_Project.logger import logging
from src.Data_Science_Project.exception import CustomException

from src.Data_Science_Project.components.data_ingestion import DataIngestion
from src.Data_Science_Project.components.data_ingestion import DataIngestionConfig

from src.Data_Science_Project.components.data_transformation import DataTransformation
from src.Data_Science_Project.components.data_transformation import DataTransformationConfig

from src.Data_Science_Project.components.model_trainer import ModelTrainer
from src.Data_Science_Project.components.model_trainer import ModelTrainerConfig

import sys


if __name__ == "__main__":
    logging.info("Starting the application...")

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

  