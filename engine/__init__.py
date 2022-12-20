'''
Engine
'''
__version__ = '0.1'

from engine.scene_handler import SceneHandler

class Engine:

	def __init__(self) -> None:
		self.scene = SceneHandler()

		self.load()

	def load(self) -> None:
		pass

	def run(self) -> None:
		for count, _ in enumerate(iter(bool, True)):
			self.draw()
			self.input()
			self.update()

	def draw(self) -> None:
		self.scene.draw()

	def input(self) -> None:
		self.scene.input()

	def update(self) -> None:
		self.scene.update()

