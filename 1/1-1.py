report = []

import csv
with open('input.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        report.append(int(row[0]))

def incMeasurement(report):
    return sum([1 for v in range(len(report)) if report[v]>report[v-1]])


def incSlidingWindow(report):

    # for v in range(len(report)-2):
    #     if(sum(report[v+1:v+4]) > sum(report[v:v+3]) ):
    return sum([1 for v in range(len(report)-2) if sum(report[v+1:v+4]) > sum(report[v:v+3]) ])


    # return sum( [1 for v in range(len(report)) if report[v]>report[v-1]])

print(incMeasurement(report))

print(incSlidingWindow(report))