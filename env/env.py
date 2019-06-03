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
	FPS = 60

	prevTimeMark = time.time()
	timeDelta = 0.1

	controlEvents = {}
	events = {}

	bindingEvents = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_ESCAPE: 'Exit'}
	concurentEvents = [{'up', 'donw'}, {'left', 'right'}]

	#dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([self.DEF_WIDTH, self.DEF_HEIGHT])

		self.timeDelta = 1 / float(self.FPS)

	def get_controls(self):
		""" get current controls """

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.controlEvents['Exit'] = True

			# get release keys
			if event.type == pygame.KEYUP:
				self.__clear_event(event.key)

			# get pressed keys
			if event.type == pygame.KEYDOWN:
				self.events[event.key] = time.time()
				#if event.key == pygame.K_ESCAPE:
				#	self.controlEvents['Exit'] = time.time()

		
		for bindedEvent, controlEvent in self.bindingEvents:
			if bindedEvent in self.events:
				self.controlEvents[controlEvent] = True

		"""
			maxTime = 0
			resultEvent = None
			for event in self.events:
				if self.events[event] > maxTime:
					maxTime = self.events[event]
					resultEvent = event
		"""

		#print self.events
		print self.controlEvents

		return self.controlEvents

	def __clear_event(self, eventName):
		""" remove eventName from self.controlEvents """

		if eventName in self.controlEvents:
			self.events.pop(eventName)


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
