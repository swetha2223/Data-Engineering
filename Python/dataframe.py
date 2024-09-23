import pandas as pd

# creating a Dataframes from a dictionary with indian names


data = {
    "Name": ["Amit", "Priya", "Vikram", "Neha", "Ravi"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Pune"]
}

df = pd.DataFrame(data)

print(df)

# access data from data frame
# one column
print(df["Name"])

# accessing multiple column
print(df[["Name", "Age"]])

# accessing first row
print(df.iloc[0])

#filter rows where age is greater than 30
filtered_df = df[df["Age"]>30]
print(filtered_df)

#Adding a new column 'Salary'
df["Salary"] = [50000, 60000, 76000, 80000, 90000]
print(df)

#sorting by age
sorted_df = df.sort_values(by="Age",ascending=False)
print(sorted_df)

#rename the 'name' column to 'fullname' and 'age' to 'years'
df_renamed = df.rename(columns={"Name":"Full name","Age":"Years"})
print(df_renamed)

#drop the 'City' column
df_dropped = df.drop(columns=["City"])
print(df_dropped)


# drop the row at index 2 (vikram)
df_drop_row =  df.drop(index=2)
print(df_drop_row)

# create a new column "seniority' based on the age

df['seniority'] = df['Age'].apply(lambda x: 'senior' if x >= 35 else 'junior')

#group by 'city' and calculate the average salary in each city

df_grouped = df.groupby("City")["Salary"].mean()
print(df_grouped)

#apply a customer function to the 'salary' column to add a 10% bonus


def add_bonus(Salary):
    return Salary * 1.10

df['Salary_with_Bonus'] = df['Salary'].apply(add_bonus)
print(df)

# create another dataframe
df_new = pd.DataFrame({
    "Name": ["Amit", "Priya", "Ravi"],
    "Bonus_New": [5000, 6000, 7000]
})

df_merged = pd.merge(df, df_new, on="Name", how="left")
print(df_merged)


# concat - they must have same data so that only it applicable
# Create the second DataFrame
df_new = pd.DataFrame({
    "Name": ["Sonia", "Rahul"],
    "Age": [29, 31],
    "City": ["Kolkata", "Hyderabad"],
    "Salary": [58000, 63000]
})

# Concatenate the two DataFrames
df_concat = pd.concat([df, df_new], ignore_index=True)
print(df_concat)

# people who more than 50000 Salary
df_more_salary = df[df['Salary'] > 50000]
print(df_more_salary)

# people name starts with a
a_name_people = df[df['Name'].str.startswith('A')]
print(a_name_people)








