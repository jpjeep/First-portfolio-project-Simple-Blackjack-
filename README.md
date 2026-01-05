# First-portfolio-project-Simple-Blackjack- (PLEASE VIEW IN CODE FOR BETTER LAYOUT)
Welcome to my first coding project that will be uploaded to GitHub. I used python to create a simple Blackjack game. 
I did not include all the rules in Blackjack, but the essential ones are included such as drawing playing cards from a standard deck of 52 to form a hand as 
equating as close as possible to 21 but not exceeding it.

Description of each file:
  card.py
    - This file is used for creating a class Card, which will create the objects that will acts as the cards of the game. This class only has attributes.
  deck.py
    - This file is used for creating the class Deck, which will create the standard 52 card deck which create Crad objects with rank, suit, value attributes.
    - It has only one attribute with two methods.
    - shuffle() is used for ramdomy arranging the deck for each round of a game.
    - deal() is for popping the shuffled deck as it acts as a list of Card objects
  hand.py
    - This file is used for holding the value of hand of an object of Player class from the player file. it has three methods.
    - First, the total() method is used for summing the value of the cards of an instance of a player, already includes the proper handling of the value of an ace
    - Next, is the is_blackjack() method for returng a True or False statement if the total() is equal to 21.
    - Finally, the is_bust() method for returng a True or False statement if the total() is more than 21.
  player.py
    - This file is used for creating instances of the "players" of the game, it has three attribute and one property. It also has three methods to simulate a real player.
    - I created the property so that it changes whenever the hand changes. This will be useful for eliminating the last "data" from the last round and moving on to the next round.
    - place_bet() is handling the bets and subtrancting the balance of a player
    - hit() is acting as a decision of the player to add a card to their hand
    - stand() is a decsion for ending their turn
  dealer.py
    - This file is used for automatic decision making of a made-up player called the dealer. It has the same attributes as the Player class from player.py
    - Its only method play_turn() is automated in the game.py if the hand of the dealer is less than 17.
  game.py
    - This file is for instancing a game of Blackjack from a number of players as long its more than 0. It uses the other classes and files so far to make a smooth game of Blackjack
    - The game creates instances of players, dealers, round_number and a deck which also serves as its attributes
    - First, the start() method is used for utilizing all other methods in the Class BlackjackGame. it also acts as simulating a round of blackjack
    - Next, is setup_players(), it used for initiliazing who the players are and is not repeated
    - After this, this is where the "rounds" of the game begin with place_bets() which runs every players decison with also checking their balance.
    - initial_deal() is used for simulating the first two cards and the dealer's revealed and upside down card
    - Next is the run_player_turns() which asks for the decison of each player to hit or stand which are mthods from the Player class
    - And then the run_dealer_turn() to simulate the decison of the dealer after revealing the upside down card.
    - resolve_round is used for determing the wins and lossess from computing the total value of each hand from the players and the dealer
    - eliminate_broke_players() is use for removing the players with 0 balance from the attribute players and ending the whole start() program redirecting to main.py if all players have 0 balance
    - ask_conitnue is used for determing the continutation of more rounds of Blackjack or ending the game
    - results() is for displaying the balance of the players after a game.
  main.py
    - This only utilizes the Blackjack game class to create an instance of a "game"> It is mainly for looping to create instances of Blackjack games.
  
Problems encountered:
1. Uploading to GitHub. Cost me so much time trying to figure the command prompt way, I alsmot didn't past in time. Just went in and brute force my way in uploading the files
2. loops get confusing. Most of the time that was spent was navigating the countless of loops in order to execute a smooth game
3. Personal problem, handling of \n makes the output look complicated. Took time to figure out so the problems from the output was so chaotic because of my incorrect used of \n in some functions
4. Checking the game rules on betting returns was confusing to focus in incorporating in the code
5. Treating the project, "object oriented" and not adjusted using the properties of object and classes
6. I got trouble how to reset the score or the value of the hand back to 0 every round. Searched in upped and used @property
7. I got trouble handling the ace value cards solved at the end.
