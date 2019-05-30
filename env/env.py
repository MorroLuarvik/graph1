import os, json, pygame, sys, time

class Env:
	FONT_PATH = "/res/fonts/tahoma.ttf"
	DEF_WIDTH = 800
	DEF_HEIGHT = 600
	FPS = 60

	prevTimeMark = time.time()
	timeDelta = 0.1

	controlEvents = {}
	events = {}

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([self.DEF_WIDTH, self.DEF_HEIGHT])

		self.timeDelta = 1 / float(self.FPS)
		
		"""
		dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))
		print("dirName: " + dirName)
		print("ownFileName: " + ownFileName)
		"""

	def getControls(self):
		""" get current controls """

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.controlEvents['Exit'] = True
			
			if event.type == pygame.KEYUP:
				self.__clearEvent(event.key)

				"""
				if event.key == pygame.K_UP:
					

				if event.key == pygame.K_DOWN:
					self.__clearEvent('bg_darker')
				"""

				"""
				#if arrayKeys[pygame.K_UP] and arrayKeys[pygame.K_DOWN]:
				print(event.key)
				print('K_UP' + str(pygame.K_UP))
				print('K_DOWN' + str(pygame.K_DOWN))
				"""
				

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.controlEvents['Exit'] = time.time()

					self.events[event.key] = time.time()
				
				"""
				if event.key == pygame.K_UP:
					self.events['bg_lighter'] = time.time()

				if event.key == pygame.K_DOWN:
					self.events['bg_darker'] = time.time()
				"""

				#print(event.key)
				#print('down K_UP' + str(pygame.K_UP))
				#print('down K_DOWN' + str(pygame.K_DOWN))

				#arrayKeys = pygame.key.get_pressed()
				#if arrayKeys[pygame.K_SPACE]:
				#	print("space pressed")
				#if arrayKeys[pygame.K_ESCAPE]:
				#	self.controlEvents['Exit'] = True

				"""
				if event.key == pygame.K_UP:
					self.controlEvents['bg_lighter'] = True
				if event.key == pygame.K_DOWN:
					self.controlEvents['bg_lighter'] = False
				"""

			maxTime = 0
			resultEvent = None
			for event in self.events:
				if self.events[event] > maxTime:
					maxTime = self.events[event]
					resultEvent = event

		print(self.events)

		return self.controlEvents

	def __clearEvent(self, eventName):
		""" remove eventName from self.controlEvents """

		if eventName in self.controlEvents:
			self.events.pop(eventName)


	def displayItems(self, items):
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

	def hasExitEvent(self, controls):
		""" get exit event in controls """
		if 'Exit' in controls:
			return controls['Exit']

		return False

	def quit(self):
		pygame.quit()