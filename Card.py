class Card:
    SAY_TAKEN_SCORES = [
    [50, 10, 20, 30, 40, 50, 60, 70, 80, 90],
    [-500, 100, 20, 30, 40, 50, 60, 70, 80, 90],
    [-500, 10, 150, 30, 40, 50, 60, 70, 80, 90],
    [-500, 10, 20, 200, 40, 50, 60, 70, 80, 90],
    [-500, 10, 20, 30, 250, 50, 60, 70, 80, 90],
    [-500, 10, 20, 30, 40, 300, 60, 70, 80, 90],
    [-500, 10, 20, 30, 40, 50, 350, 70, 80, 90],
    [-500, 10, 20, 30, 40, 50, 60, 400, 80, 90],
    [-500, 10, 20, 30, 40, 50, 60, 70, 450, 90],
    [-500, 10, 20, 30, 40, 50, 60, 70, 80, 900]
]
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



