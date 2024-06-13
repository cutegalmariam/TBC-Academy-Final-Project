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
            card_input = input(f"{self.name}, choose a card to play (e.g., 9H for 9 of Hearts): ").upper()
            if len(card_input) >= 2 or card_input == "JOKERRED" or card_input == "JOKERBLACK":
                value = int(card_input[:-1]) if card_input[:-1].isdigit() else card_input[:-1]
                color = card_input[-1]
                chosen_card = Card(value, color)
                # print(type(self.hand[0]))
                if chosen_card in self.hand:
                    # Check if the player has the leading color or trump
                    has_leading_color = any(card.color == leading_color for card in self.hand)
                    has_trump = any(card.color == trump for card in self.hand)

                    if leading_color:
                        if chosen_card.color == leading_color or chosen_card.color == trump:
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
            else:
                print("Invalid input. Please enter a card in the format value+color (e.g., 9H).")


    def card_value(self, card, trump):
        value_order = {6: 0, 7: 1, 8: 2, 9: 3, 10: 4, "A": 5, "J": 6, "Q": 7, "K": 8}
        trump_bonus = 10 if card.color == trump else 0
        return value_order[card.value] + trump_bonus
