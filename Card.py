#define class Card with the attributes suit and value
class Card:
	def __init__(self, suit, value, covered):
		self.suit = suit
		self.value = value
		self.covered = covered