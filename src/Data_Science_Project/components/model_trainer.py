import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# from sklearn.neighbours import KNeighboursRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.Data_Science_Project.exception import CustomException
from src.Data_Science_Project.logger import logging

from src.Data_Science_Project.utils import save_object, evaluate_model

# For MLflow
import mlflow
from urllib.parse import urlparse



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def eval_metrics(self, actual, pred):
        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
        rmse = mean_squared_error(actual, pred, squared=False)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and testing data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=0),
                #"K-Neighbours Regressor": KNeighboursRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # Hyperparameter tuning

            params = {
                "Decision Tree": {
                    "criterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
                    # 'splitter': ['best', 'random'],
                    # 'max_features': ['sqrt', 'log2']
                },
                "Random Forest": {
                    # "criterion": ["squared_error", "friedam_mse", "absolute_error", "poisson"],
                    # 'max_features': ['sqrt', 'log2', 'None'],
                    "n_estimators": [8, 16, 32, 64, 128, 256]
                },
                "Gradient Boosting": {
                    # "loss": ["squared_error", "absolute_error", "huber", "quantile"],
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    "subsample": [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    # 'criterion': ['friedman_mse', 'squared_error'],
                    # 'max_features': ['sqrt', 'log2', 'auto'],
                    "n_estimators": [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "XGBRegressor": {
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    "n_estimators": [8, 16, 32, 64, 128, 256]
                },
                "CatBoosting Regressor": {
                    "depth": [6, 8, 10],
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    "iterations": [30, 50, 100]
                },
                "AdaBoost Regressor": {
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    # 'loss': ['linear', 'square', 'exponential'],
                    "n_estimators": [8, 16, 32, 64, 128, 256]
                }
            }
            model_report:dict = evaluate_model(
                X_train, y_train, X_test, y_test, models, params
            )

            ## To get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dictionary
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            print(f"Best model found: {best_model_name} with score: {best_model_score}")

            model_name = list(params.keys())

            actual_model = ""

            for model in model_name:
                if model == best_model_name:
                    actual_model = actual_model + model
                    
            best_params = params[actual_model]




            mlflow.set_registry_uri("https://dagshub.com/PiyushAgarwalcs/Data_Science_Project.mlflow")
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # ML flow

            with mlflow.start_run():

                predicted_qualities = best_model.predict(X_test)

                (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

                # mlflow.log_param(best_params)
                for param_name, param_value in best_params.items():
                    mlflow.log_param(param_name, param_value)
                
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)
                
            
                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    # Register the model
                    # There are two ways to log the model
                    # 1. Log the model with a name
                    # 2. Register the model with a name
                    # There are other ways to use the model registry, which depend on the tracking server configuration.
                    # Here we are using the second way to register the model.
                    # Link for more details: https://www.mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(best_model, "model", registered_model_name="StudentScorePredictor")
                else:
                    mlflow.sklearn.log_model(best_model, "model")












            if best_model_score < 0.6:
                raise CustomException("model is not good enough")
            logging.info(f"Best model found on both training and testing dataset.")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)

