import csv

diagReport= []

test = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']


with open('input.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        rowValues = row[0].split()
        diagReport.append(rowValues[0])


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def invertBit(bits):
    return ''.join([ '0'  if b =='1' else '1' for b in bits])



def getPower(diagReport):
    gamma = ''
    for i in range(len(diagReport[0])):
        zeroBit = 0
        oneBit = 0
        for v in diagReport:
            if v[i] == '0':
                zeroBit +=1
            else:
                oneBit +=1
        # print(zeroBit, oneBit)
        if zeroBit > oneBit:
            gamma += '0'
        else:
            gamma +='1'

    gammaBit = binaryToDecimal(int(gamma))
    epsilonBit = binaryToDecimal(int(invertBit(gamma)))

    return gammaBit * epsilonBit


def getMostCommon(diagReport):
    pivot = []
    for i in range(len(diagReport[0])):
        zeroBit = 0
        oneBit = 0
        for v in diagReport:
            if v[i] == '0':
                zeroBit +=1
            else:
                oneBit +=1
        if zeroBit > oneBit:
            pivot.append(0)
        else:
            pivot.append(1)
    return pivot



def getMatchingVal( i, temp):
    val = getMostCommon(temp)
    matchingVal = []
    # print(val, i, temp)
    if len(temp)==1:
        return temp
    else:
        for v in temp:
            # print(str(val[i]) != str(v[i]), val[i], v[i], v)
            if str(val[i]) == str(v[i]):
                matchingVal.append(v)
        getMatchingVal(i+1, matchingVal)


print(getMatchingVal( 0, [*test]))













# print(getPower(diagReport))

