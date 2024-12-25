from heapq import merge
import itertools
import copy
from pprint import pp 

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
    all_cells = copy.deepcopy(cell_list)

    connections = []
    for cell in cell_list:

        # Skip if cell is already part of a connected component
        if cell in itertools.chain.from_iterable(connections):
            continue

        sides = 4
        curr_dir = (0,0)
        visited = [cell]
        dfs(cell,cell_list,visited,limx,limy,sides,curr_dir)
        connection = {}
        connection['sides'] = sides
        connection['cell_list'] = visited
        connections.append(connection)

    return connections


def dfs(cell,cell_list,visited,limx,limy,sides,curr_dir):
    cell_neighbours = find_neighbours(cell,cell_list,limx,limy)
    unvisited_neighbours = {k:v for k,v in cell_neighbours.items() if k not in visited}

    new_sides = 0
    if len(unvisited_neighbours) == 1:
        for neigh in unvisited_neighbours:
            if unvisited_neighbours[neigh] != curr_dir and curr_dir != (0,0):
                new_sides = 2
    if len(unvisited_neighbours) == 2:
        new_sides = 4
    if len(unvisited_neighbours) == 3:
        new_sides = 6
    for neigh in unvisited_neighbours:
        neigh_dir = unvisited_neighbours[neigh]
        visited.append(neigh)
        dfs(neigh,cell_list,visited,limx,limy,sides+new_sides,neigh_dir)

def list_to_map(cell_list,limx,limy):
    map = [['' for _ in range(limy)] for _ in range(limx)]

    for cell in cell_list:
        map[cell[0]][cell[1]] = 'x'

    return map

def is_right_side_filled(side,cell_list,limx,limy):
    # Convert side into cell
    x = side[0]
    y = side[1] + 1

    # if (x,y) in cell_list or is_inside((x,y),limx,limy):
    if (x,y) in cell_list:
        return True

    return False

def is_down_side_filled(side,cell_list,limx,limy):
    # Convert side into cell
    x = side[0] + 1
    y = side[1] 

    # if (x,y) in cell_list or is_inside((x,y),limx,limy):
    if (x,y) in cell_list:
        return True

    return False

def is_up_side_filled(side,cell_list,limx,limy):
    # Convert side into cell
    x = side[0] - 1
    y = side[1] 

    # if (x,y) in cell_list or is_inside((x,y),limx,limy):
    if (x,y) in cell_list:
        return True

    return False

def is_down_right_filled(side,cell_list,limx,limy):
    # Convert side into cell
    x = side[0] + 1
    y = side[1] + 1

    # if (x,y) in cell_list or is_inside((x,y),limx,limy):
    if (x,y) in cell_list:
        return True

    return False

def is_up_right_filled(side,cell_list,limx,limy):
    # Convert side into cell
    x = side[0] - 1
    y = side[1] + 1

    # if (x,y) in cell_list or is_inside((x,y),limx,limy):
    if (x,y) in cell_list:
        return True

    return False

# Deprecated
def get_sides(cell_list,limx,limy):
    hor_sides = []
    ver_sides = []
    for cell in cell_list:
        h_sides, v_sides = no_neighbours(cell,cell_list,limx,limy)
        hor_sides.extend(h_sides)
        ver_sides.extend(v_sides)

    # horizontal sides needs to be swapped to employ the same "refe*
    orig_hor_sides = copy.deepcopy(hor_sides)
    hor_sides = [(side[1],side[0]) for side in hor_sides]
    hor_sides.sort()
    
    ver_sides_to_check = [(side[1],side[0]) for side in hor_sides]
    ver_sides.sort()
    merged_h_sides = [[hor_sides[0][0],hor_sides[0][1]]]

    for i in range(1,len(hor_sides)):
        # Check if the last merged sides matches the h index, and the v index is merged + 1
        condition1 = merged_h_sides[-1][0] == hor_sides[i][0] and merged_h_sides[-1][1] == hor_sides[i][1] - 1  
        # condition2 = (merged_h_sides[-1][0],merged_h_sides[-1][1]) not in ver_sides_to_check
        # condition2 = is_right_side_filled((merged_h_sides[-1][1],merged_h_sides[-1][0]),cell_list,limx,limy)
        condition2 = is_down_side_filled(merged_h_sides[-1],cell_list,limx,limy)
        condition3 = is_right_side_filled(merged_h_sides[-1],cell_list,limx,limy)
        condition4 = is_down_right_filled(merged_h_sides[-1],cell_list,limx,limy)
        condition5 = not condition2 and not condition3 and condition4

        condition6 = is_up_side_filled(merged_h_sides[-1],cell_list,limx,limy)
        condition7 = is_up_right_filled(merged_h_sides[-1],cell_list,limx,limy)
        condition8 = not condition3 and not condition6 and condition7

        if condition1 and not condition5 and not condition8:
        # if condition1:
            # Check also if there is an adjacent vertical fence, in that case we cannot merge
            merged_h_sides[-1][1] = hor_sides[i][1]
        else:
            merged_h_sides.append([hor_sides[i][0],hor_sides[i][1]])


    merged_v_sides = [[ver_sides[0][0],ver_sides[0][1]]]

    for i in range(1,len(ver_sides)):
        # Check if the last merged sides matches the h index, and the v index is merged + 1
        condition1 = merged_v_sides[-1][0] == ver_sides[i][0] and merged_v_sides[-1][1] == ver_sides[i][1] - 1 
        # condition2 = (merged_h_sides[-1][0],merged_h_sides[-1][1]) not in orig_hor_sides
        condition2 = is_down_side_filled(merged_v_sides[-1],cell_list,limx,limy)
        condition3 = is_right_side_filled(merged_v_sides[-1],cell_list,limx,limy)
        condition4 = is_down_right_filled(merged_v_sides[-1],cell_list,limx,limy)
        condition5 = not condition2 and not condition3 and condition4

        condition6 = is_up_side_filled(merged_v_sides[-1],cell_list,limx,limy)
        condition7 = is_up_right_filled(merged_v_sides[-1],cell_list,limx,limy)
        condition8 = not condition3 and not condition6 and condition7
        if condition1 and not condition5 and not condition8: 
        # if condition1:
            merged_v_sides[-1][1] = ver_sides[i][1]
        else:
            merged_v_sides.append([ver_sides[i][0],ver_sides[i][1]])

    return merged_h_sides, merged_v_sides

if __name__ == '__main__':
    with open('test.txt','r') as f:
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
            print(component['cell_list'])
            # map =  list_to_map(component,limx,limy)
        #     perim = perimeter(component,limx,limy)
            a = area(component['cell_list'])
            sides = component['sides']
            # print(f"sides: {hor_sides}")
            # print(f"ver sides: {ver_sides}")
            # sides = hor_sides
            # sides.extend(ver_sides)
            print(f"sides {sides}")
            price += a*sides

    print(f"the total price is {price}")
