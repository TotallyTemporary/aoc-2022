from enum import Enum, auto

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value


def wins(our_hand, opp_hand):
	if our_hand == 'X' and opp_hand == 'C': return True
	if our_hand == 'Y' and opp_hand == 'A': return True
	if our_hand == 'Z' and opp_hand == 'B': return True
	return False

def ties(our_hand, opp_hand):
	if our_hand == 'X' and opp_hand == 'A': return True
	if our_hand == 'Y' and opp_hand == 'B': return True
	if our_hand == 'Z' and opp_hand == 'C': return True
	return False

def hand_points(our_hand):
	return {'X': 1, 'Y': 2, 'Z': 3}[our_hand]

def main():
	total_points = 0
	for line in input_lines():
		opp_hand, our_hand = line[:3].split(" ")

		if wins(our_hand, opp_hand): victory_points = 6
		elif ties(our_hand, opp_hand): victory_points = 3
		else: victory_points = 0

		total_points += (victory_points + hand_points(our_hand))
	
	print(total_points)


if __name__ == "__main__":
	main()