from functools import reduce
from datetime import date
import pandas as pd
from geopy.distance import geodesic
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def count_simba(simba):
    return reduce(lambda acc, s: acc + s.lower().count('simba'), simba, 0)

strings = ["Simba and Nala are lions.", "I laugh in the face of danger.",
                 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

# print(count_simba(strings))

def get_day_month_year(dates):
    return pd.DataFrame(list(map(lambda d: {'day': d.day, 'month': d.month, 'year': d.year}, dates)))

# dates_list = [date(2022, 10, 20), date(2023, 10, 23), date(2024, 10, 24)]
# print(get_day_month_year(dates_list))

def compute_distance(coordinates):
    return list(map(lambda coords: geodesic(coords[0], coords[1]).kilometers, coordinates))

# coordinates = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
# print(compute_distance(coordinates))

def sum_general_int_list(l):
    return reduce(lambda acc, el: acc + (sum_general_int_list(el) if isinstance(el, list) else el), l, 0)

# nlist = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
# print(sum_general_int_list(nlist))

def get_data(path: str) -> pd.DataFrame:
    """
    Getting data from local file
    """
    file_path = Path().parent / path

    data = pd.read_csv(file_path)

    return data

def plot_tree(model: DecisionTreeClassifier, features: list[str], depth: int) -> None:
    """
    120 70 is most optimal for such depth (7)
    """
    plt.figure(figsize=(120, 70))  
    tree.plot_tree(
        decision_tree=model, 
        feature_names=features, 
        filled=True, 
        precision=2, 
        max_depth=depth,
        fontsize=10 
    )
    plt.show()

def get_model(X_train: pd.DataFrame, y_train: pd.DataFrame, depth: int) -> DecisionTreeClassifier:
    """
    Decision Tree was chosen as a predictinve model since we can easier analyze features that actually affects the target graphically
    """
    decision_tree = DecisionTreeClassifier(max_depth=depth)
    decision_tree.fit(X_train, y_train)

    return decision_tree

def preprocess_data(data: pd.DataFrame, nan_columns: list[str]) -> pd.DataFrame:
    """
    Dropping nan values, filling dataframe, encoding features
    """
    data = data.drop(columns=["Unnamed: 0"])

    data = data.dropna(subset=nan_columns)

    data = pd.get_dummies(data, columns=["ethnicity"], drop_first=True)

    label_encoder = LabelEncoder()
    data["gender_binary"] = label_encoder.fit_transform(data["gender"])

    return data