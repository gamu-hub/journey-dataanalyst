# import pandas as pd

# df = pd.read_csv("students.csv")

# print(df[df["Current"] > 80])

# print(df[["Student", "Current"]])

# print(df[df["Current"] > 80][["Student", "Current"]])
# print(df)


import pandas as pd

# Load data
df = pd.read_csv("students.csv")

# Step 1: Filter (Past > 60)
filtered = df[df["Past"] > 60]

# Step 2: Select columns
selected = filtered[["Student", "Past"]]

# Step 3: Sort
result = selected.sort_values(by="Past", ascending=False)

# Show result
print(result)
#First day of learning python data analytics.