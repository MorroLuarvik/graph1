#!/usr/bin/env python
#-*-coding:utf-8-*-
""" player graph element """

import os
import sys
import pygame

import random

from bg import Bg

class Player(Bg):
	""" player object """
	x = 100
	y = 100

	width = 32
	height = 48
	busyWidth = 24
	busyHeight = 16
	canCollision = True

	playerImage = None
	playerImagePath = "/res/persons/"

	isAnimate = False
	allwaysAnimate = False
	
	enabledAI = False
	stage = 0
	maxStages = 4
	animateDelay = 6
	animateCounter = 0
	direction = 0 # 0 - down 1 - left 2 - right 3 - up

	targetX = None
	targetY = None
	sleepTimer = None

	maxSleepTime = 300
	maxTargetX = 760
	maxTargetY = 550

	def __init__(self, x = 100, y = 100, imageFile = "officeman1.png", enabledAI = False):
		""" init palyer image """

		self.x = x
		self.y = y
		dirName = os.path.split(os.path.abspath(sys.argv[0]))[0]
		self.playerImage = pygame.image.load(dirName + self.playerImagePath + imageFile)
		self.enabledAI = enabledAI

		print dirName + self.playerImagePath + imageFile
		self.imageFile = imageFile

	def action(self, items):
		if not self.enabledAI:
			return
		
		if self.sleepTimer is not None:
			#print "sleep " + str(self.sleepTimer)
			self.direction = 0
			self.stop_animate()
			self.sleepTimer -= 1
			if self.sleepTimer <= 0:
				self.sleepTimer = None
			return

		if self.targetX is not None:
			#print "move to " + str(self.targetX) + ', ' + str(self.targetY)

			moveFlag = False

			if self.x < self.targetX and not moveFlag:
				moveFlag |= self.move_right(items)

			if self.x > self.targetX and not moveFlag:
				moveFlag |= self.move_left(items)

			if self.y < self.targetY and not moveFlag:
				moveFlag |= self.move_down(items)

			if self.y > self.targetY and not moveFlag:
				moveFlag |= self.move_up(items)

			if self.y == self.targetY and self.x == self.targetX:
				self.targetX = None
				self.targetY = None
			
			if not moveFlag:
				self.targetX = None
				self.targetY = None
			return

		if random.randint(0, 1) == 0:
			self.sleepTimer = random.randint(0, self.maxSleepTime)
			return
		
		self.targetX = random.randint(0, self.maxTargetX)
		self.targetY = random.randint(0, self.maxTargetY)

	def get_busy_min_x(self):
		""" get_busy_min_x """
		return self.x

	def get_busy_max_x(self):
		""" get_busy_max_x """
		return self.x + self.busyWidth

	def get_busy_min_y(self):
		""" get_busy_min_y """
		return self.y + self.height - self.busyHeight

	def get_busy_max_y(self):
		""" get_busy_min_y """
		return self.y + self.height

	def animate(self):
		""" internal control and animate """
		if self.isAnimate:
			self.animateCounter += 1
			if self.animateCounter >= self.animateDelay:
				self.animateCounter = 0
				self.stage += 1
				if self.stage >= self.maxStages:
					self.stage = 0

	def display(self, screen):
		""" display object on screen """
		screen.blit(self.playerImage, (self.x, self.y), (0 + self.stage * self.width, self.direction * self.height, self.width, self.height))

	def get_z_index(self):
		""" return z index for dispaly sort """
		return self.y

	def has_collision(self, items):
		for item in items:
			if item == self:
				continue
			if not item.canCollision:
				continue
			#print "compare " + self.imageFile + " width " + item.imageFile
			if self.get_busy_min_x() <= item.get_busy_max_x() and self.get_busy_max_x() >= item.get_busy_min_x() and self.get_busy_min_y() <= item.get_busy_max_y() and self.get_busy_max_y() >= item.get_busy_min_y():
				#print str(self.get_busy_min_x()) + '<=' + str(item.get_busy_max_x()) + ' and ' + str(self.get_busy_max_x()) + '>=' + str(item.get_busy_min_x()) + ' and ' + str(self.get_busy_min_y()) + '<=' + str(item.get_busy_max_y()) + ' and ' + str(self.get_busy_max_y()) + '>=' + str(item.get_busy_min_y())
				return True
		return False


	def stop_animate(self):
		if self.allwaysAnimate:
			return

		self.isAnimate = False
		self.stage = 0

	def move_up(self, items):
		self.isAnimate = True
		self.direction = 3
		self.y -= 1
		if self.y < 0:
			self.y = 0
		
		if self.has_collision(items):
			self.y += 1
			return False
		
		return True

	def move_down(self, items):
		self.isAnimate = True
		self.direction = 0
		self.y += 1
		
		if self.has_collision(items):
			self.y -= 1
			return False
		
		return True

	def move_left(self, items):
		self.isAnimate = True
		self.direction = 1
		self.x -= 1
		if self.x < 0:
			self.x = 0
		
		if self.has_collision(items):
			self.x += 1
			return False

		return True

	def move_right(self, items):
		self.isAnimate = True
		self.direction = 2
		self.x += 1
		
		if self.has_collision(items):
			self.x -= 1
			return False

		return True
