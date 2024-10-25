from sklearn.model_selection import train_test_split

import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, path: str) -> None:
        self.file_path = Path(__file__).parent.parent / path
        self.data = pd.read_csv(self.file_path)

    def get_data(self, test_size: float, random_state: int) -> list[pd.DataFrame]:
        train_data, test_data = train_test_split(self.data, test_size=test_size, random_state=random_state)

        return train_data, test_data
    
class NanDropper:
    def __init__(self, columns: list[str]):
        self.columns = columns

    def process(self, data: pd.DataFrame):
        return data.dropna(subset=self.columns).copy()
    
class NanFiller:
    def __init__(self, columns: list[str]):
        self.columns = columns

    def process(self, data: pd.DataFrame):
        for column in self.columns:
            data[column] = data[column].fillna(data[column].mean())
            
        return data.copy()
    

    
