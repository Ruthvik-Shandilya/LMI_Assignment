class Card:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suite = suit

    def __str__(self):
        return self.rank + ' of ' + self.suite
