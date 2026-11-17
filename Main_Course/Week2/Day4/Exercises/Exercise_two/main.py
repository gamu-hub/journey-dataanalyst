# ### Exercise 2: Working with JSON

# **Goal:** Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.

# **Key Python Topics:**

# - JSON parsing (`json.loads()`)
# - JSON serialization (`json.dump()`)
# - Dictionaries
# - File handling (`open()`)
# **Instructions:**
# Using the follow code:
# ```
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"


# 1. Access the nested “salary” key.
# 2. Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: `"birth_date": "YYYY-MM-DD"`.
# 3. Save the modified JSON to a file.

# **Step 1: Load the JSON string**

# - Import the `json` module.
# - Use `json.loads()` to parse the JSON string into a Python dictionary.
# **Step 2: Access the nested “salary” key**

# - Access the “salary” key using nested dictionary access (e.g., `data["company"]["employee"]["payable"]["salary"]`).
# - Print the value of the “salary” key.
# **Step 3: Add the “birth_date” key**

# - Add a new key-value pair to the “employee” dictionary: `"birth_date": "YYYY-MM-DD"`.
# - Replace `"YYYY-MM-DD"` with an actual date.

# **Step 4: Save the JSON to a file**

# - Open a file in write mode (`"w"`).
# - Use `json.dump()` to write the modified dictionary to the file in JSON format.
# - Use the `indent` parameter to make the JSON file more readable.


import json

sampleJson = """{
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""

# Step 1: Load JSON
data = json.loads(sampleJson)

# Step 2: Access salary
salary = data["company"]["employee"]["payable"]["salary"]
print(salary)

# Step 3: Add birth date
data["company"]["employee"]["birth_date"] = "1995-06-15"

# Step 4: Save modified JSON
# with open("employee.json", "w") as file:

# I copy paste the path because this help me organise
#  or make the new file employee.json to the same folder.

with open("Main_Course/Week2/Day4/Exercises/Exercise_two/employee.json", "w") as file:
    json.dump(data, file, indent=4)