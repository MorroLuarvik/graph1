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
		self.items = Items()
		self.env = Env()

	def run(self):
		"""Let's go"""
		running = True
		while running:
			controls = self.env.get_controls()
			self.items.update_by_controls(controls)
			self.env.display_items(self.items.get_items())
			self.env.delay()
			running = not self.env.has_exit_event(controls)

		self.env.quit()

if __name__ == "__main__":
	proc = GameLoop()
	proc.run()

print "Bye!"
exit()
