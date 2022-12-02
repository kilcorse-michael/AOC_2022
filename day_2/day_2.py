#day_2 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_2/day_2.txt", "./day_2/day_2_min.txt"

LOSS_CONDITION = [{"A", "Z"}, {"B", "X"}, {"C", "Y"}]
DRAW_CONDITION = [{"A", "X"}, {"B", "Y"}, {"C", "Z"}]
WIN_CONDITION = [{"A", "Y"}, {"B", "Z"}, {"C", "X"}]

SCORE = 0

with open(TEST_DATA) as f:
	strategy_sheet = [set(rounds.split()) for rounds in f.read().split("\n")]

def find_score(sheet):
	new_list = []
	for x in sheet:
		for y in LOSS_CONDITION:
			if x != y:
				new_list.append(x)
				break
	return new_list

print(find_score(strategy_sheet))