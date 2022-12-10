def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

reg_X = 1
cycles = 0

important_sum = 0

def main():
	global cycles, reg_X, important_sum

	def increase_clock(count):
		global cycles, reg_X, important_sum

		for _ in range(count):
			cycles += 1

			# part 1
			if (cycles-20) % 40 == 0:
				important_sum += (cycles * reg_X)

	for line in input_lines():
		args = line.split(" ")
		match args[0]:
			case "noop":
				increase_clock(1)
				continue

			case "addx":
				increase_clock(2)
				_, value = args ; value = int(value)
				reg_X += value
				continue

			case x: print(x)
	print(f"part 1 sum: {important_sum}")

if __name__ == "__main__":
	main()