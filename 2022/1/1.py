with open("input.txt") as f:
    c = 0
    calories = []
    for line in f.read().splitlines():
        if not line:
            calories.append(c)
            c = 0
            continue
        c += int(line)
    calories.append(c)
    calories.sort(reverse=True)


print(max(calories))  # first star
print(sum(calories[:3]))  # second star
