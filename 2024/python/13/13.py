import math

def parse_button(line):
    try:
        pre,post = line.split(':')
    except:
        raise Exception("Parsing error for line {line}")
    
    x = int(post.split('X+')[1].split(',')[0])
    y = int(post.split('Y+')[1].strip())

    return x,y

def parse_prize(line):

    x = int(line.split('X=')[1].split(',')[0])
    y = int(line.split('Y=')[1].strip())

    return x,y

def compute_i(x_a,y_a,x_b,y_b,x_p,y_p):
    # THIS does not work, we may have to study integer programming
    # we have the following eq: y_p = y_a*i + y_b*j
    # and also x_p = x_a*i + x_b*j
    # therefore i = (y_p - y_b*j)/y_a
    # also i = (x_p - x_b*j)/x_a
    # You can solve the system and find a unique solution
    # where i and j must be integers and i<100, j<100
    # find all i and j that satisfy, then compute the cost as 3*i + j. The min wins.
    x_p = x_p + 10000000000000 
    y_p = y_p + 10000000000000
    j = (y_a*x_p - x_a*y_p)//(y_a*x_b - x_a*y_b)
    i = (y_p - y_b*j)//y_a
    rem_j = (y_a*x_p - x_a*y_p)%(y_a*x_b - x_a*y_b)
    rem_i = (y_p - y_b*j)%y_a 

    if i < 0 or j < 0:
        return None
    if rem_i == 0 and rem_j ==0:
        return 3*i + j


#Brute force, do all combinations of i and j and compute cost
def minimize(x_a,y_a,x_b,y_b,x_p,y_p):

    x_p = x_p + 10000000000000
    y_p = y_p + 10000000000000

    init_i, init_j = compute_i(x_a,y_a,x_b,y_b,x_p,y_p)
    return 3*init_i + init_j

# def branch_and_repeat(i,j,x_a,x_b,y_a,y_b,x_p,y_p):
#     x_e = x_p - x_a*i - x_b*j
#     y_e = y_p - y_a*i - y_b*j

#     if x_e == 0 and y_e == 0:
#         return 3*i+j
#     elif x_e < 0 and y_e < 0:
#         cost_i = branch_and_repeat(i-1,j,x_a,x_b,y_a,y_b,x_p,y_p)
#         cost_j = branch_and_repeat(i,j-1,x_a,x_b,y_a,y_b,x_p,y_p)

if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()
    
    total_cost = 0
    for i, line in enumerate(lines):
        if i%4 == 0:
            x_a, y_a = (parse_button(line))
        elif i%4 == 1:
            x_b, y_b = (parse_button(line))
        elif i%4 == 2:
            x_p, y_p = (parse_prize(line))
        elif i%4 == 3:
            cost = compute_i(x_a,y_a,x_b,y_b,x_p,y_p)
            # print(cost)
            if cost is not None:
                total_cost+=cost

    print(f"total cost is {total_cost}")