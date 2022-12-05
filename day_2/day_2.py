#day_2 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_2/day_2.txt", "./day_2/day_2_min.txt"

conditions = {"loss": (("A", "Z"), ("B", "X"), ("C", "Y")), "draw":(("A", "X"), ("B", "Y"), ("C", "Z")), "win":(("A", "Y"), ("B", "Z"), ("C", "X"))}

SCORE = 0

with open(FULL_DATA) as f:
	strategy_sheet = [tuple(rounds.split()) for rounds in f.read().split("\n")]

win = []
draw = []
loss = []

for i in strategy_sheet:
	for key in conditions:
		if i in conditions[key]:
			match i[1]:
				case "X":
					SCORE += 1
				case "Y":
					SCORE += 2
				case "Z":
					SCORE += 3
				case _:
					raise
			eval(key).append(i)


SCORE += len(win) * 6
SCORE += len(draw) * 3
print(SCORE)


		
			 