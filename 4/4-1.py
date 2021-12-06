testdraw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

testboards = [
[[22,13,17,11,0],
[8,2,23,4,24],
[21,9,14,16,7],
[6,10,3,18,5],
[1,12,20,15,19]]
,
[[3,15,0,2,22],
[9,18,13,17,5],
[19,8,7,25,23],
[20,11,10,24,4],
[14,21,16,12,6]]
,
[[14,21,17,24,4],
[10,16,15,9,19],
[18,8,23,26,20],
[22,11,13,6,5],
[2,0,12,3,7]]
]

# initBoard = [[0 for _ in range(5)] for _ in range(5)]
draws = []
boards = []

with open('input4.txt', 'r') as fd:
    draws = [int(num) for num in fd.readline().split(',')]
    newboard= []
    for row in fd:
        if row == '\n':
            if len(newboard):
                boards.append(newboard)
            newboard= []
        else:
            newboard.append([int(num.strip()) for num in row.split(' ') if num.strip()])




print(draws, boards)



def checkBoard(num, board, boardState):
    for rowIndex, row in enumerate(board):
        if num in row:
            index = row.index(num)
            boardState[rowIndex][index] = 1
    return boardState




def isBingo(board):
    for row in board:
        if sum(row) == 5:
            return True

    for col in range(5):
        colSum = 0
        for row in board:
            colSum += row[col]
            if(colSum) ==5:
                return True

    diag1 = 0
    diag2 = 0
    for rowIdx in range(5):
        for colIdx in range(5):
            if rowIdx == colIdx:
                diag1 +=board[rowIdx][colIdx]
                if diag1 ==5:
                    return True
            if rowIdx + colIdx ==4 :
                diag2 +=board[rowIdx][colIdx]
                if diag2 ==5:
                    return True
    return False


def mainLoop():
    # currentStates = [initBoard for _ in range(len(boards))]
    # drawsToBingo = [0 for _ in range(len(boards))]
    # print(drawsToBingo)
    # for boardIdx, board in enumerate(boards):
    #     print('????', boardIdx)
    #     for num in draw:
    #         if not isBingo(currentStates[boardIdx]):
    #             updatedBoardState = checkBoard(num, board, currentStates[boardIdx])
    #             # print(currentStates, boardIdx, currentStates[boardIdx])
    #             currentStates[boardIdx] = updatedBoardState
    #             # print(drawsToBingo[boardIdx])
    #             drawsToBingo[boardIdx] += 1

    winningState = []
    drawsToBingo = []

    for board in boards:
        counter = 0
        boardState = [[0 for _ in range(5)] for _ in range(5)]
        print(boardState)
        for num in draws:
            if isBingo(boardState):
                winningState.append(boardState)
                drawsToBingo.append(counter)
                break
            else:
                boardState = checkBoard(num, board, boardState)
                # print(boardState)
                # print(currentStates, boardIdx, currentStates[boardIdx])
                # print(drawsToBingo[boardIdx])
                counter += 1

    print(drawsToBingo)


mainLoop()







