import os, json, sys

class Items:

	items = []

	def __init__(self):
		self.items = [
			{ 
				'name': 'bg',
				'method': 'fill',
				'params': [155, 155, 155]
			}
		]

	def getItems(self):
		return self.items

	def updateByControls(self, controls):
		if not('bg_lighter' in controls):
			return

		if controls['bg_lighter']:
			print('add light')
		else:
			print('dec light')

		#return False

