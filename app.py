from src.Data_Science_Project.logger import logging
from src.Data_Science_Project.exception import CustomException

from src.Data_Science_Project.components.data_ingestion import DataIngestion
from src.Data_Science_Project.components.data_ingestion import DataIngestionConfig
import sys


if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Train data saved at: {train_data_path}")
        logging.info(f"Test data saved at: {test_data_path}")

        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys) from e

  