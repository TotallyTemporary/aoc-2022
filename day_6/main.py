def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

# sop=start of packet
def find_sop_marker(string, slice_length=4):


	slices = [string[index:index+slice_length] for index in range(0, len(string)-slice_length)]
	for index, slice in enumerate(slices):
		# length of (list) set 
		if len(set(slice)) == slice_length:
			return index+slice_length


def main():
	sop_marker = find_sop_marker(input_lines()[0])
	print(sop_marker)

if __name__ == "__main__":
	main()