import pandas as pd
#load the CSV fiDataFrame

df = pd.read_csv('employee.csv')

print (df)

#Display the first three rows
print(df.head(3))

#show summary information about the DataFrame
print(df.info())

#display summary statistics of numeric columns
print(df.describe())

# filtering row where salary is greater than 80000
high_salary_df = df[df['Salary'] > 80000]
print(high_salary_df)


#sorted by age in descending
sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)




