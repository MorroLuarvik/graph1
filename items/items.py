import os, json, sys

class Items:

	items = []

	def __init__(self):
		self.items = [
			{ 
				'method': 'fill',
				'params': [155, 155, 155]
			}
		]

	def getItems(self):
		return self.items

	def updateByControls(self, controls):
		return False

