# import pandas as pd

# df1 = pd.DataFrame({
#     "Name": ["A", "B"],
#     "Score" : [80,90]
# })

# df2 = pd.DataFrame({
#     "Name": ["C", "D"],
#     "Score" : [70,60]
# })

# result = pd.concat([df1, df2])
# print(result)

# result2 = pd.concat([df1, df2], ignore_index=True)
# print(result2)

# 🔹 1. Vertical Concat (axis=0) — stacking rows
# 🧠 What’s happening
# You put df2 UNDER df1
# Columns stay the same
# Index is kept as-is (that’s why it repeats)
# 👉 Think:
# df1
# A
# B
# +
# df2
# C
# D
# =
# A
# B
# C
# D   (stacked)
# 🔴 Why index repeats

# Because Pandas is basically doing:

# df1 index: 0,1
# df2 index: 0,1

# → combine → 0,1,0,1

# 👉 It does NOT reset unless you say so.

# 🔹 2. Fixing index (ignore_index=True)
# 7
# 🧠 What changes
# Pandas throws away old indexes
# Creates new clean sequence: 0,1,2,3
# 🔹 3. Horizontal Concat (axis=1) — side by side
# 6
# 🧠 What’s happening
# Now we combine columns
# Rows are matched by index

# 👉 Think:

# df1        df2
# A   80     C   70
# B   90     D   60

# → combine →

# A 80 | C 70
# B 90 | D 60
# 🔴 Important rule (THIS is key)

# 👉 Horizontal concat = match by index

# If indexes don’t match → you get NaN

# 🔥 Final simple memory trick
# axis=0 → ⬇️ stack down (rows)
# axis=1 → ➡️ stick side (columns)


# import pandas as pd

# df1 = pd.DataFrame({
#     "Name": ["John", "Emma"],
#     "Score": [85, 90]
# })

# df2 = pd.DataFrame({
#     "Name": ["Liam", "Olivia"],
#     "Score": [75, 95]
# })

# result = pd.concat([df1, df2])

# 🧪 Exercise Set – Day 6 (concat mastery)
# 🔹 Exercise 1 — Basic Vertical Concat
# import pandas as pd

# df1 = pd.DataFrame({
#     "Name": ["John", "Emma"],
#     "Score": [85, 90]
# })

# df2 = pd.DataFrame({
#     "Name": ["Liam", "Olivia"],
#     "Score": [75, 95]
# })
# 👉 Tasks:
# 1. Combine them vertically
# 2. Fix the index


# import pandas as pd
# df1 = pd.DataFrame({
#     "Name" : ["John", "Emma"],
#     "Score" : [85, 90]
# })

# df2 = pd.DataFrame({
#     "Name" : ["Liam", "Olivia"],
#     "Score" : [75, 95]
# })

# result = pd.concat([df1, df2])
# print (result)

# result_clean = pd.concat([df1, df2], ignore_index=True)
# print(result_clean)


# 🧪 Exercise 3 — Horizontal Concat
# ✅ Step 1: Create DataFrames


import pandas as pd

df1 = pd.DataFrame({
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "Score": [100, 200]
})

result = pd.concat([df1, df2], axis=1)

print(result)
