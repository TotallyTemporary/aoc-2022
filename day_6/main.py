def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

def find_marker(string, *, slice_length):
	# divide a string into all its [slice_length] -length substrings
	slices = [string[index:index+slice_length] for index in range(0, len(string)-slice_length)]

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