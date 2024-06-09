from Card import Card
import random


class Deck:
    def __init__(self):
        self.CARD_COLORS = ["S", "H", "D", "C"] # S-Spade, H-Heart, D-Diamond, C-Club
        self.CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
        self.deck = self.create_deck()

    def create_deck(self):
        # Create regular deck
        deck = [Card(value, color) for color in self.CARD_COLORS for value in self.CARD_VALUES]
        # Add Jokers
        deck.append(Card("Joker", "Black"))
        deck.append(Card("Joker", "Red"))
        return deck

    def show_deck(self):
        for card in self.deck:
            print(card)

    def draw_random_card(self):
        return random.choice(self.deck)
