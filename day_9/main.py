def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

def are_neighbors(pos1, pos2):
	if (
		int(abs(pos1[0] - pos2[0])) <= 1 and
		int(abs(pos1[1] - pos2[1])) <= 1
		):
		return True
	else: return False

# tail always follows head ; if head is no longer neighbor of tail, move tail to where head used to be.
def main():
	head = (0, 0)
	tail = (0, 0)
	tail_visited_locations = { tail }

	for line in input_lines():
		dir, count = line.split(" ") ; count = int(count)
		print(dir, count)
		for _ in range(count):
			last_head_pos = (head[0], head[1])

			match dir: # move head
				case "U":
					head = (head[0], head[1]+1)
					
				case "D":
					head = (head[0], head[1]-1)
					

				case "R":
					head = (head[0]+1, head[1])
					
				case "L":
					head = (head[0]-1, head[1])

				case x: 
					print(f"Unrecognized direction {x}")
					assert 0 == 1
			
			if not are_neighbors(head, tail):
				tail = last_head_pos
			tail_visited_locations.add( tail )
	
	print(len(tail_visited_locations))

if __name__ == "__main__":
	main()