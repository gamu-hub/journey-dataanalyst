import random # We need import random module from step 6

# Step 1: Create the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# Step 2: Create the Deck class
class Deck:
    def __init__(self):

        # Attribute to store all the cards
        self.cards = []

    #STEP 3: Create the suits and values
    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2","3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K"]
        # Start with an empty deck to reset the deck
        self.cards = []
        # Use nested loop ( A loop inside another loop to combine 
        # the suit and values)
        for suit in suits: # Taking one suit at a time
            for value in values: # Goes through all 13 values for that suit
                self.cards.append(Card(suit, value)) # Adds that card to our deck
        
        # Randomize the deck
        random.shuffle(self.cards)

    # STEP 4: Deal one card
    def deal(self):
        if self.cards:
            return self.cards.pop()
        return None

# TEST
# Create a deck
# deck = Deck()

# # Shuffle and create 52 cards
# deck.shuffle()

# print("Cards in deck:", len(deck.cards))

# # Deal one card
# card = deck.deal()

# print("Dealt card:", card.value, "of", card.suit)
# print("Cards remaining:", len(deck.cards))



        