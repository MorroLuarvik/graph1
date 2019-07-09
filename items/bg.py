#!/usr/bin/env python
#-*-coding:utf-8-*-
""" screen bg element """

import pygame

class Bg(object):
	""" bg object """
	y = -1
	bgColor = [100, 250, 100]

	def __init__(self, bg_color = [100, 100, 100]):
		""" init palyer image """

		self.bgColor = bg_color


	def display(self, screen):
		""" display object on screen """

		screen.fill(self.bgColor)