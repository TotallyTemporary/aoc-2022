from collections import namedtuple
Point = namedtuple("Point", "x y")

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

class World():
	def __init__(self, coords):
		self.world_map = coords
		self.bounds = find_bounds(coords)

	def print(self):
		for y in range(0, self.bounds.max_y):
			for x in range(self.bounds.min_x, self.bounds.max_x +1):
				if (x, y) == (500, 0):
					print("S", end="")
					continue
				print("#" if self.is_obstacle(x, y) else ".", end="")
			print()
	
	def is_obstacle(self, x, y):
		return Point(x, y) in self.world_map

	def is_in_bounds(self, x, y):
		if x < self.bounds.min_x: return False
		if x > self.bounds.max_x: return False
		# if y < self.bounds.min_y: return False # sand spawns high up, don't delete. 
		if y > self.bounds.max_y: return False
		return True

	def part_1_simulate_all(self):
		count = 0
		while not self.part_1_simulate(): 
			count += 1
		return count
		
	# returns True if fell out of map, returns False if stuck.
	def part_1_simulate(self):
		start_location = (500, 0)
		pos = start_location

		while self.is_in_bounds(*pos):
			x, y = pos
			# if nothing below, move down
			if not self.is_obstacle(x, y+1):
				pos = (x, y+1)
				continue
			
			# try move diagonally left
			if not self.is_obstacle(x-1, y+1):
				pos = (x-1, y+1)
				continue

			# try move diagonally right
			if not self.is_obstacle(x+1, y+1):
				pos = (x+1, y+1)
				continue

			# we are stuck.
			self.world_map.add(Point(*pos))
			return False
		return True

# find the min and max  x and y coordinates
def find_bounds(coords):
	min_x = min_y = 1000000 ; max_x = max_y = -1000000

	for point in coords:
		min_x = min(min_x, point.x) ; max_x = max(max_x, point.x)
		min_y = min(min_y, point.y) ; max_y = max(max_y, point.y)
	Bounds = namedtuple("Bounds", "min_x min_y max_x max_y")
	return Bounds(min_x, min_y, max_x, max_y)

def main():
	coords = set()

	for input_line in input_lines():
		points = [Point(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in input_line.split(" -> ")] # list of Points
		lines = [(points[i], points[i+1]) for i in range(len(points)-1)] # tuple of two Points

		for p1,p2 in lines:
			if p1.x == p2.x:
				for y in range(min(p1.y, p2.y), max(p1.y, p2.y) +1):
					coords.add(Point(p1.x, y))
				continue

			if p1.y == p2.y:
				for x in range(min(p1.x, p2.x), max(p1.x, p2.x) +1):
					coords.add(Point(x, p1.y))
				continue

			raise ValueError(f"{p1} and {p2} did not have the same x or y. Diagonal lines not supported")
		

	world = World(coords)
	world.print()
	print(f"Part 1 solution: {world.part_1_simulate_all()}")
	world.print()

if __name__ == "__main__":
	main()