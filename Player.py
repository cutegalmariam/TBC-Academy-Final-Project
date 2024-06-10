class Player:
    def __init__(self, name, score, cards_taken):
        self.name = name
        self.score = score
        self.cards_taken = cards_taken
        self.hand = []
        self.trump = None
        self.say = 0

    def __repr__(self):
        return f"Player(name={self.name}, score={self.score}, games_played={self.games_played}, hand={self.hand}, trump={self.trump}, say={self.say})"

    def add_cards_to_hand(self, cards):
        self.hand.extend(cards)
