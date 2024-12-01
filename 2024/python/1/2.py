with open("input.txt", "r") as f:
    file = f.readlines()

# Read each line. First number goes into one list, second on the other
left = []
right = []
for line in file:
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

# left = sorted(left)
# right = sorted(right)

sum = 0
for a in left:
    occurences = 0

    for b in right:
        if a == b:
            occurences += 1

    sum += a * occurences

print(f"The sum is {sum}")
