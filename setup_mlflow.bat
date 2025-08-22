@echo off
echo === MLflow Configuration Setup for DagsHub ===
echo.

set MLFLOW_TRACKING_URI=https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow
set MLFLOW_REGISTRY_URI=https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow

echo MLflow Tracking URI set to: %MLFLOW_TRACKING_URI%
echo.

set /p MLFLOW_TRACKING_USERNAME=Enter your DagsHub username: 
set /p MLFLOW_TRACKING_PASSWORD=Enter your DagsHub access token: 

echo.
echo === Configuration Complete ===
echo You can now run your ML pipeline in this terminal session!
echo.
echo Note: These environment variables are only set for the current terminal session.
echo To make them permanent, you can:
echo 1. Set them in Windows System Environment Variables
echo 2. Run this script before each session
echo.
pause 