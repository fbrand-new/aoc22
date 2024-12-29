from copy import deepcopy
import queue
import math


def create_grid(lines):
    grid = [[c for c in line.strip()] for line in lines] 
    return grid

def render(grid):
    for line in grid:
        print(''.join(line))

def get_starting_point(grid):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                return (i,j)

def get_ending_point(grid):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'E':
                return (i,j)

def add(node1,node2):
    return (node1[0]+node2[0],node1[1]+node2[1])

def diff(node1,node2):
    return (node1[0]-node2[0],node1[1]-node2[1])

def get(grid,node):
    return grid[node[0]][node[1]]

def find_neighbours(node,grid):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    neighs = []
    for dir in dirs:
        new_node = add(node,dir)
        if get(grid,new_node) != '#':
            neighs.append(new_node)

    return neighs

def compute_cost(new_dir,current_dir):

    if new_dir == current_dir:
        return 1
    else:
        return 1001

def create_edge_grid(grid):
    starting_point = get_starting_point(grid)
    initial_dir = (0,1)
    edges = {}
    nodes_to_visit = queue.Queue()
    nodes_to_visit.put((starting_point,initial_dir))
    visited_nodes = set()

    while not nodes_to_visit.empty():
        node, current_dir = nodes_to_visit.get()
        neighbours = find_neighbours(node,grid)
        for neigh in neighbours:
            if neigh in visited_nodes:
                continue
            dir = diff(neigh,node)
            if dir != current_dir:
                edges[(node,neigh)] = 1000
                # Lets try to trick if we need to come back
                edges[(neigh,node)] = math.inf
            else:
                edges[(node,neigh)] = 1
                edges[(neigh,node)] = math.inf
            nodes_to_visit.put((neigh,dir))

        visited_nodes.add(node)
                

    return edges

def get_nodes(grid):
    nodes_set = set()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c != '#':
                nodes_set.add((i,j))

    return nodes_set


def find_best_path(ending_point,starting_node,grid,nodes_dist):
    # TODO: still needs to add all the paths
    shortest_paths = []
    shortest_path = [ending_point]
    shortest_paths.append(shortest_path)

    for path in shortest_paths:
        curr_node = ending_point
        while curr_node != starting_node:
            min_dist = math.inf
            closest_node = (0,0)
            neighbours = find_neighbours(curr_node,grid)
            closest_nodes = set()
            closest_node = (0,0)
            for neigh in neighbours:
                if nodes_dist[neigh][0] < min_dist:
                    min_dist = nodes_dist[neigh][0]
                    closest_node = neigh
                elif nodes_dist[neigh][0] == min_dist:
                    closest_nodes.add(neigh)

            closest_nodes.add(closest_node)
            for node in closest_node:
                new_path = deepcopy(path)
                new_path.append(node)
                shortest_paths.append(new_path)

            curr_node = closest_node

    return shortest_path

def render_best_path(grid,best_path):
    grid_render = deepcopy(grid)
    for node in best_path:
        grid_render[node[0]][node[1]] = 'O'

    render(grid_render)


def djikstra(grid):
    unvisited_nodes = get_nodes(grid)
    nodes_dist = {k:(math.inf,(0,0)) for k in unvisited_nodes}
    starting_node = get_starting_point(grid)
    starting_dir = (0,1)
    nodes_dist[starting_node] = (0,starting_dir)

    # Resort based on min distance
    while len(unvisited_nodes) > 0:
        nodes_dist = dict(sorted(nodes_dist.items(), key=lambda item:item[1][0]))
        unvisited_nodes_ordered = [i for i in nodes_dist.keys() if i in unvisited_nodes]
        # Select first item on the dict
        first_node = unvisited_nodes_ordered[0]
        curr_dist = nodes_dist[first_node][0]
        current_dir = nodes_dist[first_node][1]
        neighbours = find_neighbours(first_node,grid)

        for neigh in neighbours:
            if neigh in unvisited_nodes:
                dir = diff(neigh,first_node)
                cost = compute_cost(dir,current_dir)
                new_dist = curr_dist + cost
                if new_dist < nodes_dist[neigh][0]:
                    nodes_dist[neigh] = (new_dist,dir)

        unvisited_nodes.remove(first_node)
    
    return nodes_dist

def part1(lines):
    grid = create_grid(lines)
    nodes_dist = djikstra(grid)
    ending_point = get_ending_point(grid)
    best_path = find_best_path(ending_point,get_starting_point(grid),grid,nodes_dist)
    render_best_path(grid,best_path)
    print(f"Min dist is: {nodes_dist[ending_point]}")


if __name__ == '__main__':

    with open('test.txt','r') as f:
        lines = f.readlines()

    part1(lines)