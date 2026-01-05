from card import Card
import random
class Deck():
    _CARD_DATA = [("Two", 2), ("Three", 3), ("Four", 4),
    ("Five", 5), ("Six", 6), ("Seven", 7), ("Eight", 8),
    ("Nine", 9), ("Ten", 10), ("Jack", 10), ("Queen", 10),
    ("King", 10), ("Ace", 11)
    ]
    _SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
    CARDS = []
    for rank, value in _CARD_DATA:
        for suit in _SUITS:
            CARDS.append(Card(rank, suit, value))
    def __init__(self, deck = CARDS):
        self.deck = deck
    def shuffle(self):
        self.deck = random.sample(self.CARDS, k=len(self.CARDS))
    def deal(self):
        if self.deck:
            return self.deck.pop()
        return None