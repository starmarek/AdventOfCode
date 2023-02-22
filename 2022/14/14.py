import itertools

import numpy as np

with open("input.txt") as f:
    data = [
        [[int(a) for a in c.strip().split(",")] for c in b.split("->")]
        for b in f.read().splitlines()
    ]
    max_y = 0
    for line in data:
        y = max(line, key=lambda x: x[1])[1]
        if y > max_y:
            max_y = y


def create_cave(data):
    cave = np.full((200, 800), ".", dtype=str)
    for line in data:
        for cord1, cord2 in itertools.pairwise(line):
            if cord1[0] != cord2[0]:
                if cord1[0] < cord2[0]:
                    cave[cord1[1], cord1[0] - 1 : cord2[0]] = "#"
                else:
                    cave[cord1[1], cord2[0] - 1 : cord1[0]] = "#"
            else:
                if cord1[1] < cord2[1]:
                    cave[cord1[1] : cord2[1], cord1[0] - 1] = "#"
                else:
                    cave[cord2[1] : cord1[1], cord1[0] - 1] = "#"
    return cave


def simulate1(cave):
    sand = [499, 0]
    while True:
        try:
            if cave[sand[1] + 1][sand[0]] not in "o#":
                sand[1] += 1
            elif cave[sand[1] + 1][sand[0] - 1] not in "o#":
                sand[1] += 1
                sand[0] -= 1
            elif cave[sand[1] + 1][sand[0] + 1] not in "o#":
                sand[1] += 1
                sand[0] += 1
            else:
                cave[sand[1]][sand[0]] = "o"
                sand = [499, 0]
        except IndexError:
            break


def simulate2(cave):
    sand = [499, 0]
    while cave[0, 499] != "o":
        if cave[sand[1] + 1][sand[0]] not in "o#":
            sand[1] += 1
        elif cave[sand[1] + 1][sand[0] - 1] not in "o#":
            sand[1] += 1
            sand[0] -= 1
        elif cave[sand[1] + 1][sand[0] + 1] not in "o#":
            sand[1] += 1
            sand[0] += 1
        else:
            cave[sand[1]][sand[0]] = "o"
            sand = [499, 0]


cave = create_cave(data)
simulate1(cave)
np.savetxt("star1.out", cave, fmt="%s", delimiter="")
print(np.count_nonzero(cave == "o"))  # first star


data.append([[1, max_y + 2], [800, max_y + 2]])
cave = create_cave(data)
simulate2(cave)
np.savetxt("star2.out", cave, fmt="%s", delimiter="")
print(np.count_nonzero(cave == "o"))  # second star
