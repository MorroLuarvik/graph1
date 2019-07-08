#!/usr/bin/env python
#-*-coding:utf-8-*-

import pygame
import time

class Controls(object):
	""" get and recognize controls """

	bindingEvents = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_ESCAPE: 'Exit'}
	concurentEvents = [{'up', 'donw'}, {'left', 'right'}]

	events = {}
	
	def get_controls(self):
		""" get current controls """

		controlEvents = {}

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				controlEvents['Exit'] = True

			# get release keys
			if event.type == pygame.KEYUP:
				self.events = self.__clear_event(self.events, event.key)

			# get pressed keys
			if event.type == pygame.KEYDOWN:
				self.events[event.key] = time.time()

		#self.events = self.__remove_concurent_events(self.events, self.concurentEvents)

		for bindedEvent, controlEvent in self.bindingEvents.iteritems():
			if bindedEvent in self.events:
				controlEvents[controlEvent] = True

		#print self.events
		#print controlEvents

		return controlEvents

	def __clear_event(self, events, eventCode):
		""" remove eventName from self.controlEvents """

		if eventCode in events:
			events.pop(eventCode)
		
		return events

	def __remove_concurent_events(self, events, concurentEvents):
		""" remove concurent event from list """
		for inputCode in events:
			if inputCode in self.bindingEvents:
				if self.__in_concurent(inputCode, concurentEvents):
					print self.__get_concurent_codes(inputCode, concurentEvents)
					events = self.__clear_concurent(events, self.__get_concurent_codes(inputCode, concurentEvents))
			else:
				events.pop(inputCode)

		return events

	def __clear_concurent(self, actions, concurentActions):
		""" remove concurent action from total action list """
		for action in concurentActions:
			actonTS = 0
			oldAction = None
			if action in actions:
				if actions[action] > actonTS:
					if not(oldAction is None) :
						print "remove " + oldAction
						actions.pop(oldAction)
					actonTS = actions[action]
					oldAction = action

		return actions

	def __in_concurent(self, code, concurentEvents):
		""" check entereded code in concurent sets """
		for setOfActions in concurentEvents:
			if self.bindingEvents[code] in setOfActions:
				return True

		return False

	def __get_concurent_codes(self, code, concurentEvents):
		""" get codes of concurecnt evenst """
		for setOfActions in concurentEvents:
			if self.bindingEvents[code] in setOfActions:
				ret = ()
				for action in setOfActions:
					for addCode in self.bindingEvents:
						if self.bindingEvents[addCode] == action:
							ret = ret + (addCode, )
				return ret

		return ()
