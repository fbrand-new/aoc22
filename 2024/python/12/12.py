from heapq import merge
import itertools
import copy
from pprint import pp
from turtle import left 

# these calculations work for a connected region. Now we need to distinguish between unconnected regions.
# we need to do a dfs to find all the connected components. We'll do it in Rome.

def create_map(all_plots,lines):
    plots_map = {}
    for plot in plots:
        plot_map = [[(i,j) for j in range(len(lines)) if lines[i][j] == plot] for i in range(len(lines[0]))]
        plot_map = list(itertools.chain.from_iterable(plot_map))
        plots_map[plot] = plot_map
        
    return plots_map

def is_inside(cell,limx,limy):
    if cell[0] >= 0 and cell[0] < limx and cell[1] >= 0 and cell[1] < limy:
        return True

    return False

def add(cell,new_cell):
    return (cell[0] +new_cell[0], cell[1] + new_cell[1])

def no_neighbours(cell,cell_list,limx,limy):
    horizontal_dirs = [(0,1),(0,-1)]
    vertical_dirs = [(1,0),(-1,0)]

    horizontal_sides = []
    vertical_sides = []
    left_cell = add(cell,(0,-1))
    if not is_inside(left_cell,limx,limy) or left_cell not in cell_list:
        horizontal_sides.append(left_cell)

    # If we have a horizontal side then we need to add the cell in the "sides" ref system
    right_cell = add(cell,(0,1))
    if not is_inside(right_cell,limx,limy) or right_cell not in cell_list:
        horizontal_sides.append(cell)


    vertical_sides = []
    up_cell = add(cell,(-1,0))
    if not is_inside(up_cell,limx,limy) or up_cell not in cell_list:
        vertical_sides.append(up_cell)
    
    down_cell = add(cell,(1,0))
    if not is_inside(down_cell,limx,limy) or down_cell not in cell_list:
        vertical_sides.append(cell)

    return horizontal_sides, vertical_sides

def find_neighbours(cell,cell_list,limx,limy):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    neighbours = {}
    for dir in dirs:
        new_cell = add(cell,dir)
        if is_inside(new_cell,limx,limy) and new_cell in cell_list:
            neighbours[new_cell] = dir

    return neighbours

def degree(cell,cell_list,limx,limy):
    neighbours = find_neighbours(cell,cell_list,limx,limy)
    return len(neighbours)

def perimeter(cell_list,limx,limy):
    perim = 0
    for cell in cell_list:
        perim += 4 - degree(cell,cell_list,limx,limy) 

    return perim

def area(cell_list):
    return len(cell_list)

def connected_components(cell_list,limx,limy):

    connections = []
    for cell in cell_list:

        # Skip if cell is already part of a connected component
        if cell in itertools.chain.from_iterable(connections):
            continue

        visited = [cell]
        dfs(cell,cell_list,visited,limx,limy)
        connections.append(visited)

    return connections


def dfs(cell,cell_list,visited,limx,limy):
    cell_neighbours = find_neighbours(cell,cell_list,limx,limy)

    for neigh in cell_neighbours:
        if neigh in visited:
            continue
        neigh_dir = [neigh]
        visited.append(neigh)
        dfs(neigh,cell_list,visited,limx,limy)


def sides(region):

    # Count the number of corners
    sides = 0
    for cell in region:

        # If right and top no cell then corner
        right_cell = add(cell,(0,1))
        top_cell = add(cell,(-1,0))
        left_cell = add(cell,(0,-1))
        down_cell = add(cell,(1,0))

        corners = 0
        if right_cell not in region and top_cell not in region:
            corners+=1
        if right_cell not in region and down_cell not in region:
            corners+=1
        if left_cell not in region and top_cell not in region:
            corners+=1
        if left_cell not in region and down_cell not in region:
            corners+=1
        if right_cell in region and top_cell in region and add(cell,(-1,1)) not in region:
            corners+=1
        if right_cell in region and down_cell in region and add(cell,(1,1)) not in region:
            corners+=1
        if left_cell in region and top_cell in region and add(cell,(-1,-1)) not in region:
            corners+=1
        if left_cell in region and down_cell in region and add(cell,(1,-1)) not in region:
            corners+=1

        sides+=corners

    return sides

if __name__ == '__main__':
    with open('input.txt','r') as f:
        all_plots = f.read().strip()
        lines = all_plots.splitlines()

    limx = len(lines[0])
    limy = len(lines)
    plots = set(all_plots)
    plots.remove('\n')
    map = create_map(plots,lines)

    price = 0
    for plot in map:
        components = connected_components(map[plot], limx, limy)
        for component in components:
            print(plot)
            a = area(component)
            perim = perimeter(component,limx,limy)
            side = sides(component)
            print(side)
            price += a*side

    print(f"the total price is {price}")
