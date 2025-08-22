# 🚀 Quick Start Guide

Get your end-to-end ML project running in 5 minutes!

## **⚡ Super Quick Start**

### **Option 1: One Command (Recommended)**
```bash
python run_complete_project.py
```

This will:
- ✅ Set up MLflow environment
- 🚀 Train your ML model
- 🌐 Start API server
- 🎨 Launch Streamlit frontend
- 🧪 Test everything
- 🌐 Open in browser automatically

### **Option 2: Step by Step**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train model
python app.py

# 3. Start API
python api.py

# 4. Start Streamlit (in new terminal)
streamlit run streamlit_app.py
```

### **Option 3: Use Deployment Script**
```bash
# On Windows (PowerShell)
./deploy.sh

# On Mac/Linux
chmod +x deploy.sh
./deploy.sh
```

## **🌐 What You'll Get**

After running, you'll have:

- **🚀 API Server**: http://localhost:8000
- **📖 API Docs**: http://localhost:8000/docs
- **🎨 Streamlit App**: http://localhost:8501
- **📊 MLflow**: https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow

## **🔧 Troubleshooting**

### **Port Already in Use**
```bash
# Kill processes using ports 8000 and 8501
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

### **Package Installation Issues**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with specific version
pip install -r requirements.txt --force-reinstall
```

### **MLflow Connection Issues**
- Check your DagsHub access token
- Verify repository name in MLflow URI
- Ensure token has MLflow permissions

## **📱 Test Your Project**

1. **Visit Streamlit**: http://localhost:8501
2. **Input features** in the sidebar
3. **Click Predict** button
4. **See results** and visualizations

## **🚀 Next Steps**

- **Customize**: Update feature names in `api.py` and `streamlit_app.py`
- **Deploy**: Use Docker or deploy to cloud
- **Monitor**: Set up model monitoring with Evidently AI
- **Scale**: Add authentication and database

## **💡 Pro Tips**

- **Keep terminal open**: Services run in background
- **Check logs**: Look in `logs/` folder for debugging
- **Git commit**: Save your progress regularly
- **Experiment**: Try different ML algorithms in `model_trainer.py`

---

**🎉 You now have a production-ready ML system!** 

This demonstrates enterprise-level ML engineering that companies actually use! 🚀 