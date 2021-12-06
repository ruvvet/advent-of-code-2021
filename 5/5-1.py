test = [
[[0,9],[5,9]],
[[8,0],[0,8]],
[[9,4],[3,4]],
[[2,2],[2,1]],
[[7,0],[7,4]],
[[6,4],[2,0]],
[[0,9],[2,9]],
[[3,4],[1,4]],
[[0,0],[8,8]],
[[5,5],[8,2]],
]

map = []


# def addRow(rowIdx, colIdx):
#     # check current # of rows
#     currentMapRow = len(map)
#     for rowInit in range(currentMapRow, rowIdx):
#         map.append([0 for _ in range(colIdx or 1)])

# def addCol(rowIdx, colIdx):
#     currentRowCol = len(map[rowIdx])
#     print('aaaaaaaa', colIdx, rowIdx)
#     for newCol in range(currentRowCol, colIdx):
#         map[rowIdx].append(0)
#     print(map)




# def updateMap(x, y):
#     print('???????', x, y, map)

#     map[x][y] =+1

map = {}

def drawMap(lines):


        # # determine if same
        # rowRange = [startX] if startX-endX ==0 else range(startX, endX)
        # for row in rowRange:
        #     colRange = [startY] if startY-endY ==0 else range(startY, endY)
        #     for col in colRange:
        #         if len(map) < row:
        #             addRow(row, col)
        #         print('adaadad', len(map[row-1]), col)
        #         if len(map[row-1]) < col:
        #             addCol(row, col)
        #         updateMap(row-1, col)


    for start, end in lines:
        startX, startY=start
        endX, endY =end

        if startX==endX or startY==endY:
            minY = min(startY, endY)
            deltaY = abs(startY-endY)
            rowRange = [startY] if startY-endY ==0 else range(minY, minY+deltaY+1 )
            print('rowrange', rowRange)
            for row in rowRange:
                print('row#', row)
                minX = min(startX, endX)
                deltaX = abs(startX-endX)
                colRange = [startX] if startX-endX ==0 else range(minX, minX+deltaX+1)
                print('colrange', colRange)
                for col in colRange:
                    print('col#', col)
                    if f"{row}-{col}" in map:
                        map[f"{row}-{col}"] += 1
                    else:
                        map[f"{row}-{col}"] = 1

    print(sum([1 for v in map.values() if v > 1]))

drawMap(test)


