# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.



# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).


# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.


# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.


# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.


# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.


# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.


# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.


# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.


# Step 1: Create the text class

class Text:
    def __init__(self, text):
        self.text = text

    # Step 2: Implement word_frequency Method
    def word_frequency(self, word):
        # split self.text into a list of words
        words = self.text.split()
        # Count how many times the given word in the list
        count = words.count(word)
        if count == 0:
            return None
        return count

    # STEP 3: 
    def most_common_word(self):

        # Split self.text into a list of words
        words = self.text.split()

        # Create an empty dictionary to store word frequencies
        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        # Finding the word with highest frequency
        highest_count = max(word_counts.values())

        for word, count in word_counts.items():
            if count == highest_count:
                return word

    # STEP 4: Using method unique_words
    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)

    # STEP 5: Implementing from_file Class method
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()

        return cls(content)

    
# Test Step 2
my_text = Text("HOPE wins HOPE")
print(my_text.word_frequency("HOPE"))  # Expected: 2
print(my_text.word_frequency("PUBG"))  # Expected: None

# Test Step 3
my_text = Text("HOPE wins HOPE tournaments HOPE")
print(my_text.most_common_word())  # Expected: HOPE

# Test Step 4
my_text = Text("HOPE wins HOPE tournaments wins")
print(my_text.unique_words())  # Three unique words, order may vary

# Test Step 5
my_text = Text.from_file(
    r"D:\journey-dataanalyst\Main_Course\Week2\Day4\Exercises\Exercises_one\words.txt"
)
print(my_text.text)
print(type(my_text))  # Expected: <class '__main__.Text'>
