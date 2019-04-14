import random
from Card import Card

class Deck(object):
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.cards=[]

    def deal(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit,rank))

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def drawCard(self):
        return self.cards.pop()