def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

def get_substrings_of_length(string, *, substring_length):
	return [string[index:index+substring_length] for index in range(0, len(string)-substring_length +1)]

def find_marker(string, *, slice_length):
	# divide the input into all possible (contiguous) 4/14 -character slices.
	slices = get_substrings_of_length(string, substring_length=slice_length)

	# go through all slices in order and find the first one where all character are unique.
	for index, slice in enumerate(slices):
		# if all elements are unique
		if len(set(slice)) == len(slice):
			return index+slice_length # add slice length because we want end of the marker


def main():
	# part 1
	sop_marker = find_marker(input_lines()[0], slice_length=4)
	print(sop_marker)

	# part 2
	message_marker = find_marker(input_lines()[0], slice_length=14)
	print(message_marker)

if __name__ == "__main__":
	main()