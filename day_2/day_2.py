#day_2 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_2/day_2.txt", "./day_2/day_2_min.txt"

conditions = {"loss": (("A", "Z"), ("B", "X"), ("C", "Y")), "draw":(("A", "X"), ("B", "Y"), ("C", "Z")), "win":(("A", "Y"), ("B", "Z"), ("C", "X"))}

SCORE = 0

with open(TEST_DATA) as f:
	strategy_sheet = [tuple(rounds.split()) for rounds in f.read().split("\n")]

win = []
draw = []
loss = []

for i in strategy_sheet:
	for key in conditions:
		if i in conditions[key]:
			eval(key).append(i)


print(win, loss, draw)


		
			 