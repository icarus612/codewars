# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

def validSolution(board):
    flip = [[] for i in board]
    for i in range(len(board)):
        if len(set(board[i])) != 9:
            return False 
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
            flip[i].append(board[i][j])
    for i in flip:
        if len(set(i)) != 9:
            return False      
    gr = [[] for i in board]
    for i in range(len(gr)):
        n = 0
        while len(gr[i]) < 9:
            if len(board[n]) == 0:
                del board[n]
            gr[i].extend(board[n][0:3])
            board[n] = board[n][3:]
            n += 1
    for i in gr: 
        if len(set(i)) < 9:
            return False
    return True

validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]])