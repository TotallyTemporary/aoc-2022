import string

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

priority_map = {
	**dict(zip(string.ascii_letters, range(1, 52 +1))),\
	' ': 0	
}
print(priority_map)

def priority(char):
	return priority_map[char]

def main():
	priority_sum = 0
	badge_sum = 0
	input_list = input_lines() # reads file

	# splits input_list into groups of 3
	groups = [input_list[x:x+3] for x in range(0, len(input_list), 3)]

	# do for every group (solve part 2)
	for group in groups:
		# get badge
		badge = set.intersection(*[set(s) for s in group]).pop()
		badge_sum += priority(badge)

		# do for every line (solve part 1)
		for line in group:
			# get compartments
			first_comp  = line[:len(line)//2]
			second_comp = line[len(line)//2:]

			common_item = set.intersection(set(first_comp), set(second_comp)).pop()
			priority_sum += priority(common_item)

	print(priority_sum, badge_sum)

if __name__ == "__main__":
	main()