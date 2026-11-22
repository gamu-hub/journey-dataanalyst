
# Step 6: Import the Game class from game.py
from game import Game


# Step 6: Display the menu and get the user's choice
def get_user_menu_choice():

    # Keep displaying the menu until the user enters a valid choice
    while True:
        print("\n===== ROCK PAPER SCISSORS =====")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")

        # Get the user's menu choice
        choice = input("Choose an option (1, 2, or 3): ").strip()

        # Check if the choice is valid
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


# Step 7: Display the final results
def print_results(results):
    """Display the final scores and thank the user."""

    print("\n===== FINAL GAME SUMMARY =====")

    # Display all scores on one line
    print(
        f"Wins: {results['win']}, "
        f"Losses: {results['loss']}, "
        f"Draws: {results['draw']}"
    )

    print("\nThank you for playing!")


# Step 8: Main function
def main():

    # Create a dictionary to track the game results
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    # Keep showing the menu until the user chooses to quit
    while True:

        # Get the user's menu choice
        choice = get_user_menu_choice()

        # Option 1: Play a new game
        if choice == "1":

            # Create a Game object
            game = Game()

            # Play one round and receive the result
            result = game.play()

            # Update the score in the dictionary
            results[result] += 1

        # Option 2: Show current scores
        elif choice == "2":

            print("\n===== CURRENT SCORES =====")
            print("Wins:", results["win"])
            print("Losses:", results["loss"])
            print("Draws:", results["draw"])

        # Option 3: Quit the game
        elif choice == "3":

            # Display the final results
            print_results(results)

            # Exit the menu loop
            break


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
