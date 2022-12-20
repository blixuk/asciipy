import importlib
import os

from engine.lib.stack import Stack

class SceneHandler:

	SCENES = {}
	STACK = Stack()
	CURRENT = None

	def __init__(self) -> None:
		self.load()

	def load(self) -> None:
		for name in os.listdir("scenes"):
			path = f"scenes/{name}"
			if os.path.isfile(path):
				basename = os.path.basename(path)
				base, extension = os.path.splitext(path)
				if extension == ".py" and not basename.startswith("_"):
					name = name[:-3]
					module = importlib.import_module(base.replace("/", "."))
					SceneHandler.SCENES[name] = module.Scene
	
	def _is_scene(self, name) -> bool:
		return True if name in SceneHandler.SCENES else Exception(f"Scene '{name}' Doesn't exist!")

	def push(self, name:str) -> None:
		if self._is_scene(name):
			SceneHandler.STACK.push(SceneHandler.SCENES[name])
			SceneHandler.CURRENT = self.peek()()
	
	def pop(self) -> None:
		SceneHandler.STACK.pop()

	def peek(self, pointer:int = -1) -> any:
		return SceneHandler.STACK.peek(pointer)

	def draw(self) -> None:
		SceneHandler.CURRENT.draw()

	def input(self) -> None:
		SceneHandler.CURRENT.input()

	def update(self) -> None:
		SceneHandler.CURRENT.update()
