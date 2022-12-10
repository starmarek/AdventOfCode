import math

import numpy as np

grid = []
with open("input.txt") as f:
    grid = np.array([[int(item) for item in line] for line in f.read().splitlines()])


row_count = grid.shape[0]
column_count = grid.shape[1]


def tree_is_on_edge(row, column):
    return row == 0 or column == 0 or row == row_count - 1 or column == column_count - 1


c = 0
it = np.nditer(grid, flags=["multi_index"])
for item in it:
    current_row = it.multi_index[0]
    current_column = it.multi_index[1]

    if tree_is_on_edge(current_row, current_column):
        c += 1
        continue

    top = grid[:current_row, current_column]
    bottom = grid[current_row + 1 :, current_column]
    left = grid[current_row, :current_column]
    right = grid[current_row, current_column + 1 :]

    if any(
        item > biggest_tree
        for biggest_tree in [max(top), max(bottom), max(left), max(right)]
    ):
        c += 1
print(c)  # first star

c = []
it = np.nditer(grid, flags=["multi_index"])
for item in it:
    current_row = it.multi_index[0]
    current_column = it.multi_index[1]

    if tree_is_on_edge(current_row, current_column):
        continue

    top = list(reversed(grid[:current_row, current_column]))
    bottom = grid[current_row + 1 :, current_column]
    left = list(reversed(grid[current_row, :current_column]))
    right = grid[current_row, current_column + 1 :]

    scores = []
    for direction in [top, bottom, left, right]:
        for i, tree in enumerate(direction, start=1):
            if tree >= item:
                scores.append(i)
                break
        else:
            scores.append(len(direction))
    c.append(math.prod(scores))
print(max(c))  # second star
