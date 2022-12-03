def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value


_lowercase = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1, 26 +1)))
_uppercase = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(27, 52 +1)))
priority_map = {**_lowercase, **_uppercase}

def priority(char):
	return priority_map[char]

def to_comps(line):
	# get compartments
	first_comp = line[:len(line)//2]
	second_comp = line[len(line)//2:]
	return first_comp, second_comp

def get_common_item(first_comp, second_comp):
	# get items in both compartments
	both_comps_items = set.intersection(\
		set(first_comp),\
		set(second_comp))

	# there should be only 1 common item.
	assert len(both_comps_items), 1
	common_item = list(both_comps_items)[0]
	return common_item

def main():
	priority_sum = 0
	for line in input_lines():
		first_comp, second_comp = to_comps(line)
		common_item = get_common_item(first_comp, second_comp)
		char_priority = priority(common_item)

		priority_sum += char_priority
	print(priority_sum)

if __name__ == "__main__":
	main()