#day_3 AOC 2022 python file
FULL_DATA, TEST_DATA = "./day_3/day_3.txt", "./day_3/day_3_min.txt"

""""
with open(FULL_DATA) as f:
	items = [set(item[:len(item)//2]) & set(item[len(item)//2:]) for item in f.read().split()]
"""
with open(FULL_DATA) as f:
	items = [item for item in f.read().split()]

def part_one(list_items):
	priorities = []
	for item in list_items:
		item = " ".join(item)
		if item.isupper():
			item = ord(item) - 38
		else:
			item = ord(item) - 96
		priorities.append(item)
	return sum(priorities)

def part_two():
	badge_groups = [items[i: i+3] for i in range(0, len(items), 3) ]
	
	for idx, rucksacks in  enumerate(badge_groups):
		for idx_2, rucksack in enumerate(rucksacks):
			badge_groups[idx][idx_2] = set(rucksack)

		badge_groups[idx] = badge_groups[idx][0] & badge_groups[idx][1] & badge_groups[idx][2]

	return badge_groups

print(part_one(part_two()))