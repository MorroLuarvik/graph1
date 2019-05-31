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
		if not 'bg_lighter' in ctrl:
			return

		if ctrl['bg_lighter']:
			print 'add light'
		if ctrl['bg_darker']:
			print 'dec light'
		return False

