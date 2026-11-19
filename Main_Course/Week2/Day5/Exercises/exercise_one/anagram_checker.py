class AnagramChecker:

    # STEP 1: Create the class and load the dictionary
    def __init__(self):

        # Create an empty set to store words
        self.words = set()

        #Open the dictionary file
        with open("sowpods.txt", "r") as file:

            # Read the file line by line
            for line in file:

                # Clean the word
                word = line.strip().lower()

                # Add the word to our set
                self.words.add(word)
                

    # STEP 2: Check whether a word exists in our dictionary
    def is_valid_word(self, word):
        return word.lower() in self.words

    # STEP 3: Check if two words are anagrams
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    # STEP 4: Find all anagrams:

    def get_anagrams(self, word):

        # Create an empty list
        anagrams = []

        # Loop through all the dictinary words
        for candidate in self.words:

            # Check if candidate is an anagram
            if self.is_anagram(word, candidate):

                # Don't include the original word
                if candidate != word.lower():
                    anagrams.append(candidate)
        # Return the list
        return anagrams


# ==================================
# TESTING - DI WEEK 2 MINI PROJECT
# ==================================

# Create an AnagramChecker object
checker = AnagramChecker()


# DI STEP 1: Test dictionary loading

print("===== STEP 1: DICTIONARY =====")

print(len(checker.words))


# DI STEP 2: Test is_valid_word()

print("===== STEP 2: VALID WORD =====")

print(checker.is_valid_word("meat"))
print(checker.is_valid_word("MEAT"))
print(checker.is_valid_word("xyzabc"))


# DI STEP 3: Test is_anagram()

print("===== STEP 3: ANAGRAM CHECK =====")

print(checker.is_anagram("meat", "team"))
print(checker.is_anagram("listen", "silent"))
print(checker.is_anagram("hello", "world"))
print(checker.is_anagram("MEAT", "Team"))

# DI STEP 4: Test get_anagrams Method
print("===== STEP 4: GET ANAGRAM =====")
print(checker.get_anagrams("meat"))