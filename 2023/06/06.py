import functools
import operator
import re

with open("input.txt") as f:
    data1 = list(zip(*(map(int, re.findall(r"\d+", line)) for line in f)))
with open("input.txt") as f:
    data2 = [int("".join(re.findall(r"\d+", line))) for line in f]


def get_distances(time, record):
    return [distance for t in range(time) if (distance := t * (time - t)) > record]


print(  # first star
    functools.reduce(
        operator.mul, [len(get_distances(time1, record1)) for time1, record1 in data1]
    )
)
print(len(get_distances(*data2)))  # second star
