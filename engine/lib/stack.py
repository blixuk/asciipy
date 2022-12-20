class Stack:

	def __init__(self) -> None:
		self.STACK = []

	def __call__(self) -> None:
		print(self.STACK) 
	
	def push(self, item: any) -> None:
		self.STACK.append(item)

	def __add__(self, item: any) -> None:
		self.STACK.append(item)
	
	def __setitem__(self, pointer: int, item: any) -> None:
		try:
			if len(self.STACK) >= pointer:
				self.STACK[pointer] = item
		except:
			return None
	
	def pop(self) -> None:
		if len(self.STACK) > 0:
			del self.STACK[-1:]

	def __sub__(self, count: int) -> None:
		if len(self.STACK) >= count:
			del self.STACK[-count:]

	def __del__(self) -> None:
		if len(self.STACK) > 0:
			del self.STACK[-1:]

	def __getitem__(self, pointer: int) -> any:
		try:
			if len(self.STACK) >= pointer:
				return self.STACK[pointer]
		except:
			return None
	
	def peek(self, pointer: int = -1) -> any:
		try:
			if len(self.STACK) >= pointer:
				return self.STACK[pointer]
		except:
			return None
	
	def __contains__(self, item: any) -> any:
		return item in self.STACK
	
	def empty(self):
		return self.STACK == []
	
	def count(self) -> int:
		return len(self.STACK)
	
	def __len__(self) -> int:
		return len(self.STACK)
	
	def stack(self) -> list:
		return self.STACK

	def __repr__(self) -> str:
		return str(self.STACK)

	def __str__(self) -> str:
		return str(self.STACK)[1:-1]
	
	def dump(self) -> None:
		self.STACK.clear()

	def iter(self) -> any:
		for item in reversed(self.STACK):
			yield item
	
	def __iter__(self) -> any:
		while self.STACK:
			yield self.STACK.pop()

	def reverse(self) -> list:
		return self.STACK[::-1]

	def __reversed__(self) -> list:
		return self.STACK[::-1]

	def __eq__(self, item: any) -> bool:
		return self.STACK == item

	def __lt__(self, item: any) -> bool:
		return self.STACK < item

	def __le__(self, item: any) -> bool:
		return self.STACK <= item

	def __gt__(self, item: any) -> bool:
		return self.STACK > item

	def __ge__(self, item: any) -> bool:
		return self.STACK >= item

	def __ne__(self, item: any) -> bool:
		return self.STACK != item
