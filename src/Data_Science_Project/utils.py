import os
import sys
from src.Data_Science_Project.exception import CustomException
from src.Data_Science_Project.logger import logging
import pandas as pd
import pymysql

# For model training
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

# Common func for pickle file saving - save_object
import pickle
import numpy as np


# Taking Info from .env
from dotenv import load_dotenv
load_dotenv()

# Database connection details
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading data from MySQL database...")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connected to the database successfully.")
        df = pd.read_sql_query('SELECT * FROM students', mydb)  # Replace with your actual table name
        print(df.head()) 
        return df
    
    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    """
    Saves the object as a pickle file at the specified file path.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(x_train, y_train, x_test, y_test, models, param):
    """
    Takes all models and parameters as input.
    selects the best parameters for each model using GridSearchCV.
    Fits and takes the r2 score of train and test.
    Returns a dictionary with model names as keys and their r2 scores of test.
    """
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]] 

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(x_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train, y_train)

            #model.fit(x_train, y_train) # Train the model 

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report


    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    """
    Loads a pickle file from the specified file path and returns the object.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)