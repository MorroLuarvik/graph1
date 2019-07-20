#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Items module with resources about display items"""

from .bg import Bg
from .player import Player

import random

class Items(object):
	""" application items collections """

	playerImage = None
	playerImagePath = "/res/persons/officeman1.png"

	items = []
	conflictedEvents = []

	def __init__(self):
		""" init items """

		self.player = Player()

		self.items.append(Bg())
		self.items.append(self.player)
		self.items.append(Player(230, 90, "officewoman3.png"))
		self.items.append(Player(330, 200, "pinkbat.png"))
		self.items[3].isAnimate = True

		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officewoman1.png", True))
		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officewoman4.png", True))
		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officewoman5.png", True))
		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officewoman6.png", True))
		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officeman2.png", True))
		self.items.append(Player(random.randint(0, 800), random.randint(0, 600), "officeman3.png", True))

	def get_items(self):
		""" just return items """
		return sorted(self.items, key = lambda Bg: Bg.get_z_index())

	def update_by_controls(self, ctrl):
		""" update item by controlas at current version will be used up and down controls """

		if 'up' in ctrl:
			self.player.move_up(self.items)

		if 'down' in ctrl:
			self.player.move_down(self.items)

		if 'left' in ctrl:
			self.player.move_left(self.items)

		if 'right' in ctrl:
			self.player.move_right(self.items)

		if ctrl == {}:
			self.player.stop_animate()

		return
