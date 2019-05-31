import os, json, sys

class Items(object):

	items = []

	def __init__(self):
		self.items = [{ 
			'name': 'bg',
			'method': 'fill',
			'params': [155, 155, 155]
		}]

	def getItems(self):
		""" just return items """
		return self.items

	def updateByControls(self, controls):
		""" update item by controlas
		at current version will be used pygame.K_UP pygame.K_DOWN """

		if not('bg_lighter' in controls):
			return

		if controls['bg_lighter']:
			print 'add light'
		if controls['bg_darker']:
			print 'dec light'

		#return False

