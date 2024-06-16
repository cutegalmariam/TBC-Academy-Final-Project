class Card:
    def __init__(self, value, color=None):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.value}{self.color if self.color else ''}"

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.color == other.color
        return False

    def __hash__(self):
        return hash((self.value, self.color))

    def card_value(self, trump):
        value_order = {6: 0, 7: 1, 8: 2, 9: 3, 10: 4, "J": 5, "Q": 6, "K": 7, "A": 8}
        if self.value == "JOKER":
            return 100  # Assign a high value to jokers
        trump_bonus = 10 if self.color == trump else 0
        return value_order[self.value] + trump_bonus



