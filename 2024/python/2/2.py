with open("input.txt", "r") as f:
    lines = f.readlines()

safe_count = 0


def desc(x):
    d = [x[i] - x[i - 1] for i, _ in enumerate(x)][1:]
    descending = [i < 0 and i >= -3 for i in d]
    return descending


def asc(x):
    d = [x[i] - x[i - 1] for i, _ in enumerate(x)][1:]
    ascending = [i > 0 and i <= 3 for i in d]
    return ascending


def check_if_safe(x):
    descending = desc(x)
    ascending = asc(x)
    if all(descending):
        return True
    elif all(ascending):
        return True

    return False


for x in lines:
    x = [int(i) for i in x.split(" ")]
    descending = desc(x)
    ascending = asc(x)
    if all(descending):
        safe_count += 1
    elif all(ascending):
        safe_count += 1
    else:
        for i in range(len(x)):
            if check_if_safe(x[0:i] + x[i + 1 :]):
                safe_count += 1
                break

print(f"Safe count is {safe_count}")
