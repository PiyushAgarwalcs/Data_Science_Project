from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import pandas as pd
import numpy as np
from src.Data_Science_Project.pipelines.prediction_pipeline import PredictionPipeline
from src.Data_Science_Project.logger import logging

# Initialize FastAPI app
app = FastAPI(
    title="Student Performance Prediction API",
    description="API for predicting student performance scores",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize prediction pipeline
predictor = PredictionPipeline()

# Define input data model
class PredictionInput(BaseModel):
    # Update these fields based on your actual features
    feature1: float
    feature2: float
    feature3: float
    # Add all your features here
    
    class Config:
        schema_extra = {
            "example": {
                "feature1": 25.0,
                "feature2": 80.0,
                "feature3": 3.5,
                # Add example values for all features
            }
        }

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float
    message: str

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Student Performance Prediction API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: PredictionInput):
    """Make a prediction for student performance"""
    try:
        logging.info(f"Received prediction request: {input_data}")
        
        # Convert input to dictionary
        features = input_data.dict()
        
        # Make prediction
        prediction = predictor.predict_single(features)
        
        # Calculate confidence (you can implement your own confidence metric)
        confidence = 0.85  # Placeholder - implement based on your model
        
        response = PredictionResponse(
            prediction=float(prediction),
            confidence=confidence,
            message="Prediction successful"
        )
        
        logging.info(f"Prediction completed: {prediction}")
        return response
        
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-batch")
async def predict_batch(input_data: list[PredictionInput]):
    """Make predictions for multiple students"""
    try:
        logging.info(f"Received batch prediction request for {len(input_data)} samples")
        
        # Convert to list of dictionaries
        features_list = [data.dict() for data in input_data]
        
        # Convert to DataFrame
        input_df = pd.DataFrame(features_list)
        
        # Make predictions
        predictions = predictor.predict(input_df)
        
        # Format response
        results = []
        for i, pred in enumerate(predictions):
            results.append({
                "sample_id": i,
                "prediction": float(pred),
                "confidence": 0.85  # Placeholder
            })
        
        logging.info(f"Batch prediction completed for {len(predictions)} samples")
        return {
            "predictions": results,
            "total_samples": len(predictions),
            "message": "Batch prediction successful"
        }
        
    except Exception as e:
        logging.error(f"Error in batch prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model-info")
async def get_model_info():
    """Get information about the trained model"""
    try:
        # You can implement this to return model metadata
        return {
            "model_type": "Student Performance Predictor",
            "features": [
                "feature1",
                "feature2", 
                "feature3",
                # Add your actual feature names
            ],
            "target": "student_score",
            "last_trained": "2025-08-22",
            "performance_metrics": {
                "r2_score": 0.88,
                "rmse": 0.12,
                "mae": 0.09
            }
        }
    except Exception as e:
        logging.error(f"Error getting model info: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 