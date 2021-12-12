test = [
11111,
19991,
19191,
19991,
11111,
]

test2 = [
5483143223,
2745854711,
5264556173,
6141336146,
6357385478,
4167524645,
2176841721,
6882881134,
4846848554,
5283751526
]


steps=10



def createOctopusDict(octopusGrid):
    octopusDict = {}

    for yIdx, yVal in enumerate(octopusGrid):
        yString = str(yVal)
        for xIdx, xVal in enumerate(yString):
            octopusDict[f'{yIdx}-{xIdx}'] = int(xVal)

    return octopusDict


def updateDictFlash(y,x, octopusDict):

    keySet = [
    f'{y}-{x}',
    f'{y+1}-{x}',
    f'{y-1}-{x}',
    f'{y}-{x+1}',
    f'{y}-{x-1}',
    f'{y+1}-{x+1}',
    f'{y+1}-{x-1}',
    f'{y-1}-{x+1}',
    f'{y-1}-{x-1}'
    ]

    for key in keySet:
        if key in octopusDict:
            octopusDict[key] +=1
    print('non-capped', octopusDict)

    updatedOctopusDict = {k:(v if v <=9 else 9) for k,v in octopusDict.items()}
    print('capped', updatedOctopusDict)
    return updatedOctopusDict


def clearForNextStep(octopusDict):
    for energy in octopusDict.values():
        if energy >=9:
            return False

    return True



def getFlashes(octopusGrid , steps):

    octopusDict = createOctopusDict(octopusGrid)

    flashes = 0

    for step in range(steps):
        movetoNextStep = False
        # check if any values greater than 9 and keep looping

        while not movetoNextStep:
            for octopusKey, octopusEnergy in octopusDict.items():
                if octopusEnergy >= 9:
                    flashes +=1
                    y = int(octopusKey[0])
                    x = int(octopusKey[2])
                    newOctopusDict = updateDictFlash(y, x, octopusDict)
                    octopusDict = {k:v for k,v in newOctopusDict.items()}
            movetoNextStep = clearForNextStep(octopusDict)


        octopusDict = {k:(v+1 if v <9 else 0) for k,v in octopusDict.items()}
        print('hi', movetoNextStep)

    print(octopusDict)
    print(flashes)









getFlashes(test, 2)



