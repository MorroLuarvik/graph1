#!/usr/bin/env python
#-*-coding:utf-8-*-
""" player graph element """

import os
import sys
import pygame

class Player(object):
	""" player object """
	x = 100
	y = 100

	width = 32
	height = 48

	playerImage = None
	playerImagePath = "/res/persons/"

	isAnimate = False
	stage = 0
	maxStages = 4
	animateDelay = 6
	animateCounter = 0
	direction = 0 # 0 - down 1 - left 2 - right 3 - up

	def __init__(self, x = 100, y = 100, imageFile = "officeman1.png"):
		""" init palyer image """

		self.x = x
		self.y = y
		dirName = os.path.split(os.path.abspath(sys.argv[0]))[0]
		self.playerImage = pygame.image.load(dirName + self.playerImagePath + imageFile)

		print dirName + self.playerImagePath + imageFile


	def display(self, screen):
		""" display object on screen """

		if self.isAnimate:
			self.animateCounter += 1
			if self.animateCounter >= self.animateDelay:
				self.animateCounter = 0
				self.stage += 1
				if self.stage >= self.maxStages:
					self.stage = 0

		screen.blit(self.playerImage, (self.x, self.y), (0 + self.stage * self.width, self.direction * self.height, self.width, self.height))

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
