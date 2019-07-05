#!/usr/bin/env python
#-*-coding:utf-8-*-

import pygame
import time

class Controls(object):
	""" get and recognize controls """

	bindingEvents = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_ESCAPE: 'Exit'}
	concurentEvents = [{'up', 'donw'}, {'left', 'right'}]

	controlEvents = {}
	events = {}
	
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

		for bindedEvent, controlEvent in self.bindingEvents.iteritems():
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
