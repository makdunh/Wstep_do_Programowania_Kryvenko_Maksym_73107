import pandas as pd

df = pd.read.csv(filepath_or_buffer: "demografia.csv", na_values=["NA", "NaN"])
print(df.head())
print(df.describe())
print(df.info())
