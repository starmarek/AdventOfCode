import math
from itertools import cycle

with open("input.txt") as f:
    instructions = f.readline().strip()
    f.readline()
    map_ = {
        line.split("=")[0].strip(): tuple(line.split("=")[1].strip("() \n").split(", "))
        for line in f.readlines()
    }


def map_path(key, ending_condition):
    for idx, i in enumerate(cycle(instructions)):
        if ending_condition(key):
            return idx
        pair = map_[key]
        key = pair[0] if i == "L" else pair[1]


A_keys_mapped = [
    map_path(key, lambda x: x.endswith("Z")) for key in map_.keys() if key.endswith("A")
]

print(map_path("AAA", lambda x: x == "ZZZ"))  # first star
print(math.lcm(*A_keys_mapped))  # second star
