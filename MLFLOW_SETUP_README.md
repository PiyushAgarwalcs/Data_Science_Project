# MLflow Setup for DagsHub

This guide will help you configure MLflow to track experiments in DagsHub.

## Prerequisites

1. **DagsHub Account**: Make sure you have a DagsHub account
2. **Access Token**: You need to create an access token with MLflow permissions

## Getting Your DagsHub Access Token

1. Go to [DagsHub](https://dagshub.com) and sign in
2. Go to **Settings** → **Access Tokens**
3. Click **Create Token**
4. Give it a name (e.g., "MLflow Access")
5. Make sure **MLflow** permission is checked
6. Copy the generated token

## Setup Methods

### Method 1: Using the Python Script (Recommended)

1. Run the setup script:
   ```bash
   python setup_mlflow.py
   ```

2. Enter your DagsHub username and access token when prompted

3. The script will set environment variables for the current session

### Method 2: Using the Batch Script (Windows)

1. Double-click `setup_mlflow.bat`
2. Enter your DagsHub username and access token when prompted
3. The script will set environment variables for the current terminal session

### Method 3: Manual Environment Variable Setup

Set these environment variables in your system:

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow
MLFLOW_REGISTRY_URI=https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow
MLFLOW_TRACKING_USERNAME=your_dagshub_username
MLFLOW_TRACKING_PASSWORD=your_dagsHub_access_token
```

## Running Your ML Pipeline

After setting up the environment variables:

1. Run your main application:
   ```bash
   python app.py
   ```

2. The application will now:
   - Check if MLflow is properly configured
   - Log experiments to DagsHub
   - Display experiment metrics and parameters

## Verifying the Setup

1. **Check the logs**: Look for MLflow configuration messages
2. **Visit DagsHub**: Go to your repository and check the MLflow tab
3. **Check experiment runs**: You should see your experiments with metrics and parameters

## Troubleshooting

### Common Issues

1. **"MLflow not properly configured" error**
   - Make sure you've set the environment variables
   - Run the setup script again

2. **Authentication failed**
   - Verify your username and access token
   - Make sure the token has MLflow permissions

3. **No experiments showing in DagsHub**
   - Check if the tracking URI is correct
   - Verify your repository name matches exactly

### Debug Information

The application now logs MLflow configuration details. Check the logs for:
- Tracking URI
- Username
- Password status

## Notes

- Environment variables set by scripts are only valid for the current session
- For permanent setup, use system environment variables
- The access token should be kept secure and not committed to version control
- You can regenerate access tokens if needed

## Support

If you continue to have issues:
1. Check the application logs for error messages
2. Verify your DagsHub repository settings
3. Ensure MLflow is enabled in your DagsHub repository 