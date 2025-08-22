import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.Data_Science_Project.logger import logging
from src.Data_Science_Project.exception import CustomException
from src.Data_Science_Project.components.data_transformation import DataTransformation

class PredictionPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
        
    def load_model_and_preprocessor(self):
        """Load the trained model and preprocessor"""
        try:
            logging.info("Loading trained model and preprocessor...")
            
            if not os.path.exists(self.model_path):
                raise CustomException(f"Model file not found at {self.model_path}")
            
            if not os.path.exists(self.preprocessor_path):
                raise CustomException(f"Preprocessor file not found at {self.preprocessor_path}")
            
            with open(self.model_path, 'rb') as f:
                model = pickle.load(f)
            
            with open(self.preprocessor_path, 'rb') as f:
                preprocessor = pickle.load(f)
            
            logging.info("Model and preprocessor loaded successfully")
            return model, preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def preprocess_data(self, data, preprocessor):
        """Preprocess new data using the fitted preprocessor"""
        try:
            logging.info("Preprocessing new data...")
            
            # Apply the same preprocessing steps
            processed_data = preprocessor.transform(data)
            
            logging.info("Data preprocessing completed")
            return processed_data
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def predict(self, input_data):
        """Make predictions on new data"""
        try:
            logging.info("Starting prediction pipeline...")
            
            # Load model and preprocessor
            model, preprocessor = self.load_model_and_preprocessor()
            
            # Preprocess input data
            processed_data = self.preprocess_data(input_data, preprocessor)
            
            # Make predictions
            predictions = model.predict(processed_data)
            
            logging.info(f"Predictions completed. Shape: {predictions.shape}")
            return predictions
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def predict_single(self, features_dict):
        """Make prediction for a single sample"""
        try:
            # Convert single sample to DataFrame
            input_df = pd.DataFrame([features_dict])
            
            # Make prediction
            prediction = self.predict(input_df)
            
            return prediction[0]  # Return single prediction
            
        except Exception as e:
            raise CustomException(e, sys)

# Example usage function
def run_prediction_example():
    """Example of how to use the prediction pipeline"""
    try:
        # Sample input data (adjust based on your feature columns)
        sample_data = {
            'feature1': 25,
            'feature2': 80,
            'feature3': 3.5,
            # Add all your features here
        }
        
        # Initialize prediction pipeline
        predictor = PredictionPipeline()
        
        # Make prediction
        prediction = predictor.predict_single(sample_data)
        
        print(f"Predicted Score: {prediction:.2f}")
        return prediction
        
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

if __name__ == "__main__":
    run_prediction_example()
