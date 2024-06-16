class HandResultForPlayer:
    def __init__(self, say, taken, score):
        self.say = say
        self.taken = taken
        self.score = score

    def is_clean(self):
        return self.say == self.taken
