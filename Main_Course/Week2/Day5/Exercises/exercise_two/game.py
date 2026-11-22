# Import the random module for step 3:
import random

# Step 1: Create the Game class
class Game:

    # Step 2: Get the user's choice
    def get_user_item(self):

        # Keep asking untill the user enters a valid choice
        while True:
            user_item = input("Choose rock, paper, or scissors: ")

            # Convert the input to lowercase
            user_item = user_item.lower().strip()

             # Check if the choice is valid
            if user_item not in ["rock", "paper", "scissors"]:
                print("Invalid choice. Please try again.")

            else:
                return user_item

    # STEP 3: Implement get_computer_item() Method
    def get_computer_item(self):
        # list of available choices
        items = ["rock", "paper", "scissors"]

        # Randomly select one item
        computer_item = random.choice(items)

        # Return the computer's choice
        return computer_item
    
    # STEP 4: Implement Method get_game_result
    def get_game_result(self, user_item, computer_item):

        # Check if both choices are the same
        if user_item == computer_item:
            return "draw"

        # Check if the user wins
        if (user_item == "rock" and computer_item == "scissors") or \
        (user_item == "paper" and computer_item == "rock") or \
        (user_item == "scissors" and computer_item == "paper"):

            return "win"

        # If neither draw nor win, the user losses
        return "loss"
    
    # Step 5: Play one round of the game
    def play(self):
        # Get user's choice
        user_item = self.get_user_item()

        # Get the computer's choice
        computer_item = self.get_computer_item()

        # Determine the game result
        result = self.get_game_result(user_item, computer_item)

        # Display the choices and result
        print("Your choice:", user_item)
        print("Computer's choice:", computer_item)
        print("Result:", result)

        # Return the result
        return result

# ==================================
# TESTING - Rock, paper or scissors
# ==================================

# print("=== STEP 2 TEST ===")
# game = Game()
# choice = game.get_user_item()
# print("You selected:", choice)

# print("=== STEP 3 TEST ===")

# print(game.get_computer_item())
# print(game.get_computer_item())
# print(game.get_computer_item())

print("=== STEP 4 TEST ===")
game = Game()
result = game.play()

print("Returned result:", result)