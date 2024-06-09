from Card import Card
import random


class Deck:
    def __init__(self):
        self.CARD_COLORS = ["S", "H", "D", "C"] # S-Spade, H-Heart, D-Diamond, C-Club
        self.CARD_VALUES = [6, 7, 8, 9, 10, "A", "J", "Q", "K"]
        self.deck = self.create_deck()
        random.shuffle(self.deck)

    def create_deck(self):
        excluded_cards = [("6", "C"), ("6", "S")]
        # Create regular deck
        deck = [Card(value, color) for color in self.CARD_COLORS for value in self.CARD_VALUES
                if (str(value), color) not in excluded_cards]
        # Add Jokers
        deck.append(Card("Joker", "Black"))
        deck.append(Card("Joker", "Red"))
        return deck

    def show_deck(self):
        for card in self.deck:
            print(card)

    def draw_random_card(self):
        return random.choice(self.deck)

    def draw_cards(self, num_cards):
        cards = []
        for _ in range(num_cards):
            if self.deck:  # Check if cards are left in the deck
                cards.append(self.deck.pop())
            else:
                print("No more cards in the deck!")
                break
        return cards
