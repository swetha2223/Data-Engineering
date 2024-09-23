
import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('sample_data.csv')

print("Before Transformation")
print(df)

# Ensure there are no leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Strip spaces from the 'City' column and replace empty strings with NaN
df['City'] = df['City'].str.strip().replace('', np.nan)

# Fill missing values in the 'City' column with 'Unknown'
df['City'] = df['City'].fillna('Unknown')

# Fill missing values in the 'Age' column with the median age
df['Age'] = pd.to_numeric(df['Age'].str.strip(), errors='coerce')

df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing values in the 'Salary' column with the median salary
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\n", "After Transformation")
print(df)


# merging and transforming data
# Sample DataFrames
df1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4],
    'employee_name': ['John Doe', 'Jane Smith', 'Sam Brown', 'Emily Davis']
})

df2 = pd.DataFrame({
    'employee_id': [3, 4, 5, 6],
    'department': ['Finance', 'HR', 'IT', 'Marketing']
})

# Merge the DataFrames on 'employee_id'
merged_df = pd.merge(df1, df2, on='employee_id', how='inner')

print("\n", merged_df)

#group by

# Sample DataFrame
df = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 3, 3],
    'department': ['HR', 'IT', 'IT', 'Finance', 'Finance', 'Finance'],
    'salary': [50000, 60000, 62000, 55000, 58000, 60000]
})

# Group by department and calculate mean salary
grouped_df = df.groupby('department')['salary'].mean().reset_index()

print("\n", grouped_df)






