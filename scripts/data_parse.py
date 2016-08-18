import pandas as pd

data = pd.read_csv('./data_sets/train_categorical.csv')
print(data.tail())
print(data.describe())
