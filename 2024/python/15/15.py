import os
import time

def parse_lines(lines):

    warehouse_map = []
    k = 0
    for i,line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            break
        warehouse_map.append([i for i in line])
        k = i

    moves_list = []
    for line in lines[k+1:]:
        moves_list.append(line.strip())

    moves = ''.join(moves_list)
    return warehouse_map, moves

def curr_pos(wh_map):
    for i, line in enumerate(wh_map):
        for j, item in enumerate(line):
            if item == '@':
                return i,j

def add(pos1,pos2):
    return (pos1[0]+pos2[0],pos1[1]+pos2[1])

def get(wh_map,pos):
    return wh_map[pos[0]][pos[1]]

def move(wh_map,prev_pos,next_pos):
    px, py = prev_pos[0], prev_pos[1]
    nx, ny = next_pos[0], next_pos[1]
    wh_map[px][py], wh_map[nx][ny] = '.', get(wh_map,prev_pos)


def dynamic(wh_map,current_pos,dir):
    # We need to move the box and all the possible consecutive boxes
    # On the same direction up to a wall

    next_possible_pos = add(current_pos,dir)

    next_pos = current_pos
    if get(wh_map,next_possible_pos) == '.':
        next_pos = next_possible_pos
        move(wh_map,current_pos,next_pos)
        return True
    elif get(wh_map,next_possible_pos) == 'O':
        next_pos = next_possible_pos
        if dynamic(wh_map,next_pos,dir):
            move(wh_map,current_pos,next_pos)
            return True
        else:
            return False
    else:
        return False

def dynamic2(wh_map,current_pos,dir):
    # We need to move the box and all the possible consecutive boxes
    # On the same direction up to a wall

    next_possible_pos = add(current_pos,dir)

    next_pos = current_pos
    item_next_pos = get(wh_map,next_possible_pos) 
    if item_next_pos == '.':
        next_pos = next_possible_pos
        # move(wh_map,current_pos,next_pos)
        return [(current_pos,next_pos)]
    elif item_next_pos == ']' or item_next_pos == '[':

        # If we are pushing sideways is the same as before
        if dir == (0,1) or dir == (0,-1):
            next_pos = next_possible_pos
            acts = dynamic2(wh_map,next_pos,dir)
            if acts:
                # move(wh_map,current_pos,next_pos)
                acts.append((current_pos,next_pos))
                return acts
            else:
                return None
        # If we are pushing from top/bottom then we need to consider
        # That the box should "stick together"
        else:
            next_pos = next_possible_pos
            if item_next_pos == '[':
                # Closing bracket is on the right of item_next_pos
                pair_current_pos = add(next_possible_pos,(0,1))
            else:
                # Opening bracket on the left
                pair_current_pos = add(next_possible_pos,(0,-1))
            
            # Only if both of the brackets can move the robot will move
            acts1 = dynamic2(wh_map,next_pos,dir)
            acts2 = dynamic2(wh_map,pair_current_pos,dir)
            if acts1 and acts2:
                acts = acts1
                acts.extend(acts2)
                acts.append((current_pos,next_pos))
                return acts
            else:
                return False
    else:
        return None

def simulate(wh_map,action,dyn):
    current_pos = curr_pos(wh_map)

    if action== '^':
        dir = (-1,0)
    elif action == '>':
        dir = (0,1)
    elif action == 'v':
        dir = (1,0)
    else:
        dir = (0,-1)

    actions = dyn(wh_map,current_pos,dir)
    if dyn == dynamic2 and actions:
        actions = list(dict.fromkeys(actions))
        # print(f"Actions to perform {actions}")
        for action in actions:
            move(wh_map,action[0],action[1])

def render(wh_map):
    for line in wh_map:
        print(''.join(line))

def gps(wh_map,ch):
    total = 0
    for i, line in enumerate(wh_map):
        for j, item in enumerate(line):
            if item == ch:
                total += i*100 + j

    return total


def enlarge_map(wh_map):
    new_wh_map = []
    for line in wh_map:
        line_str = ''.join(line)
        line_str = line_str.replace('#','##')
        line_str = line_str.replace('O','[]')
        line_str = line_str.replace('.','..')
        line_str = line_str.replace('@','@.')
        new_wh_map.append([i for i in line_str])

    return new_wh_map

def part1(lines):
    wh_map, actions = parse_lines(lines)
    for action in actions:
        simulate(wh_map,action,dynamic)

    print(f"The GPS says: {gps(wh_map,'O')}")

def part2(lines,debug=False):

    # Modify the map
    wh_map, actions = parse_lines(lines)
    wh_map = enlarge_map(wh_map)
    
    for action in actions:
        if debug:
            print(f"Move {action}")
            render(wh_map)
            input()
        simulate(wh_map,action,dynamic2)
        if debug:
            input()
            os.system('cls' if os.name == 'nt' else 'clear')

    print(f"The GPS says: {gps(wh_map,'[')}")
    return wh_map

if __name__ == '__main__':

    with open('input.txt','r') as f:
        lines = f.readlines()

    # Debug
    # wh_map, actions = parse_lines(lines)
    # wh_map = enlarge_map(wh_map)
    # t = 10
    # for i in range(t):
    #     print(f"Move {actions[i]}")
    #     render(wh_map)
    #     input()
    #     simulate(wh_map,actions[i],dynamic2)
    #     os.system('cls' if os.name == 'nt' else 'clear')

    # part1(lines)
    wh_map = part2(lines)
    # render(wh_map)


    