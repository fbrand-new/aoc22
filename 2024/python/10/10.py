with open('test.txt','r') as f:
    map = [line.strip() for line in f.readlines()]

# def find_trailheads():

def pos_in_map(pos,limx,limy):
    if pos[0]>limy or pos[0]<0 or pos[1]>limx or pos[0]<0:
        return False
    
    return True

def find_neighbours(head,map,limx,limy):
    head_val = map[head[0],head[1]]
    
    if head_val == 9:
        return []
    
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    neighs = []
    for dir in dirs:
        neigh = (head[0]+dir[0],head[1]+dir[1])
        if pos_in_map(neigh,limx,limy):
            new_val = map[neigh[0],neigh[1]]
            if new_val == head_val+1:
                neighs.append(neigh)
    
    return neighs

def start_find_trail(head,map,limx,limy):
    trail = [head]
    i = 0
    
    while  

def find_trail(trail,map,limx,limy):
    neighbours = find_neighbours(trail[-1],map,limx,limy)
    for neigh in neighbours:
        trail.append(neigh)
        find_trail(neigh)

# for trailhead in trailheads:
