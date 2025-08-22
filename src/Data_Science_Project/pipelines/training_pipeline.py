import os
import sys
from src.Data_Science_Project.logger import logging
from src.Data_Science_Project.exception import CustomException

from src.Data_Science_Project.components.data_ingestion import DataIngestion
from src.Data_Science_Project.components.data_transformation import DataTransformation
from src.Data_Science_Project.components.model_trainer import ModelTrainer

class TrainingPipeline:
    """
    Training Pipeline Class
    
    This class orchestrates the complete training process:
    1. Data Ingestion (read data, split into train/test)
    2. Data Transformation (preprocessing, feature engineering)
    3. Model Training (train multiple models, select best)
    """
    
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
    
    def start_training(self):
        """
        Start the complete training pipeline
        """
        try:
            logging.info("🚀 Starting Training Pipeline...")
            
            # Step 1: Data Ingestion
            logging.info("📥 Step 1: Data Ingestion")
            train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()
            logging.info(f"✅ Data ingestion completed")
            logging.info(f"   Train data: {train_data_path}")
            logging.info(f"   Test data: {test_data_path}")
            
            # Step 2: Data Transformation
            logging.info("🔄 Step 2: Data Transformation")
            train_arr, test_arr, preprocessor_path = self.data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info(f"✅ Data transformation completed")
            logging.info(f"   Preprocessor saved at: {preprocessor_path}")
            logging.info(f"   Train array shape: {train_arr.shape}")
            logging.info(f"   Test array shape: {test_arr.shape}")
            
            # Step 3: Model Training
            logging.info("🤖 Step 3: Model Training")
            r2_score = self.model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"✅ Model training completed")
            logging.info(f"   Best model R² score: {r2_score:.4f}")
            
            # Pipeline Summary
            logging.info("🎉 Training Pipeline Completed Successfully!")
            logging.info("="*50)
            logging.info("📊 Pipeline Summary:")
            logging.info(f"   • Data ingested and split")
            logging.info(f"   • Data transformed and preprocessed")
            logging.info(f"   • Models trained and evaluated")
            logging.info(f"   • Best model selected with R²: {r2_score:.4f}")
            logging.info(f"   • All artifacts saved in 'artifacts/' folder")
            logging.info("="*50)
            
            return {
                "status": "success",
                "r2_score": r2_score,
                "train_data_path": train_data_path,
                "test_data_path": test_data_path,
                "preprocessor_path": preprocessor_path,
                "message": "Training pipeline completed successfully"
            }
            
        except Exception as e:
            logging.error(f"❌ Training Pipeline Failed: {e}")
            raise CustomException(e, sys)
    
    def get_pipeline_status(self):
        """
        Get the current status of the training pipeline
        """
        try:
            status = {
                "data_ingestion": {
                    "train_data_exists": os.path.exists(os.path.join("artifacts", "train.csv")),
                    "test_data_exists": os.path.exists(os.path.join("artifacts", "test.csv")),
                    "raw_data_exists": os.path.exists(os.path.join("artifacts", "raw.csv"))
                },
                "data_transformation": {
                    "preprocessor_exists": os.path.exists(os.path.join("artifacts", "preprocessor.pkl"))
                },
                "model_training": {
                    "model_exists": os.path.exists(os.path.join("artifacts", "model.pkl"))
                }
            }
            
            return status
            
        except Exception as e:
            logging.error(f"Error getting pipeline status: {e}")
            return {"error": str(e)}

# Function to run training pipeline (for easy import)
def run_training_pipeline():
    """
    Convenience function to run the training pipeline
    """
    try:
        pipeline = TrainingPipeline()
        result = pipeline.start_training()
        return result
    except Exception as e:
        logging.error(f"Failed to run training pipeline: {e}")
        raise e

if __name__ == "__main__":
    # Test the training pipeline
    try:
        result = run_training_pipeline()
        print(f"✅ Training completed successfully!")
        print(f"R² Score: {result['r2_score']:.4f}")
    except Exception as e:
        print(f"❌ Training failed: {e}")
