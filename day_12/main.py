import string

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

# copied from day 8.
# these "direction" classes simply allow me to deal with a single-dimensional array rather than a 2d array.
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

# get all possible neighbors of an index
def neighbors(index, directions):
	return [dir.move(index) for dir in directions if not dir.is_edge(index)]

# this class is mutated by the bfs.
class Cell():
	def __init__(self, index, value, is_end=False):
		self.index = index
		self.value = value
		self.is_end = is_end

		self.searched = False
		self.parent = None

	def __repr__(self):
		return f"{self.index}"

def main():
	lines = input_lines()
	width = len(lines[0]) ; height = len(lines)
	directions = [ Left(width, height), Right(width, height), Up(width, height), Down(width, height) ]

	# find start and end
	input_string = "".join(input_lines())
	for index, value in enumerate(input_string):
		if value == "S": start_position = index
		if value == "E": end_position = index

	# make input string into cells
	def _make_cell(index, char, start_position, end_position): 
		if index == start_position: return Cell(index, ord('a'))
		if index == end_position: return Cell(index, ord('z'), is_end=True)
		return Cell(index, ord(char))
	input = [_make_cell(index, value, start_position, end_position) for index, value in enumerate(input_string)]

	# perform breadth-first-search
	# big thanks to https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode 
	search_list = [ input[start_position] ] # positions we need to search
	input[start_position].searched = True

	while len(search_list) != 0:
		cell = search_list.pop()
		if cell.is_end: break
		for neighbor in [input[pos] for pos in neighbors(cell.index, directions)]:
			if neighbor.searched: pass #print(f"{neighbor} already searched.")
			elif neighbor.value > (cell.value + 1): pass #print(f"{neighbor} is too high {neighbor.value}, {cell.value}")
			else:
				neighbor.searched = True
				neighbor.parent = cell

				search_list.insert(0, neighbor)

	# make the path from end to start
	path = [ input[end_position] ]
	while path[-1].parent != None:
		path.append(path[-1].parent)

	# print the map
	i = 0
	for y in range(height):
		for x in range(width):
			char = lines[y][x]
			if i in [cell.index for cell in path]: char = "#"
			print(char, end="")
			i += 1
		print()
	
	# print the length of the path (part 1 answer)
	print(f"{path=}, length={len(path)-1}") # why it's off by one i don't know.

if __name__ == "__main__":
	main()