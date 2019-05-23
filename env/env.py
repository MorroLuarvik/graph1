import os, json, pygame, sys

class Env:
	FONT_PATH = "/res/fonts/tahoma.ttf"
	DEF_WIDTH = 800
	DEF_HEIGHT = 600

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([800, 600])

		#dirName, ownFileName = os.path.split(os.path.abspath(__file__))
		dirName, ownFileName = os.path.split(os.path.abspath(sys.argv[0]))
		print("dirName: " + dirName)
		print("ownFileName: " + ownFileName)
		print(os.path.sep)
		print sys.argv[0].split(os.path.sep)

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

	def displayObjects(self, objects):
		""" show objects in application window """

		pygame.display.flip()
		return

	def delay(self):
		""" delay execute by FPS setting """
		return

	def hasExitEvent(self, controls):
		""" get exit event in controls """
		if 'Exit' in controls:
			return controls['Exit']

		return False

	def quit(self):
		pygame.quit()