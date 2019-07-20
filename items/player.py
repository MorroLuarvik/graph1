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

	playerImage = None
	playerImagePath = "/res/persons/"

	isAnimate = False
	enabledAI = False
	stage = 0
	maxStages = 4
	animateDelay = 6
	animateCounter = 0
	direction = 0 # 0 - down 1 - left 2 - right 3 - up

	targetX = None
	targetY = None
	sleepTimer = None

	maxSleepTime = 100
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

	def action(self):
		if not self.enabledAI:
			return

		if self.sleepTimer is not None:
			#print "sleep " + str(self.sleepTimer)
			self.stop_animate()
			self.sleepTimer -= 1
			if self.sleepTimer <= 0:
				self.sleepTimer = None
			return

		if self.targetX is not None:
			#print "move to " + str(self.targetX) + ', ' + str(self.targetY)
			if self.x < self.targetX:
				self.move_right()
			if self.x > self.targetX:
				self.move_left()
			if self.y < self.targetY:
				self.move_down()
			if self.y > self.targetY:
				self.move_up()
			if self.y == self.targetY and self.x == self.targetX:
				self.targetX = None
				self.targetY = None
			return

		if random.randint(0, 1) == 0:
			self.sleepTimer = random.randint(0, self.maxSleepTime)
			return
		
		self.targetX = random.randint(0, self.maxTargetX)
		self.targetY = random.randint(0, self.maxTargetY)



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

	def stop_animate(self):
		self.isAnimate = False
		self.stage = 0

	def move_up(self):
		self.isAnimate = True
		self.direction = 3
		self.y -= 1
		if self.y < 0:
			self.y = 0

	def move_down(self):
		self.isAnimate = True
		self.direction = 0
		self.y += 1

	def move_left(self):
		self.isAnimate = True
		self.direction = 1
		self.x -= 1
		if self.x < 0:
			self.x = 0

	def move_right(self):
		self.isAnimate = True
		self.direction = 2
		self.x += 1
