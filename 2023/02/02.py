import re
from array import array

thresholds = {"red": 12, "green": 13, "blue": 14}


def part1():
    return array(
        "H",
        (
            idx
            for idx, line in enumerate(f, 1)
            if all(
                thresholds[item.split()[1]] >= int(item.split()[0])
                for item in re.findall(r"\d+ \w+", line)
            )
        ),
    )


def part2():
    return array(
        "H",
        (
            find_max_from_color("red", line)
            * find_max_from_color("green", line)
            * find_max_from_color("blue", line)
            for line in f
        ),
    )


def find_max_from_color(color, line):
    return int(
        max(re.findall(rf"\d+ {color}", line), key=lambda x: int(x.split()[0])).split()[
            0
        ]
    )


with open("input.txt") as f:
    part1 = part1()
with open("input.txt") as f:
    part2 = part2()

print(sum(part1))  # first star
print(sum(part2))  # second star
