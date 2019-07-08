#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Items module with resources about display items"""

import os
import sys
import pygame
#import json

class Items(object):
	""" application items collections """

	playerImage = None
	playerImagePath = "/res/persons/officeman1.png"

	items = []
	conflictedEvents = []

	def __init__(self):
		dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))
		self.playerImage = pygame.image.load(dirName + self.playerImagePath)

		self.items.append({'name': 'bg', 'method': 'fill', 'params': {"color": [155, 155, 155]}})
		self.items.append({'name': 'palyer', 'method': 'blit', 'params': {"source": self.playerImage, "dest": [50, 50], "area": [0, 0, 32, 48]}})
		self.conflictedEvents = [{'up', 'down'}, {'left', 'right'}]

	def get_items(self):
		""" just return items """
		return self.items

	def update_by_controls(self, ctrl):
		""" update item by controlas at current version will be used up and down controls """

		if 'up' in ctrl:
			self.__inc_light()
		if 'down' in ctrl:
			self.__dec_light()
		return False

	def __inc_light(self):
		""" increase background color """
		color = self.items[0]['params']['color'][0]
		color += 1
		if color > 255:
			color = 255
		print color
		self.items[0]['params']['color'] = [color, color, color]

	def __dec_light(self):
		""" increase background color """
		color = self.items[0]['params']['color'][0]
		color -= 1
		print color
		if color < 0:
			color = 0
		self.items[0]['params']['color'] = [color, color, color]
