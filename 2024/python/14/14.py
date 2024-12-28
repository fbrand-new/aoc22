import os
import time

def pos_t(pos,vel,t,limx,limy):
    x_t = pos[0] + vel[0]*t
    y_t = pos[1] + vel[1]*t
    return (x_t%limx,y_t%limy)

def count_quadrants(robots,limx,limy):

    quadrants = [0,0,0,0]
    for robot in robots:
        px, py = robot['pos']
        if px < limx//2 and py < limy//2:
            quadrants[0] += 1
        elif px > limx//2 and py < limy//2:
            quadrants[1] += 1
        elif px < limx//2 and py > limy//2:
            quadrants[2] += 1
        elif px > limx//2 and py > limy//2:
            quadrants[3] += 1
        
    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

def part1():
    with open('test.txt','r') as f:
        lines = f.readlines()

    robots = []
    for line in lines:
        p,v = line.split(' ')
        pos = [int(i) for i in p.split('=')[1].split(',')]
        vel = [int(i.strip()) for i in v.split('=')[1].split(',')]
        robots.append({'pos': pos, 'vel': vel})

    limx = 7
    limy = 11

    t = 100
    for robot in robots:
        robot['pos'] = pos_t(robot['pos'],robot['vel'],t,limx,limy)


    print(f"The total is {count_quadrants(robots,limx,limy)}")

def grid(robots,limx,limy):
    grid = [[' ' for i in range(limx)] for j in range(limy)]
    for robot in robots:
        px, py = robot['pos']
        grid[py][px] = 'X'

    return grid


def print_robots(grid):
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    with open('input.txt','r') as f:
        lines = f.readlines()

    robots = []
    for line in lines:
        p,v = line.split(' ')
        pos = [int(i) for i in p.split('=')[1].split(',')]
        vel = [int(i.strip()) for i in v.split('=')[1].split(',')]
        robots.append({'pos': pos, 'vel': vel})

    limx = 101
    limy = 103

    t = 100000
    first_tree = 40
    intervals = [20,81]
    k = 0
    for i in range(t):
        for robot in robots:
            robot['pos'] = pos_t(robot['pos'],robot['vel'],i,limx,limy)
        g = grid(robots,limx,limy)
        if i == first_tree:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_robots(g)
            first_tree += intervals[k%2]
            k+=1
            input()
        # time.sleep(0.2)


    # print(f"The total is {count_quadrants(robots,limx,limy)}")