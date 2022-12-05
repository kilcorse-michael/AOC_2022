#day_4 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_4/day_4.txt", "./day_4/day_4_min.txt"

with open(FULL_DATA) as f:
	section_pairs = [[num[0].split('-'), num[1].split('-')]  for pair in f.read().split("\n") for num in [pair.split(',')]]

def get_range(pairs_list):
	new = []
	for pair in pairs_list:
		group = []
		for num in pair:
			group.append(set(range(int(num[0]), int(num[1]) + 1)))
		new.append(group)
	return new

def part_one(lst):
	counter = 0
	for pair in lst:
		if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
			counter += 1
	return counter

def part_two(lst):
	new = []
	for pair in lst:
		overlap = pair[0] & pair[1]
		if overlap:
			new.append(overlap)
	return len(new)

print(part_one(get_range(section_pairs)))
print(part_two(get_range(section_pairs)))