
input = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

input1 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    s = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].isdigit():
                if board[i][j] not in s:
                    s.add(board[i][j])
                else:
                    return False
        s = set()
    
    for j in range(len(board)):
        for i in range(len(board)):
            if board[i][j].isdigit():
                if board[i][j] not in s:
                    s.add(board[i][j])
                else:
                    return False
        s = set()

    for box_row in range(3):
        for box_col in range(3):
            s = set()

            for i in range(3):
                for j in range(3):
                    
                    actual_row = (box_row*3) + i
                    actual_col = (box_col*3) + j

                    cell = board[actual_row][actual_col]

                    if cell.isdigit():
                        if cell not in s:
                            s.add(cell)
                        else:
                            return False
    return True

print(isValidSudoku(input1))
