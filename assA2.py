import pandas as pd
dataset = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Python/DataPreprocessing.csv')
dataset
dataset.isnull()
dataset.isnull().head(10)
dataset.isnull().sum()
dataset.isnull().head().sum()
modifieddataset=dataset.fillna(" ")
modifieddataset.isnull().sum()
dataset=dataset.dropna()
