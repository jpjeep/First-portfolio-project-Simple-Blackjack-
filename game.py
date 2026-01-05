from player import Player
from dealer import Dealer
from deck import Deck
class BlackjackGame:
    def __init__(self, num_players, dealer = None, deck = None, players = None, round_number = 1):
        self.num_players = num_players
        self.dealer = dealer
        self.deck = deck
        self.players = players
        self.round_number = round_number
    def start(self):
        self.setup_players()
        ("Players have been set-up.")
        ("Let us now begin.")
        ("Reminder: All players start with $1000 of balance.")
        game_status = "Y"
        while game_status == "Y":
            self.place_bets()
            self.initial_deal()
            self.run_player_turns()
            self.run_dealer_turn()
            self.resolve_round()
            self.eliminate_broke_players()
            if not self.players:
                print("All players have been eliminated.")
                print("The dealer has won this games.")
                break
            while True:
                answer = self.ask_continue()
                if answer == "Y":
                    self.round_number += 1
                    self.dealer.hand = []
                    for a in self.players:
                        a.hand = []
                    break
                elif answer ==  "N":
                    self.results()
                    break
                else:
                    print("Not part of the choices.\n")
            game_status = answer
    def setup_players(self):
        print(f"You will have a total of {self.num_players} players.")
        self.players = []
        for a in range (self.num_players):
            while True:
                person = input(f"\nWhat is the name of your #{a} player: ")
                answer = input(f"Is ({person}) correct?[Y/N]: ")
                if (answer == "Y") or (answer == "N"):
                    if answer == "Y":
                        self.players.append(Player(person,0 , []))
                        break
                    elif answer == "N":
                        pass
                else:
                    print("Only input valid choices.\n")
        print("\nHere are your players.")
        for b in self.players:
            print(f"- {b.name}")
        self.dealer = Dealer([])
        self.deck = Deck()
    def place_bets(self):
        print(f"\nWelcome to round {self.round_number}.")
        print("Place your bets!\n")
        for a in self.players:
            while True:
                try: 
                    while True:
                        bet = int(input(f"How much will {a.name} bet? "))
                        if bet > a.balance:
                            print("Exceeds your current balance.\n")
                            continue
                        break
                except ValueError:
                    print("Must be an integer.")
                break
            a.place_bet(bet)
        print("Here are your bets per player.")    
        for b in self.players:
            print(f"{b.name} has betted {b.bet}, with a remaining balance of {b.balance}.")
        print("\n")
    def initial_deal(self):
        self.deck.shuffle()
        for _ in range(2):
            self.dealer.hand.append(self.deck.deal())
            for a in self.players:
                a.hand.append(self.deck.deal())    
        print(f"The dealer's hand is {self.dealer.hand[0].rank} of {self.dealer.hand[0].suit}. One card is covered.\n")
        print("Below corresponds to cards of the players.\n")
        for b in self.players:
            print(f"{b.name} has {b.hand[0].rank} of {b.hand[0].suit} and {b.hand[1].rank} of {b.hand[1].suit}.")
        for c in self.players:
            if c.score.is_blackjack():
                print(f"{c.name}, you got a Blackjack! You are now excluded for the rest of the round.")
                continue
            else:
                continue
    def run_player_turns(self):
        print("\n")
        for a in self.players:
            if not a.score.is_blackjack():
                print(f"What will {a.name} play.")
                while True:
                    try: 
                        while True:
                            choice = int(input(f"Input 1 for hit and input 2 for stand: "))
                            if choice == 1:
                                draw = self.deck.deal()
                                a.hit(draw)
                                print (f"{a.name} has drawn {draw.rank} of {draw.suit}.")
                                if a.score.is_bust():
                                    print(f"{a.name}, you have busted.\n")
                                    break
                                elif a.score.is_blackjack():
                                    print(f"{a.name}, you got a Blackjack with that draw.")
                                    print("Let's wait for the dealer's total.\n")
                                else:
                                    pass
                                print(f"{a.name} can still choose to hit or stand.\n")
                            elif choice == 2:
                                a.stand()
                                break
                            else:
                                print("Not part of the choices.\n")
                    except ValueError:
                        print("Not part of the choices.\n")
                    break
            else:
                print(f"{a.name}, you already got a Blackjack.")
                print("Let's wait for the dealer's total.\n")
        print("Here is an update to each players' hand.\n")
        for b in self.players:
            for c in b.hand:
                print(f"{b.name} has {c.rank} of {c.suit}.")
            print("\n")
    print("\n")
    def run_dealer_turn(self):
        print(f"The dealer's last card is {self.dealer.hand[1].rank} of {self.dealer.hand[1].suit}.")
        self.dealer.play_turn(self.deck.deal())
        print("\n")
    def resolve_round(self):
        for a in self.players:
            print(f"The total for {a.name} is {a.score.total()}.")
        print (f"The total for the dealer is {self.dealer.score.total()}.\n")
        for b in self.players:
            if b.score.is_bust():
                print(f"{b.name} busted.")
                print(f"{b.name}, you're new balance is {b.balance}$.\n")
                continue
            if self.dealer.score.is_bust():
                print("Everybody wins twice their bet, except the busted players.")
                for c in self.players:
                    if not c.score.is_bust():
                        c.balance += 2*(c.bet)
                        print(f"{c.name}, you're new balance is {c.balance}$.\n")
                    else:
                        continue
                break
            elif self.dealer.score.is_blackjack():
                if b.score.is_blackjack():
                    print(f"It is a push. {b.name}'s bets are returned.")
                    b.balance += b.bet
                    print(f"{b.name}, you have {b.balance}$.\n")
                    continue
                print(f"{b.name}, you have lost.")
                print(f"{b.name}, you have {b.balance}$.\n")
                continue
            elif not self.dealer.score.is_blackjack():
                if b.score.is_blackjack():
                    print(f"{b.name} won a Blackjack.")
                    b.balance += 2*(b.bet)
                    print(f"{b.name}, you're new balance is {b.balance}$.\n")
                    break
                if b.score.total() > self.dealer.score.total():
                    print(f"{b.name}, you have won. You get twice your bet.")
                    b.balance += 2*(b.bet)
                    print(f"{b.name}, you're new balance {b.balance}$.\n")
                    continue
                elif b.score.total() < self.dealer.score.total():
                    print(f"{b.name}, you have lost.")
                    print(f"{b.name}, you have {b.balance}$.\n")
                    continue
                elif b.score.total() == self.dealer.score.total():
                    print(f"It is a push. {b.name}'s bets are returned.")
                    b.balance += b.bet
                    print(f"{b.name}, you have {b.balance}$.\n")
                    continue
    def eliminate_broke_players(self):
        for a in self.players[:]:
            if a.balance == 0:
                self.players.remove(a)
                print(f"{a.name}, you have been eliminated.\n")
            else:
                print(f"{a.name}, you are still in the game.")
                print(f"{a.balance}, is your balance.\n")
                continue
    def ask_continue(self):
        ans = input("Will you continue to play the game?[Y/N]: ")
        return ans
    def results(self):
        print(f"\nThe game went on for {self.round_number} rounds.\n")
        for a in self.players:
            print(f"{a.name} has won {a.balance}$.")
