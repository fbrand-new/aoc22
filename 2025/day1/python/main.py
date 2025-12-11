import sys

filename = "test.txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


with open(filename) as f:
    l = f.readlines()
    inst = [i.strip() for i in l]
    curr_val = 50
    res = 0
    for i in inst:
        try:
            val = int(i[1:])
        except:
            print("Wrong conversion, your code is bugged!")
            exit(-1)
        if i[0] == 'L':
            curr_val = (curr_val - val)%100
        else:
            curr_val = (curr_val + val)%100
        
        if curr_val == 0:
            res += 1


    print(f"Res is {res}")
        
