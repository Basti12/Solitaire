#import Card file to utilize object from class Card to build the deck
from Card import *

#define class Deck with the attributes 
class Deck:
    def __init__(self, deck):
        self.deck = []
#create buildDeck functionality to initialize a deck from the empty list deck and fill with 52 cards whole card deck. The list will be filled by objects of class Card. There is a outer for loop that loops through the suits and a inner for loop that loops through the values. For each x and y that is looped through a new card is added to a object of class Deck when the build function is called so that the 52 Card deck is created.
    def buildDeck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = [1,2,3,4,5,6,7,8,9,"Jack", "Queen", "King", "Ace"]
        for x in suits:
            for y in values:
                card = Card(x,y)
                self.deck.append(card)
#create showDeck functionality that prints the suit and value of each card object in the deck list 
    def showDeck(self):
        for card in self.deck:
            print(card.suit, card.value)
#upcoming functionality to shuffle the deck
    def shuffleDeck(self):
        return self
    
