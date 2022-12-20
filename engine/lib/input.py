import sys

class Choice:

	def __init__(self, options: dict) -> None:
		self.entered = None
		self.choice = None
		self.options = options if options else {"Quit" : "close"}

	def draw(self) -> None:
		for count, item in enumerate(self.options, 1):
			print(f"{str(count)}) {item}")
	
	def input(self)  -> None:
		try:
			self.entered = int(input("Option: "))
			if not self.entered <= len(self.options):
				self.entered = None
		except:
			print("Please enter a number!")
			self.input()

	def update(self) -> any:
		try:
			if self.entered is not None:
				self.choice = list(self.options.values())[self.entered -1]
				if self.choice == "close":
					self.close()
				else:
					return self.choice
			else:
				print("Please enter a number in range!")
		except ValueError:
			print("Please enter a number!")	

	def close(self):
		responce = input("Do you want to quit? [y/n] ")
		if responce.lower() in ["y", "yes"]:
			sys.exit(0)