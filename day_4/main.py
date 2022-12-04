def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

def fully_contains_the_other(first, second):
	if all([(x in second) for x in first]): return True
	if all([(x in first) for x in second]): return True
	return False

def first_contains_second(first, second):
	f1, f2 = first; s1, s2 = second

	if not f1 < s1: return False
	if not f2 > s2: return False
	return True

def main():
	containment_sum = 0
	for line in input_lines():
		ranges = line.split(",")
		first1, first2 = map(lambda x: int(x), ranges[0].split("-"))
		second1, second2 = map(lambda x: int(x), ranges[1].split("-"))

		first = set(range(first1, first2 +1))
		second = set(range(second1, second2 +1))

		if first.issubset(second) or second.issubset(first):
			containment_sum += 1
	
	print(containment_sum)

if __name__ == "__main__":
	main()