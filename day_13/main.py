from enum import Enum
from functools import cmp_to_key

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

class Parser():
	def __init__(self, input: str):
		self.input = input # input string
		self.index = 0

	# returns true if we advanced, false otherwise
	def advance(self):
		self.index += 1
		if self.index >= len(self.input):
			self.index = len(self.input)
			return False
		return True

	def current(self):
		return self.input[self.index]

	def error(self, expected):
		raise ValueError(f"Excepted {expected} at {self.index} but got {self.current()}")

	def parse(self):
		return self._parse_object()

	def _parse_object(self):
		if self.current() == "[": return self._parse_list()
		elif self.current().isdigit(): return self._parse_int()
		else: self.error("digit")

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
		while (self.current().isdigit() and self.advance()): pass
		end = self.index
		return int(self.input[start:end])

class ComparisonResult(Enum):
	left_lt_right = 0
	left_gt_right = 1
	equal         = 2
	

def compare(left, right):
	if type(left) == int and type(right) == list:
		left = [left]
	if type(left) == list and type(right) == int:
		right = [right]


	if type(left) == int:
		if left < right:   return ComparisonResult.left_lt_right
		elif left > right: return ComparisonResult.left_gt_right
		else:              return ComparisonResult.equal

	if type(left) == list:
		for el_left, el_right in zip(left, right):
			result = compare(el_left, el_right)
			if   result == ComparisonResult.left_lt_right: return ComparisonResult.left_lt_right
			elif result == ComparisonResult.left_gt_right: return ComparisonResult.left_gt_right
			else: pass # keep iterating if comparisons are equal.
		
		# we have made it to the end of one of the lists without a differing element
		if   len(left) < len(right): return ComparisonResult.left_lt_right
		elif len(left) > len(right): return ComparisonResult.left_gt_right
		else:                        return ComparisonResult.equal

def main():
	input = iter(input_lines())

	# begin part 1
	pair_index = 1
	pair_indices_sum = 0
	try:
		while True:
			left = Parser(next(input)).parse()
			right = Parser(next(input)).parse()

			match compare(left, right):
				case ComparisonResult.left_lt_right:
					pair_indices_sum += pair_index
				case ComparisonResult.left_gt_right | ComparisonResult.equal:
					pass 

			pair_index += 1		

			next(input) # get rid of the empty line
	except StopIteration:
		pass

	print("Part 1 solution:", pair_indices_sum)

	# part 2
	input = iter(input_lines())
	all_packets = list()
	try:
		while True:
			all_packets.append(Parser(next(input)).parse())
			all_packets.append(Parser(next(input)).parse())
			next(input)
	except StopIteration:
		pass

	divider_1 = [[2]]
	divider_2 = [[6]]
	all_packets.append(divider_1)
	all_packets.append(divider_2)

	def sorting_comp(left, right):
		match compare(left, right):
			case ComparisonResult.left_lt_right:
				return -1
			case ComparisonResult.left_gt_right:
				return 1
			case ComparisonResult.equal:
				return 0
	
	packets_sorted = sorted(all_packets, key = cmp_to_key(sorting_comp))
	print("part 2 solution:", (packets_sorted.index(divider_1)+1) * (packets_sorted.index(divider_2)+1))

if __name__ == "__main__":
	main()