from hmac import new


with open('test.txt','r') as f:
    lab = [i.strip() for i in f.readlines()]

# Get coordinate of the guard
# While coordinate of the guard are inside the perimeter
# move guard up 
# if moving guard up would hit obstacle move guard to the right
# track coordinates found by guard

class Coordinate:
    def __init__(self,x,y,lab) -> None:
        self.x = x
        self.y = y
        self.dir = [0,-1]
        self.lab = lab

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
        self.go_ahead()

    def go_ahead(self):
        self.x = self.dir[0] + self.x
        self.y = self.dir[1] + self.y
        
def get_guard_coordinate(lab):
    for y,floor in enumerate(lab):
        for x,pos in enumerate(floor):
            if pos == '^':
                return Coordinate(x,y,lab)

    return Coordinate(-1,-1,lab)

guard = get_guard_coordinate(lab) 

# visited_positions = [(guard.x,guard.y)]
visited_positions = []
while not guard.is_out_of_bounds():

    visited_positions.append((guard.x,guard.y))
    if guard.is_next_pos_obstacle():
        guard.turn_right()
    else:
        guard.go_ahead()

visited_set = set(visited_positions)
print(f"The guard has visited a total of {len(visited_set)}")

