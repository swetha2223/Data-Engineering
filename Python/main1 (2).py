import pandas as pd
import numpy as np

#load the csv file

df = pd.read_csv("sample_data.csv")

print(df)

# number of column which has missing values
print(df.isnull().sum())


# also want to find missing records --- data cleaning and processing
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)# saying an engine it starts with and end with to machine using r'^\s*$'.

#drop the rows with missing values
df_cleaned = df.dropna()
print(df_cleaned)

# what are the rows has missing data
print(df[df.isnull().any(axis=1)]) # axis = 1 means operates in horizontal way ,by default it will be by column














