from hand import Hand
#only hold state
#like the hand and money available
class Dealer:
    def __init__(self, hand):
        #this is an object turned attribute to be handled in the main function
        self.hand = hand
    @property
    def score(self):
        return Hand(self.hand)
    def play_turn(self, card):
        if self.score.total() < 17:
            print("The dealer has a total of less than 17.")
            while self.score.total() < 17:
                self.hand.append(card)
                print(f"The dealer has drawn, {card.rank} of {card.suit}.")
        else:
            pass
        print (f"\nThe dealer's cards are...")
        for a in self.hand:
            print (f"{a.rank} of {a.suit}.")
        #determines if 17 or not
        #if 17 cannot draw anymore
        #elif 17 draw to determine winner   