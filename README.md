# WAR_Card_Game
## System Requirements
War is played with standard playing cards. The standard deck has 13 ranks in 4 suits.
This project is using Python 3.7

### Background
 > To start with, the players are dealt seperate hand. Each hand has equal number of cards.
 > Each player will throw in one card from their hand.
 > Player with highest valued card wins. Suit doesnt play a role in this game.
 > In case two or more players have same valued card this situation is termed as a tie. To resolve the tie players involved in tie
    continue to play until a winner is found.
 > Player that loses all the card is considered to be evicted from the game
 > Player that collects all the 52 cards is considered winner of the game
 
### Assumptions
  1) Player can range from 2-52
  2) Cards are divided equally amongst players, each player should get atleast 15 cards to avoid player running out of cards prematurely. 
  3) Player with highest valued card is the winner
  4) Player who loses all the card is no longer involved in the game
  5) All the cards won by a player goes to the end of the hand
  6) Playing card is used from the top of the deck
 
 ## Classes
 ### Card
  A standard playing card has a suit and point value from 1 to 13. This is Card class that helps create an object of each playing     card in a given deck. This object will have a Suit and a card value.
 ### Deck
  A standard playing card deck has 52 cards and 4 suits. This is Deck class that works as a collection of Card objects. This is used to simulate real life deck of 52 playing cards. 
### Game
This is the driver class of WAR game. This keeps track of each player in a given round.
This class starts and ends the game upon the appropriate given end condition.
2-52 Players can play this game. Game is ended when a player wins all the cards.
Players are evicted from the game when they loose all their cards in hand to other
player. 
 ### Hand
  A collection of cards. This class is used to simulate a bunch of card in any players hand. Just like a real life person, this class will help add cards to hand, take first card from the hand, or add cards to the hand.
 ### Main
  Driver class that gathers player information, creates game and starts the game.
 ### Player 
  This class is used to a player. It maintains players name and player hand. This class helps perform action on behalf of a player like playing a card from hand and take back cards into the hand.
 ### Pot
  This method simulates the center part of table where game is being played. Players throw in the cards on the table. In case of a tie extra cards which are known as bonus cards are also played here.
 ### Suit
  This class maintains 4 suit of a playing card deck.

## Structure

This repository contains two folder 
1) Tests
    > This folder contains all the tests related to a given class
2) WAR
    > This folder contains actual code of each class
    
## Working
### Tests
    > Each test class can be run seperately by running the python file
    > Test cases are written in Python 3.7 and are running using unittest
    
### WAR Game
    > To start the game go to main.py and run the file
    > This will ask for Number of players.
    > Once number is given then program will ask for names of each player
    > Once the player information is given the program will simulate the WAR game and give the winner at the end.  
    > Program is written using Python 3.7

