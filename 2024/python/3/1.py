import re

with open("input.txt", "r") as f:
    line = f.read()

x = re.findall("mul\(\d+,\d+\)", line)

sum = 0
for exp in x:
    print(exp)
    a, b = [int(i) for i in re.findall("\d+", exp)]
    print(a, b)

    sum += a * b

print(sum)
