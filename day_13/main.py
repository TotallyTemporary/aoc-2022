from enum import Enum
from functools import cmp_to_key

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

class Parser():
	def __init__(self, input: str):
		self.input = input
		self.index = 0

	# try move forward 1 ; returns true if we advanced, false otherwise
	def advance(self):
		self.index += 1
		if self.index >= len(self.input):
			self.index = len(self.input)
			return False
		return True

	# helper funcs
	def current(self): return self.input[self.index]
	def error(self, expected): raise ValueError(f"Excepted {expected} at {self.index} but got {self.current()}")

	def parse(self):
		return self._parse_object()

	# parses int or list, depending on which one is at current index
	def _parse_object(self):
		if self.current() == "[": return self._parse_list()
		elif self.current().isdigit(): return self._parse_int()
		else: self.error("list or digit")
	
	def _parse_list(self):
		if self.current() != "[": self.error("[")
		self.advance()

		lst = list()
		while self.current() != "]":
			lst.append(self._parse_object())
			if self.current() == ",": self.advance()
		self.advance()
		return lst

	def _parse_int(self):
		start = self.index
		while (self.current().isdigit() and self.advance()): pass # stop when no longer digit or end of input
		end = self.index
		return int(self.input[start:end])
	
# left gt right = -1
# left lt right = 1
# equal         = 0
def compare(left, right):
	# if one type is int and another is list, convert int to list and then compare.
	if type(left) == int  and type(right) == list: left  = [left]
	if type(left) == list and type(right) ==  int: right = [right]

	# compare ints
	if type(left) == int: return right - left

	# compare lists element by element
	if type(left) == list:
		for el_left, el_right in zip(left, right):
			result = compare(el_left, el_right)
			if result != 0: return result # keep iterating if comparisons are equal.
		
		# we're out of elements, see which one ran out first
		return len(right) - len(left)

def main():
	input = iter(input_lines())

	# begin part 1
	pair_indices_sum = 0
	try:
		for index in range(1, 99999999):
			left = Parser(next(input)).parse()
			right = Parser(next(input)).parse()

			result = compare(left, right)
			if result > 0: pair_indices_sum += index

			next(input) # get rid of the empty line
	except StopIteration:
		pass

	print("Part 1 solution:", pair_indices_sum)

	# part 2
	input = iter(input_lines())
	all_packets = list()
	try:
		while True: # keep iterating until we hit end of file
			all_packets.append(Parser(next(input)).parse())
			all_packets.append(Parser(next(input)).parse())
			next(input)
	except StopIteration:
		pass

	all_packets.append(divider_1 := [[2]])
	all_packets.append(divider_2 := [[6]])
	
	# sort packets by comparison
	packets_sorted = sorted(all_packets, key=cmp_to_key(lambda left, right: -compare(left, right)))

	# multiply the indices of the dividers (+1 because first item is not index 0 but index 1)
	print("part 2 solution:", (packets_sorted.index(divider_1)+1) * (packets_sorted.index(divider_2)+1))

if __name__ == "__main__":
	main()