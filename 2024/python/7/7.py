from itertools import product

with open('input.txt','r') as f:
    eqs = f.readlines()

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def concat(a,b):
    c,d = str(a), str(b)
    return int(c+d)

def create_ops_combinations(size):

    if size <= 1:
        raise Exception("Cant do this with only one element")

    sequence_len = size-1

    combos = [i for i in product((add,mul,concat),repeat=sequence_len)]

    return combos

def apply_combination(elements,operators):

    i = 0
    curr = elements[i]
    for op in operators:
        curr = op(curr,elements[i+1])
        i += 1

    return curr

def all_combos(total, elements):
    combos = create_ops_combinations(len(elements))

    for com in combos:
        if apply_combination(elements,com) == total:
            return True

    return False

sum = 0
for i,eq in enumerate(eqs):
    print(f"Computing combos for {i}-th eq")
    total, elements = eq.split(":")
    total = int(total)
    elements = elements.strip().split(" ")
    elements = [int(i) for i in elements]

    # Try all possible combinations of operators on the elements
    if all_combos(total,elements):
        sum += total

print(f"The sum is {sum}")
