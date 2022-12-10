def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

reg_X = 1
cycles = 0
crt_line = ""

important_sum = 0

def main():
	global cycles, reg_X, important_sum, crt_line

	def increase_clock(count):
		global cycles, reg_X, important_sum, crt_line

		for _ in range(count):
			cycles += 1
			crt_position = (cycles % 40)
			
			# part 2
			if crt_position == 0:
				print(crt_line)
				crt_line = ""
			if 0 <= (crt_position - reg_X) <= 2:
				char = "█"
			else: char = "."
			
			crt_line += char
			# print(crt_position, cycles, reg_X, crt_line)

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