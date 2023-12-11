from itertools import combinations

import numpy as np

with open("input.txt") as f:
    arr = np.array([[item for item in row.strip()] for row in f])


empty_rows = []
for idx, row in enumerate(arr):
    if "#" not in row:
        empty_rows.append(idx)

empty_cols = []
for idx, column in enumerate(arr.T):
    if "#" not in column:
        empty_cols.append(idx)


galaxies = []
it = np.nditer(arr, flags=["multi_index"])
for item in it:
    row, column = it.multi_index
    if item == "#":
        galaxies.append(it.multi_index)

s = 0
expansions = 0
for (g1_y, g1_x), (g2_y, g2_x) in combinations(galaxies, 2):
    expansion = 0
    expansion += sum(x in empty_cols for x in range(min(g1_x, g2_x), max(g1_x, g2_x)))
    expansion += sum(y in empty_rows for y in range(min(g1_y, g2_y), max(g1_y, g2_y)))
    expansions += expansion
    s += abs(g1_x - g2_x) + abs(g1_y - g2_y) + expansion

print(s)  # first star
print(s + (expansions * 999998))  # second star
