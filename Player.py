#import Card file to utilize objects from the class and its functions
from Card import *

#define class Player with the attributes name and hand (hand is a empty list)
class Player:
	def __init__(self, name, hand):
		self.name = name
		self.hand = []
#define addCardToHand function with the attribute Card so relating to objects from class Card
	def addCardToHand(self, Card):
		self.hand.append(Card)
#define disposeCardToHand function with the attribute Card so relating to objects from class Card
	def disposeCardOfHand(self, Card):
		self.hand.remove(Card)
