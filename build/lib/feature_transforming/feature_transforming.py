from abc import ABC, abstractmethod

import pandas as pd

class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

class EthnicityTransformer(FeatureTransformer):
    def transform(self, data: pd.DataFrame):
        data["ethnicity_group"] = pd.Categorical(data["ethnicity"]).codes

        return data

class GenderTransformer(FeatureTransformer):
    def transform(self, data: pd.DataFrame):
        data['gender_numeric'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)

        return data

class AgeTransformer(FeatureTransformer):
    def transform(self, data: pd.DataFrame):
        data['age_category'] = data['age'].apply(lambda x: 1 if x >= 50 else 0)

        return data