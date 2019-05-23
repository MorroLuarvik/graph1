import os, json, pygame, sys, time

class Env:
	FONT_PATH = "/res/fonts/tahoma.ttf"
	DEF_WIDTH = 800
	DEF_HEIGHT = 600
	FPS = 60;

	prevTimeMark = time.time()
	timeDelta = 0.1

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([800, 600])

		self.timeDelta = 1 / float(self.FPS)
		
		dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))
		print("dirName: " + dirName)
		print("ownFileName: " + ownFileName)

	def getControls(self):
		""" get current controls """

		controlEvents = {}

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				controlEvents['Exit'] = True
			if event.type == pygame.KEYDOWN:
				arrayKeys = pygame.key.get_pressed()
				#if arrayKeys[pygame.K_SPACE]:
				#	print("space pressed")
				if arrayKeys[pygame.K_ESCAPE]:
					controlEvents['Exit'] = True

		return controlEvents

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