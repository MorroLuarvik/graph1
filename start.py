#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Main module whes start application"""

#import time, os, json, sys, datetime
#import pygame

from env import Env
from items import Items

class GameLoop(object):
	"""Main class - main process"""

	def __init__(self):
		"""initialization class"""
		self.env = Env()
		self.items = Items()

	def run(self):
		"""Let's go"""
		running = True
		while running:
			controls = self.env.get_controls()
			self.items.updateByControls(controls)
			self.env.displayItems(self.items.getItems())
			self.env.delay()
			running = not self.env.hasExitEvent(controls)

		self.env.quit()

if __name__ == "__main__":
	proc = GameLoop()
	proc.run()

print "Bye!"
exit()
