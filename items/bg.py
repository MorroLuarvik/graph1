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

	def get_z_index(self):
		""" return z index for dispaly sort """
		return -1

	def action(self):
		""" display object on screen """
		return

	def animate(self):
		""" display object on screen """
		return
