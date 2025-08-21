import os
import sys
from src.Data_Science_Project.exception import CustomException
from src.Data_Science_Project.logger import logging
import pandas as pd
import pymysql

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
