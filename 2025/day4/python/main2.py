import sys
from copy import deepcopy

filename = "test.txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

def check_position(grid,i,j):
    if check_boundary(grid,i,j):
        return grid[i][j] == '@'
    else:
        return False


def check_boundary(grid,i,j):
    if i == len(grid):
        return False
    elif i < 0:
        return False
    elif j == len(grid[0]):
        return False
    elif j < 0:
        return False

    return True
    
def check_positions(grid,i,j):
    res = 0
    if check_position(grid,i-1,j-1):
        res += 1
    if check_position(grid,i-1,j):
        res += 1
    if check_position(grid,i-1,j+1):
        res += 1
    if check_position(grid,i,j-1):
        res += 1
    if check_position(grid,i,j+1):
        res += 1
    if check_position(grid,i+1,j-1):
        res += 1
    if check_position(grid,i+1,j):
        res += 1
    if check_position(grid,i+1,j+1):
        res += 1
        
    return res

with open(filename) as f:
    l = f.readlines()
    grid = [[k for k in i.strip()] for i in l]
    new_grid = deepcopy(grid)
    res = 0
    changed = True
    while changed:
        changed = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c] == '@':
                    neighs = check_positions(grid,r,c)

                    if neighs < 4:
                        new_grid[r][c] = "."
                        changed = True
                        res += 1
    
        grid = new_grid 
                
    print(f"Res is: {res}")
                
                
