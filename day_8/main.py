from math import prod

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

	def trees_visible_in_dir(index: int, direction: Direction):
		value = map[index]

		working_index = index   # stepper
		visible_count = 0       # stepper
		while not direction.is_edge(working_index):
			working_index = direction.move(working_index)
			visible_count += 1
			if map[working_index] >= value:
				break
		return visible_count

	def scenic_score(index: int):
		return prod([trees_visible_in_dir(index, dir) for dir in directions])

	'''#solves part 1
	s = 0
	for index in range(size):
		if is_visible(index): s += 1
	print(s)
	'''

	# solves part 2
	best = -10000 # get best scenic score of all indices
	for index in range(size):
		best = max(best, scenic_score(index))
	print(best)

if __name__ == "__main__":
	main()