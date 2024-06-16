import random
from Card import Card


class Player:
    def __init__(self, name, score, cards_taken, games_played):
        self.name = name
        self.score = score
        self.cards_taken = cards_taken
        self.games_played = games_played
        self.hand = []
        self.trump = None
        self.say = 0
        self.rounds_won = 0

    def __repr__(self):
        return f"Player(name={self.name}, score={self.score}, games_played={self.games_played}, hand={self.hand}, trump={self.trump}, say={self.say}, rounds_won={self.rounds_won})"

    def add_cards_to_hand(self, cards):
        self.hand.extend(cards)

    def choose_card(self, leading_color, trump):
        while True:
            print(f"Your hand: {self.hand}")
            card_input = input(f"{self.name}, choose a card to play (e.g., 9H for 9 of Hearts, or JokerRed, JokerBlack): ").strip().upper()

            # Handle Joker input separately
            if card_input == "JOKERRED" or card_input == "JOKERBLACK":
                value = "JOKER"
                color = card_input[5:]
            elif len(card_input) >= 2 and (card_input[:-1].isdigit() or card_input[:-1] in ["A", "J", "Q", "K"]):
                value_str = card_input[:-1]
                color = card_input[-1]

                try:
                    value = int(value_str) if value_str.isdigit() else value_str
                except ValueError:
                    print("Invalid card value. Please try again.")
                    continue
            else:
                print("Invalid input. Please enter a card in the format value+color (e.g., 9H or JokerRed, JokerBlack).")
                continue

            chosen_card = Card(value, color)
            # Check if the chosen card is in the player's hand
            if chosen_card in self.hand:
                if leading_color:
                    # Check if the player has the leading color or trump
                    has_leading_color = any(card.color == leading_color for card in self.hand)
                    has_trump = any(card.color == trump for card in self.hand)
                    # Problem here 2nd joker cant take over 1st one
                    if chosen_card.color == leading_color or chosen_card.color == trump or chosen_card.value == "JOKER":
                        self.hand.remove(chosen_card)
                        return chosen_card
                    elif not has_leading_color and not has_trump:
                        self.hand.remove(chosen_card)
                        return chosen_card
                    else:
                        print(f"You must follow the leading color: {leading_color} or play a trump: {trump}.")
                else:
                    self.hand.remove(chosen_card)
                    return chosen_card
            else:
                print("Invalid card. Please choose a card from your hand.")

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
