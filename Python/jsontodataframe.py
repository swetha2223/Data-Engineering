import pandas as pd

#Load the json file into dataframe

df = pd.read_json('employees.json')

print(df)

# add new column "bonus" which is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10
print(df)

# save the updated Dataframe to anew JSON file
df.to_json('employees_with_bonus,join', orient='records', lines=True)

