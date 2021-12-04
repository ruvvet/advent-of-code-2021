draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

boards = [
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

initBoard = [[0 for _ in range(5)] for _ in range(5)]

def checkBoard(num, board, boardState):
    print(num, board, boardState)
    for rowIndex, row in enumerate(board):
        if num in row:
            index = row.index(num)
            boardState[rowIndex][index] = 1
    return boardState




def is_solved(board):
    for i in range(0,5):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][0]

    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    else:
        return -1






def mainLoop():
    # boardsState = [initBoard for _ in range(len(boards))]
    currentStates = [initBoard for _ in range(len(boards))]
    for boardIdx, board in enumerate(boards):
        drawsToBingo = 0
        for num in draw:
            updatedBoardState = checkBoard(num, board, currentStates[boardIdx])
            currentStates[boardIdx] = updatedBoardState
            #TODO: check board state to see if it has hit bingo
            drawsToBingo +=1


        print(drawsToBingo)



mainLoop()







