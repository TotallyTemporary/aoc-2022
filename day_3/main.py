import string

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

priority_map = {
	**dict(zip(string.ascii_letters, range(1, 52 +1))),\
	' ': 0	
}
print(priority_map)

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
	badge_sum = 0

	possible_group_characters = set(' ')
	for i, line in enumerate(input_lines() + ["  "]):
		if i % 3 == 0: # end last group, then start new one.
			assert len(possible_group_characters), 1
			group_badge = list(possible_group_characters)[0]
			badge_sum += priority(group_badge)
			print(group_badge, priority(group_badge))
			# reset
			possible_group_characters = set(string.ascii_letters)
		print(line)
		# solve second problem
		possible_group_characters = set.intersection( \
			possible_group_characters, \
			set(line)
		)

		# solve first problem
		first_comp, second_comp = to_comps(line)
		common_item = get_common_item(first_comp, second_comp)
		char_priority = priority(common_item)

		priority_sum += char_priority
	print(priority_sum)
	print(badge_sum)

if __name__ == "__main__":
	main()