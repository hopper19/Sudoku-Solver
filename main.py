import random
import time

def display(grid):
    for i in range(0,9):
        for j in range(0,9):
            if j%3!=2:
                if len(grid[i][j])==1:
                    print(grid[i][j][0],end=' ') 
                else:
                    print(0,end=' ')
            else:
                if len(grid[i][j])==1:
                    print(grid[i][j][0],end='  ')
                else:
                    print(0,end='  ')
        print()
        if i%3==2:
            print()

puzzle = [[0,0,5, 3,0,0, 0,0,0],
          [8,0,0, 0,0,0, 0,2,0],
          [0,7,0, 0,1,0, 5,0,0],
            
          [4,0,0, 0,0,5, 3,0,0],
          [0,1,0, 0,7,0, 0,0,6],
          [0,0,3, 2,0,0, 0,8,0],
            
          [0,6,0, 5,0,0, 0,0,9],
          [0,0,4, 0,0,0, 0,3,0],
          [0,0,0, 0,0,9, 7,0,0]] 

def gridset(puzzle):
    x = [1,2,3,4,5,6,7,8,9]
    grid = [[0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0]] 
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] != 0:
                grid[i][j] = [puzzle[i][j]]
            else:
                grid[i][j] = x
    return grid
    
def done(grid):
    for i in range(0,9):
        for j in range(0,9):
            if len(grid[i][j]) != 1:
                return False
    return True

def check(grid,x,y,z):
    if len(grid[x][y])==1:
        return False
    a = []
    b = []
    c = []
    for i in range(0,9):
        p = 3*int(x/3) + int(i/3)
        q = 3*int(y/3) + (i%3)
        if len(grid[i][y])==1:
            a.append(grid[i][y][0])
        if len(grid[x][i])==1:
            b.append(grid[x][i][0])
        if len(grid[p][q])==1:
            c.append(grid[p][q][0])
        if (z in a) or (z in b) or (z in c):
                return False
    return True

def eliminate(grid):
    # for i in range(0,81):
    #     x = int(i/9)
    #     y = i%9
    for x in range(0,9):
        for y in range(0,9):
            if len(grid[x][y]) == 1:
                value = grid[x][y][0]
                a = 3*(int(x/3))
                b = 3*(int(y/3))
                for j in range(0,9):
                    yline = []
                    xline = []
                    zline = []
                    u = a+(int(j/3))
                    v = b+(j%3)
                    if (len(grid[j][y])!=1) and (value in (grid[j][y])):
                        yline[:] = grid[j][y]
                        (yline).remove(value)
                        grid[j][y] = yline
                    if (len(grid[x][j])!=1) and (value in (grid[x][j])):
                        xline[:] = grid[x][j]
                        (xline).remove(value)
                        grid[x][j] = xline
                    if (len(grid[u][v])!=1) and (value in (grid[u][v])):
                        zline[:] = grid[u][v]
                        (zline).remove(value)
                        grid[u][v] = zline
    for m in range(0,9):
        for o in range(1,10):
            xmark = 0
            ymark = 0
            p=0
            q=0
            for n in range(0,9):
                if o in grid[m][n]:
                    xmark=xmark+1
                    p=n
                if o in grid[n][m]:
                    ymark=ymark+1
                    q=n
            if xmark == 1:
                grid[m][p] = [o]
            if ymark == 1:
                grid[q][m] = [o]
    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(1,10):
                zmark = 0
                r=0
                s=0
                for a in range(0,3):
                    for b in range(0,3):
                        x = i+a
                        y = j+b
                        if k in grid[x][y]:
                            zmark = zmark+1
                            r=x
                            s=y
                if zmark == 1:
                    grid[r][s] = [k]
                    
    return grid

def probably(grid):
    for x in range(0,9):
        for y in range(0,9):
            # x = int(i/9)
            # y = i%9
            if len(grid[x][y]) == 2:
                k = random.randint(0,1)
                z = (grid[x][y][k])
                if check(grid,x,y,z):
                    grid[x][y] = [z] 
                    return grid
            if (len(grid[x][y]) == 3) and ((x==3 or x==4 or x==5) and (y==3 or y==4 or y==5)):
                k = random.randint(0,2)
                z = (grid[x][y][k])
                if check(grid,x,y,z):
                    grid[x][y] = [z]  
                    return grid       
    return grid

def solved(grid):
    if not done(grid):
        return False
    for i in range(0,9):
        a = 3*(int(i/3))
        b = 3*(i%3)
        for k in range(1,10):
            xmark = 0
            ymark = 0
            zmark = 0
            for j in range(0,9):
                if grid[i][j][0] == k:
                    xmark = xmark+1
                    if xmark > 1:
                        return False
                if grid[j][i][0] == k:
                    ymark = ymark+1
                    if ymark > 1:
                        return False
                x = a+int(j/3)
                y = b+(j%3)
                if grid[x][y][0] == k:
                    zmark = zmark+1
                    if zmark > 1:
                        return False
    return True

def sudoku(puzzle):
    while True:
        # print('set')
        grid = gridset(puzzle)
        grid = eliminate(grid)
        while not done(grid):
            grid = probably(grid)
            grid = eliminate(grid)
            # display(grid)
            # print('__________________')
        if solved(grid):
            break
    return grid

tot = 0
runs = 10000
max = 0
min = 1000
for i in range(0,runs):
    print('  ',i+1,end="\r")
    start = time.time()
    grid = sudoku(puzzle)
    elapsed = (time.time()-start)
    tot = tot + elapsed
    if elapsed>max:
        max = elapsed
    if elapsed<min:
        min = elapsed
print()
display(grid)

print('avg: ', tot/runs)
print('min: ', min)
print('max: ', max)

