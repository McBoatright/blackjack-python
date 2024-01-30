import random

# The Card class definition
class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value

# The Deck class definition
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 11):
                self.cards.append(Card(suit, str(value), value))
            for face_card in ['J', 'Q', 'K', 'A']:
                if face_card == 'A':
                    card_value = 11
                else:
                    card_value = 10
                self.cards.append(Card(suit, face_card, card_value))
        random.shuffle(self.cards)

# The Hand class definition
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            value += card.card_value
            if card.value == 'A':
                num_aces += 1
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

# Function to print the cards
def print_cards(cards, hidden):
    s = ""
    for card in cards:
        s = s + "\t| {} |".format(card.value)
        if hidden:
            s += "\t| * |"
    print(s)
    s = ""
    for card in cards:
        s = s + "\t|________________|"
        if hidden:
            s += "\t|________________|"
    print(s)
    print()

# Function for a single game of blackjack
def blackjack_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal the initial cards
    player_hand.add_card(deck.cards.pop())
    dealer_hand.add_card(deck.cards.pop())
    player_hand.add_card(deck.cards.pop())
    dealer_hand.add_card(deck.cards.pop())

    # Show the initial cards
    print("Player's Hand:")
    print_cards(player_hand.cards, False)
    print("Dealer's Hand:")
    print_cards(dealer_hand.cards, True)

    # Allow the player to hit or stand
    while True:
        action = input("Do you want to hit or stand? (h/s): ")
        if action.lower() == "h":
            player_hand.add_card(deck.cards.pop())
            print("Player's Hand:")
            print_cards(player_hand.cards, False)
            if player_hand.get_value() > 21:
                print("Bust! You lose.")
                break
        elif action.lower() == "s":
            break

    # Deal the dealer's cards
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.cards.pop())

    # Determine the winner
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    
    print("Player's Hand:")
    print_cards(player_hand.cards, False)
    print("Dealer's Hand:")
    print_cards(dealer_hand.cards, False)

    if player_value > 21:
        print("Bust! You lose.")
    elif dealer_value > 21 or player_value == 21 or (player_value < 21 and player_value > dealer_value):
        print("You win!")
    elif player_value == dealer_value:
        print("It's a tie!")
    else:
        print("Dealer wins.")

# Example usage
blackjack_game()