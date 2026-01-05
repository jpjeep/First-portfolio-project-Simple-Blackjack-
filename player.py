from hand import Hand
class Player:
    balance  = 1000
    def __init__(self, name, bet, hand):
        self.name = name
        self.bet = bet
        self.hand = hand
    @property
    def score(self):
        return Hand(self.hand)
    def place_bet(self, bet):
        self.bet = bet
        self.balance -= self.bet
        print (f"{self.name} has betted {self.bet}$.\n")
    def hit(self, card):
        print(f"{self.name} chooses to hits.\n")
        self.hand.append(card)
        return
    def stand(self):
        print(f"{self.name} chooses to stand.\n")
        pass
