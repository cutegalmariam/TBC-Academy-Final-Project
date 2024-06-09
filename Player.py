class Player:
    def __init__(self, name, score, cards_taken):
        self.name = name
        self.score = score
        self.cards_taken = cards_taken
        self.hand = []

    def __repr__(self):
        return f"{self.name}, {self.score}, {self.cards_taken} , hand={self.hand}"

    def add_cards_to_hand(self, cards):
        self.hand.extend(cards)
