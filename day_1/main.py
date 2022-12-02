def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value


def main():
	current_sum = 0
	elves: List[Int] = list()

	# parse file to calories carried by elves
	for line in input_lines():
		if line.isspace():
			elves.append(current_sum)
			current_sum = 0
		else:
			current_sum += int(line)

	# print part 1: elf with most calories and part 2: sum of calories carried by top 3 elves.
	print(f"best: {max(elves)}") # get best
	print(f"sum of top 3: {sum(sorted(elves)[-3:])}") # sum of top 3


if __name__ == "__main__":
	main()