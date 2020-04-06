import pygame

class Translate:
	def __init__(self, amt):
		self.amt = amt

	def apply(self, pos):
		return self.amt + pos

	def applyx(self, pos):
		return self.amt.x + pos

	def applyy(self, pos):
		return self.amt.y + pos