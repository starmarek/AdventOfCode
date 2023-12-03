import itertools
import math
import re
from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
symbols = {
    (i, j)
    for i, l in enumerate(data)
    for j, x in enumerate(l)
    if x != "." and not x.isdigit()
}


parts = []
parts_by_symbol = defaultdict(list)
for line_idx, line in enumerate(data):
    for match_ in re.finditer(r"\d+", line):
        number = int(match_.group(0))
        start, end = match_.span()

        boundary = {
            (line_idx + di, j + dj) for di, dj in box for j in range(start, end)
        }

        if symbols & boundary:
            parts.append(number)
        for symbol in symbols & boundary:
            parts_by_symbol[symbol].append(number)


print(sum(parts))  # first star

# This assumes that no non-star symbol touches exactly two numbers
print(sum(math.prod(v) for v in parts_by_symbol.values() if len(v) == 2))  # second star
