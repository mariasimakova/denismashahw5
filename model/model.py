from sklearn.linear_model import LogisticRegression, LinearRegression
import pandas as pd
import numpy as np

from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, feature_columns: list[str], target_column: str, model):
        self._feature_columns = feature_columns 
        self._target_column = target_column
        self.model = model
    
    @abstractmethod
    def train(self, data: pd.DataFrame) -> None:
        X = data[self._feature_columns]
        y = data[self._target_column]
        self.model.fit(X, y)

    @abstractmethod
    def predict(self, data: pd.DataFrame) -> np.ndarray:
        pass

class LogModel(Model):
    def __init__(self, feature_columns: list[str], target_column: str, model=LogisticRegression()):
        super().__init__(feature_columns, target_column, model)
    
    def train(self, data: pd.DataFrame) -> None:
        X = data[self._feature_columns]
        y = data[self._target_column]
        self.model.fit(X, y)

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        X = data[self._feature_columns]

        return self.model.predict_proba(X)[:, 1] 

class LinearModel(Model):
    def __init__(self, feature_columns: list[str], target_column: str, model=LinearRegression()):
        super().__init__(feature_columns, target_column, model)

    def train(self, data: pd.DataFrame) -> None:
        X = data[self._feature_columns]
        y = data[self._target_column]
        self.model.fit(X, y)

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        X = data[self._feature_columns]

        return self.model.predict(X) 