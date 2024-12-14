import re

with open("input.txt", "r") as f:
    line = f.read()


def mul(exp):
    a, b = [int(i) for i in re.findall("\d+", exp)]
    return a * b


donts = line.split("don't()")

sum = 0
for i, line in enumerate(donts):
    if i == 0:
        s = re.findall("mul\(\d+,\d+\)", line)
        print(s)
        for exp in s:
            sum += mul(exp)
        continue

    try:
        s = line.split("do()")[1:]
        for a in s:
            x = re.findall("mul\(\d+,\d+\)", a)
            print(x)
            for exp in x:
                sum += mul(exp)
    except:
        pass

print(sum)
