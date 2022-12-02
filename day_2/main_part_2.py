from enum import Enum, auto

def input_lines():
	with open("./input.txt", "r") as file:
		return_value = file.readlines()
	return return_value

def get_hand_points(hand):
	return {'A': 1, 'B': 2, 'C': 3}[hand]

def get_our_hand(opp_choice, game_end):
	if game_end == 'Y': return opp_choice
	if game_end == 'X':
		return {'A': 'C', 'B': 'A', 'C': 'B'}[opp_choice]
	if game_end == 'Z':
		return {'A': 'B', 'B': 'C', 'C': 'A'}[opp_choice]


def main():
	total_points = 0
	for line in input_lines():
		opp_choice, game_end = line[:3].split(" ")
		our_hand = get_our_hand(opp_choice, game_end)

		if game_end == 'X': victory_points = 0
		if game_end == 'Y': victory_points = 3
		if game_end == 'Z': victory_points = 6
		
		total_points += (victory_points + get_hand_points(our_hand))

	print(total_points)



if __name__ == "__main__":
	main()