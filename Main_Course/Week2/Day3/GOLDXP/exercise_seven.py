# Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in 
# a list of dictionaries.
# Read more about this module HERE



# Key Python Topics:

# faker module
# Dictionaries
# Lists
# Loops


# Instructions:

# Install the faker module and use it to create a list of dictionaries,
#  where each dictionary represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module

# Step 3: Create an empty list of users

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list


"""
Exercise 7: Faker Module

Generate fake user data and store it in a list of dictionaries.
"""

from faker import Faker

# Create a Faker instance
fake = Faker()

# Create an empty list to store users
users = []


def add_users(number_of_users):
    """Generate the requested number of fake users."""

    # Loop through the requested number of users
    for i in range(number_of_users):

        # Create a dictionary containing fake user information
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }

        # Add the user dictionary to the users list
        users.append(user)


# Generate 5 fake users
add_users(5)

# Display the list of users
print(users)

