import pandas as pd




# Creating a new dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rajesh", "Meena", "Suresh", "Anita", "Vijay", "Neeta"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Age": [29, 35, 45, 32, 50, 28],
    "Salary": [70000, 85000, 95000, 64000, 120000, 72000],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

#Exercise 1: Rename Columns
#Rename the "Salary" column to "Annual Salary" and "City" to "Location". Print the updated DataFrame.
df_renamed = df.rename(columns={"Salary": "Annual Salary","City":"Location"})
print("Renamed Data")
print(df_renamed)

# Exercise 2: Drop Columns
# Drop the "Location" column from the DataFrame. # Print the DataFrame after dropping the column.
df_dropped = df_renamed.drop(columns=["Location"])
print("\n")
print(df_dropped)

# Exercise 3: Drop Rows
# Drop the row where "Name" is "Suresh".  Print the updated DataFrame.
df_drop_row = df_renamed.drop(index=df_renamed[df_renamed["Name"] == "Suresh"].index)
print("\n")
print(df_drop_row)



# Exercise 4
df['Salary'].fillna((df['Salary'].mean()), inplace=True)

# Print the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)



# Exercise 5: Create Conditional Columns
# Create a new column "Seniority" that assigns "Senior" to employees aged 40 or above and "Junior" to employees younger than 40. Print the updated DataFrame.
df_renamed['seniority'] = df_renamed['Age'].apply(lambda x: 'senior' if x >= 40 else 'junior')
print("\n")
print(df_renamed)

# Exercise 6: Grouping and Aggregation
# Group the DataFrame by "Department" and calculate the average salary in each department. Print the grouped DataFrame.

df_grouped = df_renamed.groupby("Department")["Annual Salary"].mean()
print("\n")
print(df_grouped)


