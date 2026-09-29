# # import pandas as pd

# # df = pd.read_csv("students.csv")

# # print(df[df["Current"] > 80])

# # print(df[["Student", "Current"]])

# # print(df[df["Current"] > 80][["Student", "Current"]])
# # print(df)


# import pandas as pd

# # Load data
# df = pd.read_csv("students.csv")

# # Step 1: Filter (Past > 60)
# filtered = df[df["Past"] > 60]

# # Step 2: Select columns
# selected = filtered[["Student", "Past"]]

# # Step 3: Sort
# result = selected.sort_values(by="Past", ascending=False)

# # Show result
# print(result)

# #First day of learning python data analytics


# import pandas as pd

# # 1. Load data
# df = pd.read_csv("students.csv")

# # 2. Show full data
# print("Full Data:")
# print(df)

# # 3. Filter (Current > 80)
# print("\nStudents with Current > 80:")
# print(df[df["Current"] > 80])

# # 4. Select columns (Student + Current)
# print("\nSelected columns (Student, Current):")
# print(df[["Student", "Current"]])

# # 5. Combine (Filter + Select)
# print("\nFiltered + Selected:")
# print(df[df["Current"] > 80][["Student", "Current"]])

# # 6. Sort by Current (highest first)
# print("\nSorted by Current (highest first):")
# print(df.sort_values(by="Current", ascending=False))

# # 7. Full combination (Filter + Select + Sort)
# print("\nFinal Result:")
# result = df[df["Current"] > 80][["Student", "Current"]].sort_values(by="Current", ascending=False)
# print(result)

# # 8. Optional: reset index
# print("\nFinal Result (clean index):")
# print(result.reset_index(drop=True))


# import pandas as pd
# df = pd.read_csv("students.csv")
# print(df)

# print(df[df["Current"] > 80])

# print(df[df["Current"] > 80][["Student","Current"]])

# print(df.sort_values(by="Current", ascending=False))

# print(
#     df[df["Current"] > 80][["Student", "Current"]]
#     .sort_values(by="Current", ascending=False)
# )
# EXERCISE one
# 🟢 EXERCISE 1 (Easy)

# 👉 Show:

# Students with Past > 60
# Only Student + Past
# 💭 Think:
# Filter → Past > 60
# Select → Student, Past

import pandas as pd
df = pd.read_csv("students.csv")
print(df)

print(df[df["Past"]> 60])
print(df[df["Past"] > 60][["Student","Past"]])


# 🟡 EXERCISE 2 (Medium)

# 👉 Show:

# Students with Improvement > 0
# Only Student + Improvement
# Sorted highest first
# 💭 Think:
# Filter → Improvement > 0
# Select → Student, Improvement
# Sort → descending
import pandas as pd
df = pd.read_csv("students.csv")
print(df)

print(
    df[df["Current"] >= 80][["Student", "Current"]]
    .sort_values(by="Current", ascending=False)
)


 #🔴 EXERCISE 3 (Real Thinking)

# 👉 Show:

# Students with Current < 90
# Only Student + Current
# Sorted lowest first



import pandas as pd
df = pd.read_csv("Students.csv")
print(df)

print(
    df[df["Current"] <90][["Student", "Current"]]
    .sort_values(by="Current", ascending=True)
)

import pandas as pd
df = pd.read_csv("students.csv")

print(
    df[(df["Current"] >= 60) & (df["Past"] < 90)][["Student", "Past", "Current"]]
    .sort_values(by="Past", ascending=False)
    )

import pandas as pd
df = pd.read_csv("students.csv")

print(
    df[df["Current"] >60][["Student", "Current"]]
    .sort_values(by="Current", ascending=True)
)