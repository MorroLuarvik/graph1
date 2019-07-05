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

		self.events = self.__remove_concurent_events(self.events, self.concurentEvents)

		for bindedEvent, controlEvent in self.bindingEvents.iteritems():
			if bindedEvent in self.events:
				self.controlEvents[controlEvent] = True

		#print self.events
		print self.controlEvents

		return self.controlEvents

	def __clear_event(self, eventName):
		""" remove eventName from self.controlEvents """

		if eventName in self.controlEvents:
			self.events.pop(eventName)

	def __remove_concurent_events(self, events, concurentEvents):
		""" remove concurent event from list """
		for inputCode in events:
			if inputCode in self.bindingEvents:
				if self.__in_concurent(inputCode, concurentEvents):
					events = self.__clear_concurent(events, inputCode, self.__get_counurent_codes(inputCode, concurentEvents))
			else:
				events.pop(inputCode)

		return events

	def __in_concurent(self, code, concurentEvents):
		""" check entereded code in concurent sets """
		for setOfActions in concurentEvents:
			if self.bindingEvents[code] in setOfActions:
				return True

		return False

	def __get_counurent_codes(self, code, concurentEvents):
		""" get codes of concurecnt evenst """
		for setOfActions in concurentEvents:
			if self.bindingEvents[code] in setOfActions:
				ret = ()
				for action in setOfActions:
					for addCode in self.bindingEvents:
						if self.bindingEvents[addCode] == action:
							ret += (addCode)
				return ret

		return ()
