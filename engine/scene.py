class Scene:

	def __init__(self) -> None:
		pass

	def draw(self) -> None:
		raise NotImplementedError

	def input(self) -> None:
		raise NotImplementedError

	def update(self) -> None:
		raise NotImplementedError