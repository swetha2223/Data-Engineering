### **Exercise 1: Creating DataFrame from Scratch**

import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Phone"],
    "Category": ["Electronics", "Accessories", "Electronics", "Accessories", "Electronics"],
    "Price": [80000, 1500, 20000, 3000, 40000],
    "Quantity": [10, 100, 50, 75, 30]
}
df = pd.DataFrame(data)
print(df)

### **Exercise 2: Basic DataFrame Operations**
#1. Display the first 3 rows of the DataFrame.
print(df.iloc[0:3])


# the column names and index of the DataFrame.
print(df.columns)
print(df.index)

#3. Display a summary of statistics (mean, min, max, etc.) for the numeric columns in the DataFrame.
print(df.describe())

### **Exercise 3: Selecting Data**
print(df[["Product", "Price"]])
print(df[df["Category"] == "Electronics"])

### **Exercise 4: Filtering Data**
# 1. Filter the DataFrame to display only the products with a price greater than `10,000`.
print(df[df["Price"] > 10000])

# 2. Filter the DataFrame to show only products that belong to the `"Accessories"` category and have a quantity greater than `50`.
print(df[(df["Category"] == "Accessories") & (df["Quantity"] > 50)])

### **Exercise 5: Adding and Removing Columns**
# 1. Add a new column `"Total Value"` which is calculated by multiplying `"Price"` and `"Quantity"`.
# 2. Drop the `"Category"` column from the DataFrame and print the updated DataFrame.

df["Total Value"] = df["Price"] * df["Quantity"]
print(df)

df_new = df.drop(columns=["Category"])
print(df_new)

### **Exercise 6: Sorting Data**
# 1. Sort the DataFrame by `"Price"` in descending order.
# 2. Sort the DataFrame by `"Quantity"` in ascending order, then by `"Price"` in descending order (multi-level sorting).

print(df.sort_values("Price", ascending=False))
print(df.sort_values(["Quantity", "Price"], ascending=[True, False]))

### **Exercise 7: Grouping Data**
# 1. Group the DataFrame by `"Category"` and calculate the total quantity for each category.
df_grouped = df.groupby("Category")["Quantity"].sum()
print(df_grouped)
# 2. Group by `"Category"` and calculate the average price for each category.
df_grouped = df.groupby("Category")["Quantity"].mean()
print(df_grouped)

### **Exercise 8: Handling Missing Data**
# 1. Introduce some missing values in the `"Price"` column by assigning `None` to two rows.
# 2. Fill the missing values with the mean price of the available products.
# 3. Drop any rows where the `"Quantity"` is less than `50`.

df.loc[1, "Price"] = None
df.loc[3, "Price"] = None
print(df)

df["Price"].fillna(df["Price"].mean(), inplace=True)
print(df)

df.drop(df[df["Quantity"] < 50].index, inplace=True)
print(df)

### **Exercise 9: Apply Custom Functions**
# 1. Apply a custom function to the `"Price"` column that increases all prices by 5%.
# 2. Create a new column `"Discounted Price"` that reduces the original price by 10%.
df["Price"] = df["Price"] * 1.05
print(df)
df["Discounted Price"] = df["Price"] * 0.9
print(df)

### **Exercise 10: Merging DataFrames**
#1. Create another DataFrame with columns `"Product"` and `"Supplier"`, and merge it with the original DataFrame based on the `"Product"` column.
suppliers = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Phone"],
    "Supplier": ["Supplier1", "Supplier2", "Supplier3", "Supplier4", "Supplier5"]
})
print(pd.merge(df, suppliers, on="Product"))

### **Exercise 11: Pivot Tables**
#1. Create a pivot table that shows the total quantity of products for each category and product combination.

print(pd.pivot_table(df, index="Category", columns="Product", values="Quantity", aggfunc="sum"))

### **Exercise 12: Concatenating DataFrames**
# 1. Create two separate DataFrames for two different stores with the same columns (`"Product"`, `"Price"`, `"Quantity"`).
# 2. Concatenate these DataFrames to create a combined inventory list.

store1 = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor"],
    "Price": [80000, 1500, 20000],
    "Quantity": [10, 100, 50]
})
store2 = pd.DataFrame({
    "Product": ["Keyboard", "Phone", "Laptop"],
    "Price": [3000, 40000, 85000],
    "Quantity": [75, 30, 20]
})
print(pd.concat([store1, store2]))

### **Exercise 13: Working with Dates**
# 1. Create a DataFrame with a `"Date"` column that contains the last 5 days starting from today.
# 2. Add a column `"Sales"` with random values for each day.
# 3. Find the total sales for all days combined.

dates = pd.date_range("2024-08-28", periods=5)
sales = [100, 200, 300, 400, 500]
df = pd.DataFrame({"Date": dates, "Sales": sales})
print(df)
print("total sales:", df["Sales"].sum())

### **Exercise 14: Reshaping Data with Melt**
# 1. Create a DataFrame with columns `"Product"`, `"Region"`, `"Q1_Sales"`, `"Q2_Sales"`.
# 2. Use `pd.melt()` to reshape the DataFrame so that it has columns `"Product"`, `"Region"`, `"Quarter"`, and `"Sales"`.

data = {
    "Product": ["Laptop", "Mouse", "Monitor"],
    "Region": ["North", "South", "East"],
    "Q1_Sales": [100, 200, 300],
    "Q2_Sales": [400, 500, 600]
}
df = pd.DataFrame(data)
df_melted = pd.melt(df, id_vars=["Product", "Region"], value_vars=["Q1_Sales", "Q2_Sales"], var_name="Quarter", value_name="Sales")
print(df_melted)

### **Exercise 15: Reading and Writing Data**
# 1. Read the data from a CSV file named `products.csv` into a DataFrame.
# 2. After performing some operations (e.g., adding a new column or modifying values), write the DataFrame back to a new CSV file named `updated_products.csv`.

df = pd.read_csv("products.csv")
print("\n", df)

df['Discounted Price'] = df['Price'] * 0.9

df.to_csv('updated_products.csv', index=False)

### **Exercise 16: Renaming Columns**
# 1. Given a DataFrame with columns `"Prod"`, `"Cat"`, `"Price"`, `"Qty"`, rename the columns to `"Product"`, `"Category"`, `"Price"`, and `"Quantity"`.
# 2. Print the renamed DataFrame.

data = {
    "Prod": ["Laptop", "Mouse", "Monitor", "Keyboard", "Phone"],
    "Cat": ["Electronics", "Accessories", "Electronics", "Accessories", "Electronics"],
    "Price": [80000, 1500, 20000, 3000, 40000],
    "Qty": [10, 100, 50, 75, 30]
}
df = pd.DataFrame(data)

df_new = df.rename(columns={
    "Prod": "Product",
    "Cat": "Category",
    "Qty": "Quantity"
})
print("\n", df_new)

### **Exercise 17: Creating a MultiIndex DataFrame**
# 1. Create a DataFrame using a MultiIndex (hierarchical index) with two levels: `"Store"` and `"Product"`. The DataFrame should have columns `"Price"` and `"Quantity"`, representing the price and quantity of products in different stores.
# 2. Print the MultiIndex DataFrame.
data = {
    ("Store A", "Laptop"): {"Price": 80000, "Quantity": 10},
    ("Store A", "Mouse"): {"Price": 1500, "Quantity": 100},
    ("Store B", "Monitor"): {"Price": 20000, "Quantity": 50},
    ("Store B", "Keyboard"): {"Price": 3000, "Quantity": 75},
    ("Store C", "Phone"): {"Price": 40000, "Quantity": 30}
}
df = pd.DataFrame(data).T
print("\n", df)

### **Exercise 18: Resample Time-Series Data**
# 1. Create a DataFrame with a `"Date"` column containing a range of dates for the past 30 days and a `"Sales"` column with random values.
# 2. Resample the data to show the total sales by week.
import pandas as pd
import numpy as np


# Create a DataFrame with a "Date" column and a "Sales" column
date_rng = pd.date_range(end=pd.Timestamp.today(), periods=31, freq='D')
df_sales = pd.DataFrame(date_rng, columns=['Date'])
df_sales['Sales'] = np.random.randint(1000, 10000, size=(31))
print(df_sales)
weekly_sales = df_sales.resample('W', on='Date').sum()
print(weekly_sales)

### **Exercise 19: Handling Duplicates**
# 1. Given a DataFrame with duplicate rows, identify and remove the duplicate rows.
# 2. Print the cleaned DataFrame.
df_duplicates = pd.DataFrame({
    "Product": ['Laptop', 'Phone', 'Monitor', 'Laptop', 'Phone'],
    "Price": [80000, 40000, 20000, 80000, 40000],
    "Quantity": [10, 30, 50, 10, 30]
})
df_cleaned = df_duplicates.drop_duplicates()
print(df_cleaned)


# Exercise 20: Correlation Matrix
# 1. Create a DataFrame with numeric data representing different features (e.g., "Height", "Weight", "Age", "Income").
# 2. Compute the correlation matrix for the DataFrame.
# 3. Print the correlation matrix.

data = {
    "Height": [175, 180, 165, 170, 185, 178, 168, 172, 181, 177],
    "Weight": [65, 70, 55, 60, 75, 68, 58, 62, 72, 69],
    "Age": [25, 30, 22, 28, 35, 27, 24, 29, 32, 26],
    "Income": [50000, 60000, 45000, 55000, 70000, 58000, 48000, 57000, 62000, 59000]
}
df = pd.DataFrame(data)
corr_matrix = df.corr()
print(corr_matrix)

### **Exercise 21: Cumulative Sum and Rolling Windows**
np.random.seed(0)
df = pd.DataFrame(np.random.randint(100, 500, size=30), index=pd.date_range(start='2024-08-01', periods=30), columns=['Sales'])
df['Cumulative Sales'] = df['Sales'].cumsum()
df['Rolling Avg'] = df['Sales'].rolling(7).mean()
print(df)

### **Exercise 22: String Operations**
# 1. Create a DataFrame with a column `"Names"` containing values like `"John Doe"`, `"Jane Smith"`, `"Sam Brown"`.
# 2. Split the `"Names"` column into two separate columns: `"First Name"` and `"Last Name"`.
# 3. Convert the `"First Name"` column to uppercase.

data = {"Names": ["Rahul Kumar", "Priya Sharma", "Rajesh Patel"]}
df = pd.DataFrame(data)
df[["First Name", "Last Name"]] = df["Names"].str.split(" ", expand=True)
df["First Name"] = df["First Name"].str.upper()
print(df)

# ### **Exercise 23: Conditional Selections with `np.where`**
# 1. Create a DataFrame with columns `"Employee"`, `"Age"`, and `"Department"`.
# 2. Create a new column `"Status"` that assigns `"Senior"` to employees aged 40 or above and `"Junior"` to employees below 40 using `np.where()`.

data = {
    "Employee": ["Rahul", "Priya", "Rajesh", "Sonia", "Vikram"],
    "Age": [35, 28, 45, 32, 42],
    "Department": ["Sales", "Marketing", "IT", "HR", "Finance"]
}
df = pd.DataFrame(data)
df["Status"] = np.where(df["Age"] >= 40, "Senior", "Junior")
print(df)

# ### **Exercise 24: Slicing DataFrames**
# 1. Given a DataFrame with data on `"Products"`, `"Category"`, `"Sales"`, and `"Profit"`, slice the DataFrame to display:  The first 10 rows.  All rows where the `"Category"` is `"Electronics"`.
#  Only the `"Sales"` and `"Profit"` columns for products with sales greater than 50,000.

data = {
    "Products": ["Phone", "Laptop", "TV", "Computer", "Tablet", "Headphones", "Speaker", "Mouse", "Keyboard", "Camera", "Printer", "Scanner"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Accessories"],
    "Sales": [80000, 120000, 90000, 100000, 70000, 60000, 50000, 40000, 30000, 110000, 20000, 15000],
    "Profit": [20000, 30000, 25000, 22000, 18000, 15000, 12000, 10000, 8000, 28000, 4000, 3000]
}
df = pd.DataFrame(data)
print(df.head(10))

print(df[df["Category"] == "Electronics"])
print(df.loc[df["Sales"] > 50000, ["Sales", "Profit"]])

### **Exercise 25: Concatenating DataFrames Vertically and Horizontally**
# 1. Create two DataFrames with identical columns `"Employee"`, `"Age"`, `"Salary"`, but different rows (e.g., one for employees in `"Store A"` and one for employees in `"Store B"`).
# 2. Concatenate the DataFrames vertically to create a combined DataFrame.
# 3. Now create two DataFrames with different columns (e.g., `"Employee"`, `"Department"` and `"Employee"`, `"Salary"`) and concatenate them horizontally based on the common `"Employee"` column.
df_store_a = pd.DataFrame({
    "Employee": ["John", "Anna", "Peter"],
    "Age": [35, 28, 45],
    "Salary": [50000, 60000, 70000]
})

df_store_b = pd.DataFrame({
    "Employee": ["Linda", "Phil", "Raj"],
    "Age": [32, 42, 38],
    "Salary": [55000, 65000, 75000]
})

df_combined = pd.concat([df_store_a, df_store_b])
print(df_combined)
df_employee_info = pd.DataFrame({
    "Employee": ["John", "Anna", "Peter", "Linda", "Phil", "Raj"],
    "Department": ["Sales", "Marketing", "IT", "HR", "Finance", "Operations"]
})
df_employee_salary = pd.DataFrame({
    "Employee": ["John", "Anna", "Peter", "Linda", "Phil", "Raj"],
    "Salary": [50000, 60000, 70000, 55000, 65000, 75000]
})
df_horizontal = pd.merge(df_employee_info, df_employee_salary, on="Employee")
print(df_horizontal)

# ### **Exercise 26: Exploding Lists in DataFrame Columns**
# 1. Create a DataFrame with a column `"Product"` and a column `"Features"` where each feature is a list (e.g., `["Feature1", "Feature2"]`).
# 2. Use the `explode()` method to create a new row for each feature in the list, so each product-feature pair has its own row.
df = pd.DataFrame({
    "Product": ["Product A", "Product B", "Product C"],
    "Features": [["Feature1", "Feature2"], ["Feature3", "Feature4"], ["Feature5", "Feature6"]]
})
df_exploded = df.explode("Features")
print("\n", df_exploded)


# ### **Exercise 27: Using `.map()` and `.applymap()`**
# 1. Given a DataFrame with columns `"Product"`, `"Price"`, and `"Quantity"`, use `.map()` to apply a custom function to increase `"Price"` by 10% for each row.
# 2. Use `.applymap()` to format the numeric values in the DataFrame to two decimal places.

df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Price": [100, 200, 300]
})
df["Price"] = df["Price"].map(lambda x: x * 1.1)
df = df.applymap(lambda x: "{:.2f}".format(x) if isinstance(x, float) else x)
print(df)

# ### **Exercise 28: Combining `groupby()` with `apply()`**
# 1. Create a DataFrame with `"City"`, `"Product"`, `"Sales"`, and `"Profit"`.
# 2. Group by `"City"` and apply a custom function to calculate the profit margin (Profit/Sales) for each city.

df = pd.DataFrame({
    "City": ["New York", "New York", "Chicago", "Chicago", "Los Angeles", "Los Angeles"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Sales": [100, 200, 150, 250, 120, 220],
    "Profit": [20, 40, 30, 50, 24, 44]
})
def calculate_profit_margin(group):
    return group["Profit"].sum() / group["Sales"].sum()
df_grouped = df.groupby("City").apply(calculate_profit_margin).reset_index()
df_grouped.columns = ["City", "Profit Margin"]
print(df_grouped)

# exercise 29
df_csv = pd.read_csv("data1.csv")
df_json = pd.read_json("data2.json")
data3 = {
    "ID": [1, 2, 3],
    "Name": ["John", "Anna", "Peter"]
}
df_dict = pd.DataFrame(data3)
df_consolidated = pd.merge(df_csv, df_json, on="ID")
df_consolidated = pd.merge(df_consolidated, df_dict, on="ID")
print(df_consolidated)


### **Exercise 30: Dealing with Large Datasets**
# 1. Create a large DataFrame with 1 million rows, representing data on `"Transaction ID"`, `"Customer"`, `"Product"`, `"Amount"`, and `"Date"`.
# 2. Split the DataFrame into smaller chunks (e.g., 100,000 rows each), perform a simple analysis on each chunk (e.g., total sales), and combine the results.

df = pd.DataFrame({
    "Amount": np.random.randint(1, 100, 1000000)
})
chunk_size = 100000
total_sales = sum(chunk["Amount"].sum() for chunk in [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)])
print("Total Sales:", total_sales)






















