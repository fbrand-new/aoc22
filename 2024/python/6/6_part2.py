import copy


with open('test.txt','r') as f:
    lab_str = f.read()
    lab = [[j for j in i.strip()] for i in lab_str.splitlines()]

# Get coordinate of the guard
# While coordinate of the guard are inside the perimeter
# move guard up 
# if moving guard up would hit obstacle move guard to the right
# track coordinates found by guard

class Coordinate:
    def __init__(self,x,y,lab_str) -> None:
        self.x = x
        self.y = y
        self.dir = [0,-1]
        self.lab_str = lab_str
        self.lab = self.__build_lab()
        self.__x = x
        self.__y = y
        self.orig_dir = self.dir[:]

    def __build_lab(self):
        return [[j for j in i.strip()] for i in self.lab_str.splitlines()]

    def reset_pos(self):
        self.x = self.__x
        self.y = self.__y
        self.lab = self.__build_lab()
        self.dir = self.orig_dir[:]

    def is_out_of_bounds(self):
        return self.is_pos_out_of_bounds(self.x,self.y)

    def is_pos_out_of_bounds(self,x,y):
        if x >= len(self.lab[0]) or y >= len(self.lab):
            return True

        if x < 0 or y < 0:
            return True
        
        return False

    def is_next_pos_obstacle(self):
        new_x = self.dir[0] + self.x
        new_y = self.dir[1] + self.y

        if self.is_pos_out_of_bounds(new_x,new_y):
            return False

        if self.lab[new_y][new_x] == '#':
            return True
        
        return False

    def turn_right(self):
        self.dir[0], self.dir[1] = -self.dir[1], self.dir[0]
        # self.go_ahead()

    def go_ahead(self):
        self.x = self.dir[0] + self.x
        self.y = self.dir[1] + self.y
        
def get_guard_coordinate(lab_str,lab):
    for y,floor in enumerate(lab):
        for x,pos in enumerate(floor):
            if pos == '^':
                return Coordinate(x,y,lab_str)

    return Coordinate(-1,-1,lab)


def is_guard_in_a_loop(positions_list, positions_set):
    if len(positions_list) == len(positions_set):
        return False
    
    return True

def is_stuck(guard):
    visited_positions = []
    visited_set = set()
    while not guard.is_out_of_bounds():

        info = (guard.x,guard.y,(guard.dir[0],guard.dir[1]))
        visited_positions.append(info)
        visited_set.add(info)
        if guard.is_next_pos_obstacle():
            guard.turn_right()
        else:
            guard.go_ahead()
        
        if is_guard_in_a_loop(visited_positions, visited_set):
            return True
        
    return False

succesful_obstructions = 0
guard = get_guard_coordinate(lab_str,lab) 

for i in range(len(guard.lab)):
    for j in range(len(guard.lab[0])):
        # print(f"Checking obstruction at {i},{j}")
        if guard.x == j and guard.y == i:
            continue
        guard.reset_pos()
        guard.lab[i][j] = "#"
        if is_stuck(guard):
            succesful_obstructions += 1
    

print(f"Number of succesful obstacles added {succesful_obstructions}")

