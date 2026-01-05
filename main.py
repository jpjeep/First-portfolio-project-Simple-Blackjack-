from game import BlackjackGame
def main():
    answer = "Y"
    while answer == "Y":
        print("Welcome to a game of Blackjack.")
        while True:
            answer = input("Are you ready to go?[Y/N]: ")
            if (answer == "Y") or (answer == "N"):
                if answer == "Y":
                    break
                elif answer == "N":
                    print("Are you sure :(\n")
                    main()
            else:
                print("Only input valid choices.\n")
        print("\nFirst, pick the number of players and place your bets. Everyone starts with $1000.")
        while True:
            try: 
                while True:
                    num = int(input("Input the number of players for this game: "))
                    if num == 0:
                        print ("Must be a positive integer.\n")
                        continue
                    else:
                        break
            except ValueError:
                print("Must be an Integer.")
                continue
            break
        print("Great we can now start!\n")
        new = BlackjackGame(num)
        new.start()
        print("The game of Blackjack has ended.")
        while True:
            answer = input("Would you like to play a new game?[Y/N] ")
            if answer == "Y":
                main()
            elif answer == "N":
                print("Until next time.")
                exit()
            else:
                print("Only input valid choices.\n")
if __name__ == "__main__":
    main()