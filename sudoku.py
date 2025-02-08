# my sudoku bad.
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

def printGrid(grid):
    for k in range(0, 9):
        for l in range(0, 9):
            print(grid[k][l], end=' ')
            if l % 3 == 2 and l != 8:
                print('|', end=' ')
        print()
        if k % 3 == 2 and k != 8:
            print("---------------------")
    print()


def valid(mesh, num, row, column):
    for i in range(0, 9):
        if num == mesh[i][column]:
            return False
    for i in range(0, 9):
        if num == mesh[row][i]:
            return False
    x = row % 3
    y = column % 3
    for i in range(row - x, row - x + 3):
        for j in range(column - y, column - y + 3):
            if num == mesh[i][j]:
                return False
    return True

def findEmpty(board):
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x , y
    return False

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        for num in range(1, 10):
            if valid(board, num, find[0], find[1]):

                board[find[0]][find[1]] = num

                if solve(board):

                    return True

                board[find[0]][find[1]] = 0
    return False



printGrid(grid)
solve(grid)
printGrid(grid)





