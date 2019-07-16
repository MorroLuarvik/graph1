#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Items module with resources about display items"""

#import os
#import json
#import sys


class Items(object):
	""" application items collections """

	items = []
	conflictedEvents = []

	def __init__(self):
		self.items = [{'name': 'bg', 'method': 'fill', 'params': [155, 155, 155]}]
		self.conflictedEvents = [{'up', 'down'}, {'left', 'right'}]

	def get_items(self):
		""" just return items """
		return self.items

	def update_by_controls(self, ctrl):
		""" update item by controlas at current version will be used pygame.K_UP pygame.K_DOWN """
		#if not 'bg_lighter' in ctrl:
		#	return

		if 'up' in ctrl:
			self.__inc_light()
		if 'down' in ctrl:
			self.__dec_light()
		return False

	def __inc_light(self):
		""" increase background color """
		color = self.items[0]['params'][0]
		color += 1
		if color > 255:
			color = 255
		print color
		self.items[0]['params'] = [color, color, color]
	
	def __dec_light(self):
		""" increase background color """
		color = self.items[0]['params'][0]
		color -= 1
		print color	
		if color < 0:
			color = 0
		self.items[0]['params'] = [color, color, color]
