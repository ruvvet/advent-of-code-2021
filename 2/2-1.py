import csv
course = []
test = [
['forward', '5'],
['down', '5'],
['forward', '8'],
['up', '3'],
['down', '8'],
['forward', '2']
]

with open('input.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        rowValues = row[0].split()
        course.append(rowValues)

def getPosition(course):
    depth = 0
    horizontal = 0
    aim = 0

    for move in course:
        if move[0] == 'down':
            depth += int(move[1])

        elif move[0] == 'up':
            depth -= int(move[1])

        else:
            horizontal += int(move[1])


    return depth * horizontal


def getAimPosition(course):
    depth = 0
    horizontal = 0
    aim = 0

    for move in course:
        if move[0] == 'down':
            aim +=int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])
        else:
            horizontal += int(move[1])
            depth += aim * int(move[1])

    return depth * horizontal

print(getPosition(course))
print(getAimPosition(course))
