# First-portfolio-project-Simple-Blackjack-
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
    -
  main.py

Problems encountered
