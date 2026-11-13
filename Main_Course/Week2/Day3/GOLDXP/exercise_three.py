
"""
Exercise 3: String Module

Generate a random string of 5 characters
using uppercase and lowercase English letters.
"""

import string
import random

# Get all uppercase and lowercase English letters
all_letters = string.ascii_letters

# Create an empty string to store the random characters
random_string = ""

# Select 5 random characters and add them to the string
for i in range(5):
    letter = random.choice(all_letters)
    random_string += letter

# Display the final random string
print(random_string)
