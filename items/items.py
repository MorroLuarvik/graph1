#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Items module with resources about display items"""

from .bg import Bg
from .player import Player

class Items(object):
	""" application items collections """

	playerImage = None
	playerImagePath = "/res/persons/officeman1.png"

	items = []
	conflictedEvents = []

	def __init__(self):
		""" init items """

		self.items.append(Bg())
		self.items.append(Player())
		self.items.append(Player(230, 90, "officewoman3.png"))
		self.items.append(Player(30, 160, "officewoman1.png"))
		self.items.append(Player(330, 200, "pinkbat.png"))
		self.items[4].isAnimate = True

	def get_items(self):
		""" just return items """
		return sorted(self.items, key = lambda player: player.y)

	def update_by_controls(self, ctrl):
		""" update item by controlas at current version will be used up and down controls """

		if 'up' in ctrl:
			self.items[1].move_up()

		if 'down' in ctrl:
			self.items[1].move_down()

		if 'left' in ctrl:
			self.items[1].move_left()

		if 'right' in ctrl:
			self.items[1].move_right()

		if ctrl == {}:
			self.items[1].stop_animate()

		return
