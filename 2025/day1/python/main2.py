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
            new_val = curr_val - val
            print(f"New val after instr {i}: {curr_val} -> {new_val}")
            if new_val <= 0 and curr_val > 0:
                print(f"Inst is: {i}")
                res += 1
                res += abs(new_val) // 100
            elif new_val <= 0 :
                res += abs(new_val) // 100
        else:
            new_val = curr_val + val
            print(f"New val after instr {i}: {curr_val} -> {new_val}")
            if new_val >= 100:
                print(f"Inst is: {i}")
                res += new_val // 100

        curr_val = new_val % 100
        # if curr_val == 0:
        #     print(f"Inst is: {i}")
        #     res += 1
        

    print(f"Res is {res}")
        
