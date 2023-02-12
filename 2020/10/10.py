from collections import Counter, deque
from functools import reduce
from operator import mul

with open("input.txt") as f:
    data = [int(item) for item in f.read().splitlines()]
    data.sort()
    data = deque(data)
    data.appendleft(0)
    data.append(data[-1] + 3)
    # [86, 149, 4, 75, 87, 132, 12, 115, 62, 61, 153, 78, 138 ...]

diffs = [data[i + 1] - data[i] for i in range(len(data) - 1)]
print(reduce(mul, Counter(diffs).values()))  # first star
