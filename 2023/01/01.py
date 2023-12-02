from array import array

import regex as re
from word2number import w2n


def part1(f):
    return [
        array("u", (digit for digit in re.findall(r"\d", line)))
        for line in f.read().splitlines()
    ]


def part2(f):
    return [
        array(
            "u",
            (
                str(w2n.word_to_num(word_or_digit))
                for word_or_digit in re.findall(
                    r"\d|one|two|three|four|five|six|seven|eight|nine",
                    line,
                    overlapped=True,
                )
            ),
        )
        for line in f.read().splitlines()
    ]


def clump_an_sum(data):
    return sum(array("H", (int(line[0] + line[-1]) for line in data)))


with open("input.txt") as f:
    part1 = part1(f)
with open("input.txt") as f:
    part2 = part2(f)

print(clump_an_sum(part1))  # first star
print(clump_an_sum(part2))  # second star
