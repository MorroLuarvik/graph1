#!/usr/bin/env python
#-*-coding:utf-8-*-
"""Envueroment module with resources and controls input"""

import os, json, sys, time
import pygame

class Env(object):
	""" enveroment class where loading resourses and working with controls"""
	FONT_PATH = "/res/fonts/tahoma.ttf"
	DEF_WIDTH = 800
	DEF_HEIGHT = 600
	FPS = 20 #60

	prevTimeMark = time.time()
	timeDelta = 0.1

	#dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([self.DEF_WIDTH, self.DEF_HEIGHT])

		self.timeDelta = 1 / float(self.FPS)

	def display_items(self, items):
		""" show items in application window """

		for item in items:
			getattr(self.screen, item['method'])(item['params'])

		pygame.display.flip()

		return

	def delay(self):
		""" delay execute by FPS setting """

		sleepTime = self.timeDelta - time.time() + self.prevTimeMark

		if sleepTime > 0:
			time.sleep(sleepTime)

		self.prevTimeMark = time.time()

	def has_exit_event(self, controls):
		""" get exit event in controls """
		if 'Exit' in controls:
			return controls['Exit']

		return False

	def quit(self):
		""" close used pygame and afer save config"""
		pygame.quit()
