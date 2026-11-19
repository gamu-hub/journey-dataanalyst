
# Step 1: Import AnagramChecker from anagram_checker.py
from anagram_checker import AnagramChecker


# Step 2: Create an instance of AnagramChecker
# The dictionary is loaded when the object is created
checker = AnagramChecker()


# Step 3: Create a menu loop
# The menu keeps appearing until the user chooses to exit
while True:
    print("\n--- ANAGRAM CHECKER ---")
    print("1. Enter a word")
    print("2. Exit")

    # Get the user's menu selection
    choice = input("Choose an option (1 or 2): ")

    # Exit the program
    if choice == "2":
        print("Thank you for using Anagram Checker!")
        break

    # User chooses to enter a word
    elif choice == "1":

        # Get the word from the user
        word = input("Enter a word: ")

        # Remove whitespace from the beginning and end
        word = word.strip()

        # Step 4: Validate the user's input

        # Check that the user entered only one word
        words = word.split()

        if len(words) != 1:
            print("Error: Please enter only one word.")
            continue

        # Check that the word contains only alphabetic characters
        if not word.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue

        # Check whether the word exists in the dictionary
        if not checker.is_valid_word(word):
            print(f"Error: '{word}' is not a valid English word.")
            continue

        # Find all possible anagrams
        anagrams = checker.get_anagrams(word)

        # Display the results in a formatted message
        print("\n------------------------------")
        print(f'YOUR WORD: "{word.upper()}"')
        print("This is a valid English word.")

        if anagrams:
            print("Anagrams for your word:", ", ".join(anagrams))
        else:
            print("No anagrams were found.")

        print("------------------------------")

    # Handle any menu choice other than 1 or 2
    else:
        print("Invalid choice. Please choose 1 or 2.")
