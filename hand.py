from card import Card
class Hand(Card):
    def __init__(self, cards):
        self.cards = cards
    #NEED TO EDIT ACE VALUES    
    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank == "Ace":
                aces += 1
                total += 11
            else:
                total += card.value
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total    
    def is_blackjack(self):
        if self.total() == 21:
            return True
        else:
            return False
        # if black jack you automatically win 2x of bet
    def is_bust(self):
        if self.total() > 21:
            return True
        else:
            return False