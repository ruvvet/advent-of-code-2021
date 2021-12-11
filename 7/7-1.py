from math import inf

with open("input7.txt", "r") as f:
    crabPositions = list(map(int, f.read().strip().split(',')))

test = [16,1,2,0,4,2,7,1,2,14]



def alignCrabsConstant(crabs):

	maxHorizontal = max(crabs)
	fuelArray = []

	for position in range(maxHorizontal):
		fuel = 0
		for crab in crabs:
			fuel += abs(position - crab)
		fuelArray.append(fuel)
	return min(fuelArray)


def alignCrabsLinear(crabs):
	maxHorizontal = max(crabs)
	fuelArray = []

	for position in range(maxHorizontal):
		fuel = 0
		for crab in crabs:
			steps = abs(position - crab)
			fuel += (steps + 1) * steps / 2  # sum of increasing series formula
		fuelArray.append(int(fuel))

	return min(fuelArray)





print(alignCrabsConstant(crabPositions))
print(alignCrabsLinear(crabPositions))