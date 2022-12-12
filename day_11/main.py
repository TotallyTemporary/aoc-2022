def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.read().splitlines()
	return return_value

# this would be horrible in any serious application
# but it's 2 in the morning and i have just a couple of hours to get this going
def parse_expression(expr):
	return lambda old: eval(expr)

# finally got python 3.11 working!
def get_monkey_num(line):
	match line.strip().split(" "):
		case ["Monkey", monkey_num]:
			return int(monkey_num.replace(":", ""))
		case x:
			raise ValueError(f"{x} is not a valid monkey line")

def get_items(line):
	match line.strip().split(" "):
		case ["Starting", "items:", *items]: # items = ["79,", "98"]
			return [int(s.replace(",", "")) for s in items]
		case x:
			raise ValueError(f"{x} is not a valid starting items line")

def get_op(line):
	match line.strip().split(" "):
		case ["Operation:", "new", "=", left, op, right]:
			return parse_expression(" ".join([left, op, right]))
		case x:
			raise ValueError(f"{x} is not a valid operation line")

def get_test(line):
	match line.strip().split(" "):
		case ["Test:", "divisible", "by", remainder]:
			remainder = int(remainder)
			return remainder
		case x:
			raise ValueError(f"{x} is not a valid test line")

def get_condition(line):
	match line.strip().split(" "):
		case ["If", _true_or_false, "throw", "to", "monkey", money_num]:
			return int(money_num)
		case x:
			raise ValueError(f"{x} is not a valid condition line")

class Monkey():
	def __init__(self, number, items, operation, test, if_true, if_false):
		self.number = number
		self.items = items
		self.operation = operation
		self.test = test
		self.if_true = if_true
		self.if_false = if_false

		self.inspect_count = 0

	def __repr__(self):
		return f"{self.number}: {self.inspect_count}"

def main():
	# add one extra line in the end so all monkeys have an empty line separating them.
	lines = iter([*input_lines(), ""]) 

	# parse monkeys
	monkeys = list()
	try:
		while True:
			num = get_monkey_num(next(lines))
			items = get_items(next(lines))
			op_func = get_op(next(lines))
			test = get_test(next(lines))
			if_true = get_condition(next(lines))
			if_false = get_condition(next(lines))
			assert next(lines) == ""

			monkeys.append(Monkey(num, items, op_func, test, if_true, if_false))
	except StopIteration:
		pass

	# now run the monkeys simulation
	ROUNDS = 20

	for _ in range(ROUNDS):
		for monkey in monkeys:
			for item in [*monkey.items]:
				# inspect this item
				monkey.inspect_count += 1
				new_worry = monkey.operation(item) // 3

				if new_worry % monkey.test == 0:
					pass_monkey = monkey.if_true
				else:
					pass_monkey = monkey.if_false
				
				# remove item from ´monkey´ and pass it to ´pass_monkey´
				monkey.items.remove(item)
				monkeys[pass_monkey].items.append(new_worry)

	# after simulation

	two_best_inspected = sorted([m.inspect_count for m in monkeys])[-2:]
	print(f"Monkey business: { two_best_inspected[0] * two_best_inspected[1] }")


if __name__ == "__main__":
	main()