from sklearn.linear_model import LogisticRegression

import pandas as pd
import numpy as np

class Model:
    def __init__(self, feature_columns: list[str], target_column: str, model=LogisticRegression()):
        self.__feature_columns = feature_columns
        self.__target_column = target_column
        self.model = model

    def train(self, data: pd.DataFrame) -> None:
        X = data[self.__feature_columns]
        y = data[self.__target_column]

        self.model.fit(X, y)

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        X = data[self.__feature_columns]
        
        return self.model.predict_proba(X)[:, 1]
