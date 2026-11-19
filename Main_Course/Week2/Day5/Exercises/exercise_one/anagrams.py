
# Import the AnagramChecker class from anagram_checker.py
from anagram_checker import AnagramChecker


# Create an AnagramChecker object
# This also loads the SOWPODS dictionary
checker = AnagramChecker()


# Display a welcome message
print("Welcome to the Anagram Checker!")


# Keep the program running until the user chooses to exit
while True:

    # Ask the user to enter a word or type 'exit'
    word = input("\nEnter a word (or type 'exit' to quit): ")

    # Remove spaces before and after the input
    word = word.strip()

    # Check if the user wants to exit
    if word.lower() == "exit":
        print("Thank you for using the Anagram Checker!")
        break

    # Check that the input contains only letters
    if not word.isalpha():
        print("Error: Please enter a single word containing only letters.")
        continue

    # Check whether the word exists in our dictionary
    if not checker.is_valid_word(word):
        print(f"Error: '{word}' is not a valid English word.")
        continue

    # Find all anagrams of the entered word
    anagrams = checker.get_anagrams(word)

    # Display the original word
    print(f"\nYour word: {word}")

    # Display the anagrams if any were found
    if anagrams:
        print("Anagrams found:")
        for anagram in anagrams:
            print(anagram)
    else:
        print("No anagrams were found.")
