with open("input6.txt", 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(",")))


test = [3,4,3,1,2]


def getFish(fishList, days):

    fish = [fishList.count(i) for i in range(9)]
    for i in range(days):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
        assert len(fish) == 9

    print(sum(fish))

getFish(data, 256)


