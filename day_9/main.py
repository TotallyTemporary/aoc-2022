def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value
	
# I'm not all too familiar with python oop
# please forgive the bad formatting.

class Direction():
	def __init__(self, width, height):
		self.width = width
		self.height = height

class Up(Direction):
	def __init__(self, width, height):
		super().__init__(width, height)

	def is_edge(self, index: int): 
		return (index // self.width == 0)

	def move(self, index: int):
		return index - self.width

class Down(Direction):
	def __init__(self, width, height):
		super().__init__(width, height)

	def is_edge(self, index: int): 
		return (index // self.width == self.height-1)

	def move(self, index: int):
		return index + self.width

class Left(Direction):
	def __init__(self, width, height):
		super().__init__(width, height)

	def is_edge(self, index: int): 
		return (index % self.width == 0)

	def move(self, index: int):
		return index - 1

class Right(Direction):
	def __init__(self, width, height):
		super().__init__(width, height)

	def is_edge(self, index: int): 
		return ((index+1) % self.width == 0)

	def move(self, index: int):
		return index + 1

def main():
	lines = input_lines()
	width = len(lines[0]) ; height = len(lines) ; size = width*height
	def is_in_bounds(index):
		return index >= size or index < 0

	map = "".join(lines) # all lines together
	directions = [ Up(width, height), Down(width, height), Left(width, height), Right(width, height) ]

	def is_visible(index: int):
		value = map[index]
		for direction in directions:
			working_index = index
			while not direction.is_edge(working_index):
				working_index = direction.move(working_index)

				if map[working_index] >= value: # a tree is blocking the way somewhere here.
					break
			else: # gets run if tree never blocked us
				return True
		
		return False # ret false is trees blocked in all directions

	s = 0
	for index in range(size):
		if is_visible(index): s += 1
	print(s)


if __name__ == "__main__":
	main()