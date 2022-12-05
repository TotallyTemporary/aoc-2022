def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

def get_initial_state():
	# 9 lists
	stacks = [list() for _ in range(9)]
	for line in input_lines():
		if line == "\n": break
		# split line into 4 character sections: "[A] ", or "[Z]\n".
		split_lines = [line[i:i+4] for i in range(0, len(line), 4)]
		split_lines = [x.strip() for x in split_lines]
		for i, box in enumerate(split_lines):
			if box == "": continue # not all locations have boxes
			if box == "1": break   # we got to the end of the diagram
			_, char, _ = box
			stacks[i] += char
		
	# reverse stacks (we added from top-to-bottom)
	# stacks = [reversed(stack) for stack in stacks]
	# this reverse is not needed - the last added character is the first element.

	return stacks

def get_moves():
	moves = list()

	lines = iter(input_lines())
	# skip first part.
	for line in lines:
		if line != "\n": continue
		break

	# second part - moves
	for line in lines:
		_, x, _, y, _, z = line.split(" ") # really wish for a match statement right about now
		count = int(x); from_ = int(y)-1; to = int(z)-1 # to indices 
		moves.append([count, from_, to])

	return moves

# debug func
def print_stacks(stacks):
	print("-----")
	for i, stack in enumerate(stacks):
		print(f"{i}: {stack}")
	print("-----")

def main():
	stacks = get_initial_state()
	moves = get_moves()

	# part 1 debug.
	# stacks = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
	# moves = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
	# moves = [[x, y-1, z-1] for x, y, z in moves] # fix indices :)

	for count, from_, to in moves:
		for _ in range(count):
			# get and remove "from_" first item, put it in "to" first item.
			stacks[to].insert(0, stacks[from_].pop(0)) 
	
	# get top values of all stacks
	print("".join([stack[0] for stack in stacks]))

if __name__ == "__main__":
	main()