class Card:
    def __init__(self, value, color=None):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.value}{self.color if self.color else ''}"
