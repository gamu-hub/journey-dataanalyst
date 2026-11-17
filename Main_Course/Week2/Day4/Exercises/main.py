# Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a 
# specified length from a word list.


# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation


# Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.


# Step 1: Create the get_words_from_file function

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.


# Step 2: Create the get_random_sentence function

# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.


# Step 3: Create the main function

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and 
# print the generated sentence.


import random

# Dataset path
WORDS_FILE = "Main_Course/Week2/Day4/Exercises/words.txt"


# STEP 1: Read words from file
def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()

    return words


# STEP 2: Generate random sentence
def get_random_sentence(length):

    # 1. Get the words from the file
    words = get_words_from_file(WORDS_FILE)

    # 2. Create an empty list for selected words
    selected_words = []


    # 3. Repeat length times
    for i in range(length):

        # Select a random word
        random.choice(words)

        # Pick a random word then add it to our list
        selected_words.append(random.choice(words))


    # 4. Join all selected words into one sentence
    sentence = " ".join(selected_words)

    # 5. Convert the sentence to lowercase
    sentence = sentence.lower()

    # 6. Return the sentence
    return sentence

print(get_random_sentence(3))