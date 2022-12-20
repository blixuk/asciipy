from engine.scene import Scene
from engine.lib.input import Choice

class Scene(Scene):

	def __init__(self) -> None:
		self.choice = Choice({
				"Start" : "new_game",
				"Quit" : "close"
			})

	def draw(self) -> None:
		self.choice.draw()

	def input(self) -> None:
		self.choice.input()

	def update(self) -> None:
		option = self.choice.update()
		print(option)
