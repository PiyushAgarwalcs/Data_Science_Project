#!/bin/bash

echo "🚀 Deploying Complete End-to-End ML Project"
echo "=============================================="

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    exit 1
fi

echo "✅ Python is available"

# Check if required packages are installed
echo "🔍 Checking required packages..."
python -c "import fastapi, streamlit, mlflow" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing required packages..."
    pip install -r requirements.txt
else
    echo "✅ Required packages are already installed"
fi

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p artifacts logs

# Set environment variables
echo "🔧 Setting environment variables..."
export MLFLOW_TRACKING_URI="https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
export MLFLOW_REGISTRY_URI="https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow"
export MLFLOW_TRACKING_USERNAME="PiyushAgarwalcs"
export MLFLOW_TRACKING_PASSWORD="9d35b0b276c3c9af8b66ef1e0ffdf3fb8782525c"

echo "✅ Environment variables set"

# Run the complete project
echo "🚀 Starting the complete project..."
python run_complete_project.py

echo "🎉 Deployment completed!"
echo ""
echo "📖 Manual access:"
echo "   - API: http://localhost:8000"
echo "   - API Docs: http://localhost:8000/docs"
echo "   - Streamlit: http://localhost:8501"
echo "   - MLflow: https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow" 