# import pandas as pd

# data ={
#     "Name" : ["A", "B", "C", "D"],
#     "Department" : ["IT", "HR", "IT", "HR"],
#     "Salary": [5000,4000,6000,4500]
# }

# df = pd.DataFrame(data)
# print(df.groupby("Department")["Salary"].mean())

# # import pandas as pd

# # data ={
# #     "Name" : ["A", "B", "C", "D"],
# #     "Department" : ["IT", "HR", "IT", "HR"],
# #     "Salary": [5000,4000,6000,4500]
# # }

# # df = pd.DataFrame(data)
# # print(df.groupby("Department")["Salary"].agg(["mean", "sum", "max"]))

# data = {
#     "Name" : ["A", "B", "C", "D"],
#     "Department" : ["IT", "HR", "IT", "HR"],
#     "Salary": [5000,4000,6000,4500]
# }

# df = pd.DataFrame(data)
# print(df.groupby("Department")["Salary"].agg(["mean","sum", "max"]))
# df.groupby("Department")["Salary"].agg(["min", "max", "count"])

# data = {
#     "Name" : ["A", "B", "C", "D"],
#     "Department" : ["IT", "HR", "IT", "HR"],
#     "Salary" : [5000, 4000, 6000, 4500]
# }


# 📘 Full Example — Grouping + Aggregation + Print
# 🧾 Step 1: Create Data

import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [5000, 4000, 6000, 4500]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

#✅ Output:
# Original DataFrame:
#   Name Department  Salary
# 0    A         IT    5000
# 1    B         HR    4000
# 2    C         IT    6000
# 3    D         HR    4500

# 🔹 Step 2: Group + Single Aggregation (Mean)

mean_salary = df.groupby("Department")["Salary"].mean()

print("\nMean Salary per Department:")
print(mean_salary)

# ✅ Output:
# Mean Salary per Department:
# Department
# HR    4250.0
# IT    5500.0
# Name: Salary, dtype: float64


# 🔹 Step 3: Group + Multiple Aggregations

agg_result = df.groupby("Department")["Salary"].agg(["mean", "sum", "max", "min", "count"])

print("\nMultiple Aggregations:")
print(agg_result)

# ✅ Output:
# Multiple Aggregations:
#              mean    sum   max   min  count
# Department                                
# HR         4250.0   8500  4500  4000      2
# IT         5500.0  11000  6000  5000      2

# 🔹 Step 4: Clean Table Format

clean_result = df.groupby("Department")["Salary"].agg(["mean", "sum", "max"]).reset_index()
print("\nClean Table (Reset Index):")
print(clean_result)


# ✅ Output:
# Clean Table (Reset Index):  Department    mean    sum   max0         HR  4250.0   8500  45001         IT  5500.0  11000  6000

# 🔹 Step 5: Sorting

sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (High to Low):")
print(sorted_df)

# ✅ Output:
# Sorted by Salary (High to Low):  Name Department  Salary2    C         IT    60000    A         IT    50003    D         HR    45001    B         HR    4000

# 🔹 Step 6: Filtering

filtered_df = df[df["Salary"] > 4500]
print("\nFiltered (Salary > 4500):")
print(filtered_df)

# ✅ Output:
# Filtered (Salary > 4500):  Name Department  Salary0    A         IT    50002    C         IT    6000

# 🧠 Final Understanding (Everything Together)
# When you write:
# df.groupby("Department")["Salary"].agg(["mean", "sum"])
# 👉 It means:


# Split data by Department


# Take Salary column


# Calculate mean and sum


# Return results in a table



