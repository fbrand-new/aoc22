with open("input.txt", "r") as f:
    lines = f.readlines()

safe_count = 0
for x in lines:
    x = [int(i) for i in x.split(" ")]
    d = [x[i] - x[i - 1] for i, _ in enumerate(x)][1:]

    if all([i < 0 and i >= -3 for i in d]):
        safe_count += 1

    if all([i > 0 and i <= 3 for i in d]):
        safe_count += 1

print(f"Safe count is {safe_count}")
