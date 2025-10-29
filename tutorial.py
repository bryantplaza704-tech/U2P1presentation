import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'], index = ["x", "y", "z"])
print(df.head())

print(df.info)
print(df.index)
print(df.describe())
print(df.nunique())
print(df['a'].unique())
print(df.size)