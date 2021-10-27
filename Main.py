#this file to run the whole application

#version 00.01.00 - Hard Coded Player can receive something and put it into a list and pop it from the list

#import Player file to utilize objects from the class and its functions
from Player import *
#import Card file to utilize objects from the class and its functions
from Card import *
#import Deck file to utilize objects from the class and its functions
from Deck import *

#initialize a hardcoded object of class Player with the name tom and an empty list
player = Player("Tom",[]) #Question: why can not initialize object with list contents e.g. player = Player("Tom",["apple", banana"])
print(player.name, player.hand)
#initialize a hardcoded object of class Card with the suit Spades and the value 1
card = Card("Spades",1)
print(card.suit, card.value)
#call the addCardToHand function for the previously created player and the previously created card objects
player.addCardToHand(card)
for card in player.hand:
	print(card.suit, card.value)
#call the disposeCardofHand function for the previously created player and the previously created card objects
player.disposeCardOfHand(card)
print(player.hand)
#initialize an object of class Deck with an empty deck list
gameDeck = Deck([])
#call the buildDeck function for the newly created Deck object
gameDeck.buildDeck()
#call the showDeck function for the created Deck object
gameDeck.showDeck()

