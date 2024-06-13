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
