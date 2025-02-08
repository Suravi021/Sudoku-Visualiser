import pygame, sys
pygame.init()

# grid = []
# for a in range(9):
#     grid.append([0]*9)
grid = [[3, 0, 2, 9, 6, 4, 8, 5, 1],
        [9, 0, 4, 8, 1, 5, 0, 7, 0],
        [0, 0, 1, 3, 7, 2, 0, 9, 6],
        [0, 4, 0, 1, 0, 9, 0, 2, 8],
        [1, 0, 9, 0, 4, 6, 0, 0, 5],
        [5, 2, 0, 7, 0, 3, 0, 1, 4],
        [2, 0, 8, 6, 0, 1, 5, 4, 7],
        [4, 1, 0, 0, 3, 0, 2, 0, 0],
        [0, 0, 5, 0, 0, 7, 1, 0, 3]]


possible = {}
index = lambda x,y : 9*x + y
var = 0
for x in range(9):
    for y in range(9):
        if grid[x][y] == 0:
            possible[var] = []
        var += 1

def valid(grid, num, row, column):
    for x in range(9):
        if grid[row][x] == num:
            return False
        if grid[x][column] == num:
            return False
    m = row % 3
    n = column % 3
    for x in range(row - m, row - m + 3):
        for y in range(column - n, column - n + 3):
            if grid[x][y] == num:
                return False
    return True

def seq(board, pos):
    temp = []
    for num in range(1, 10):
        if valid(board, num, pos[0], pos[1]):
            temp.append(num)
    return temp

def findEmpty(board):
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x, y
    return False

def colSquareNum(colour, pos, num=" "):
    pygame.draw.rect(screen, colour, pygame.Rect(pos[1]*50,pos[0]*50, 50, 50))
    textImg = font.render(num, False, (0,0,0))
    screen.blit(textImg, (50 * pos[1] + 15, 50 * pos[0] + 15))

def fillGrid(grid):
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                continue
            text = str(grid[x][y])
            textImg = font.render(text, False, (0,0,0))
            screen.blit(textImg, (50 * y + 15,50 * x + 15))



screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("sudoku")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

screen.fill((230, 230, 230))

for m in range(0, 450 // 9):
    if m % 3 == 0:
        line_w = 5
    else:
        line_w = 2
    pygame.draw.line(screen, (0,0,0), (m * 50, 450), (m * 50, 0), line_w)
    pygame.draw.line(screen, (0,0,0), (0, m * 50), (450, m * 50), line_w)
fillGrid(grid)

pygame.display.update()


solved = False
empty = True
numbers = []
find = (80, 80)
fucked = False

revert = []

n = 1
# for_fucked = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10]

while True:
    clock.tick(20)

    # draw the damn thing
    screen.fill((230, 230, 230))
    for m in range(0, 450 // 9):
        if m % 3 == 0:
            line_w = 5
        else:
            line_w = 2
        pygame.draw.line(screen, (0,0,0), (m * 50, 450), (m * 50, 0), line_w)
        pygame.draw.line(screen, (0,0,0), (0, m * 50), (450, m * 50), line_w)


    if not solved and empty:
        find = findEmpty(grid)
        if not find:
            solved = True # if you didnt find anything then its solved
        else:
            empty = False # you now have an empty box to deal with
            numbers = seq(grid, find)
            revert.append(find)

            if not numbers:
                numbers = [1,1,1]
                possible[index(find[0], find[1])] = numbers

            else:
                k = len(numbers)
                numbers.append(0)
                numbers.append(k)
                print(find, numbers)
                # if(find == (1,6)):
                #     pass

                possible[index(find[0], find[1])] = numbers
    try:
        if numbers[-2] == numbers[-1]:
            numbers[-1] = 19
            fucked = True
            f = numbers[-3] + 1
    except:
        pass
    if fucked:
        if f > 9:
            colSquareNum((255,0,0), find)
            revert.pop(-1)
            find = revert[-1]
            numbers = possible[index(find[0], find[1])]

            numbers[-2] += 1
            n = numbers[numbers[-2]-1]+1
            grid[find[0]][find[1]] = 0
            fucked = False
        else:
            colSquareNum((150, 0, 150), find, str(f))
            f += 1

    else:
        # blue, green
        if n == numbers[numbers[-2]]:
            colSquareNum((0, 255, 0), find, str(n))
            grid[find[0]][find[1]] = n
            empty = True
            n = 1
        else:
            colSquareNum((150, 0, 150), find, str(n))
            n += 1
    fillGrid(grid)


    if solved:
        # print "solved"
        pass
    # printGrid(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(possible)
            pygame.quit()
            sys.exit()
    pygame.display.update()



