def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

class Knot():
	def __init__(self, location):
		self.location = location
		self.last_location = location
	
	def move(self, new_location):
		self.last_location = self.location
		self.location = new_location

	def possible_moves(self):
		lst = list() # could probably make with a generator expression
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				lst.append((self.location[0]+dx, self.location[1]+dy))
		return lst

	def is_8_neighbor(self, other):
		dx = int(abs(self.location[0] - other.location[0]))
		dy = int(abs(self.location[1] - other.location[1]))
		if (
			dx <= 1 and
			dy <= 1
		): return True
		else: return False
	
	def is_4_neighbor(self, other):
		dx = int(abs(self.location[0] - other.location[0]))
		dy = int(abs(self.location[1] - other.location[1]))
		if dx == 0 and dy == 1: return True
		if dx == 1 and dy == 0: return True
		return False

	# los=line of sight
	def is_within_los(self, other):
		dx = int(abs(self.location[0] - other.location[0]))
		dy = int(abs(self.location[1] - other.location[1]))
		if dx == 0 or dy == 0: return True
		return False

def print_board(tail_visited_locations, head, tail):
	x_range = (-20, 20)
	y_range = (-20, 20)

	print("-"*(x_range[1] - x_range[0]))
	for y in range(*y_range):
		for x in range(*x_range):
			char = "#" if (x, y) in tail_visited_locations else "."
			if (x, y) == (0, 0): char = "s"
			
			for i, knot in enumerate([head, *tail]):
				if (x, y) == knot.location:
					char = i

			print(char, end="")
		print()
	print("-"*(x_range[1] - x_range[0]))

# tail always follows head ; if head is no longer neighbor of tail, move tail to where head used to be.
def main():
	is_part_1 = True

	start_pos = (0, 0)
	head = Knot(start_pos)

	if is_part_1:
		tail = [ Knot(start_pos) ]
	else:
		tail = [ Knot(start_pos) for _ in range(9) ]

	tail_visited_locations = { start_pos }

	for line in input_lines():
		dir, count = line.split(" ") ; count = int(count)
		print(dir, count)
		for _ in range(count):
			match dir: # move head
				case "U":
					head.move( (head.location[0], head.location[1]+1) )

				case "D":
					head.move( (head.location[0], head.location[1]-1) )


				case "R":
					head.move( (head.location[0]+1, head.location[1]) )

				case "L":
					head.move( (head.location[0]-1, head.location[1]) )

				case x: 
					print(f"Unrecognized direction {x}")
					assert 0 == 1

			for i, knot in enumerate(tail):
				if i == 0: front = head
				else: front = tail[i-1]

				if not front.is_8_neighbor(knot):
					# we have to move!

					# if the front knot is directly in front of us, we just go where they came from.
					if front.is_within_los(knot):
						knot.move(front.last_location)
						continue
					
					# first check for 4-moves
					for possible_move in knot.possible_moves():
						if Knot(possible_move).is_4_neighbor(front):
							knot.move(possible_move)
							break
					else:
						# then check 8-moves
						for possible_move in knot.possible_moves():
							if Knot(possible_move).is_8_neighbor(front):
								knot.move(possible_move)
								break

			tail_visited_locations.add(tail[-1].location)

	print_board(tail_visited_locations, head, tail)
	print(len(tail_visited_locations))

if __name__ == "__main__":
	main()