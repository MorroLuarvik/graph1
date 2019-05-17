#!/usr/bin/env python
#-*-coding:utf-8-*-

import pygame
import time, os, json, sys, datetime

dirName, ownFileName = os.path.split(os.path.abspath(__file__))

pygame.init()
screen = pygame.display.set_mode([800, 600])

screen.fill([255, 255, 255])


#pygame.display.flip()

#mainFont = pygame.font.Font(None, 12)
mainFont = pygame.font.Font(dirName + '/res/fonts/tahoma.ttf', 24)
text = mainFont.render(u'Hello привет, ребята!', 1, (0, 0, 0))
screen.blit(text, [10, 50])

screen.blit(text, [11, 51])

pygame.display.flip()

print(pygame.display.Info())

print(pygame.K_ESCAPE)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			arrayKeys = pygame.key.get_pressed()
			if arrayKeys[pygame.K_SPACE]:
				print("space pressed")
			if arrayKeys[pygame.K_ESCAPE]:
				running = False

pygame.quit()

"""
load params
init modules

while running:

"""