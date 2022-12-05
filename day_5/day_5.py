#day_5 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_5/day_5.txt", "./day_5/day_5_min.txt"

with open(TEST_DATA) as f:
	something = [stuff.split("\n") for stuff in f.read().split("\n")]

for x in something:
	print(x)