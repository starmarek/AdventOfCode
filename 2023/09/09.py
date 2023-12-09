from itertools import pairwise


def down(sequence):
    data = [sequence.copy()]
    while not all(i == 0 for i in data[-1]):
        data.append([b - a for a, b in pairwise(data[-1])])
    return data


def up(sequence):
    ans = 0
    for line1, line2 in pairwise(reversed(sequence)):
        ans = line1[-1] + line2[-1]
        line2.append(ans)
    return ans


with open("input.txt") as f:
    values1 = [up(down(list(map(int, line.split())))) for line in f]

with open("input.txt") as f:
    values2 = [up(down(list(map(int, line.split()))[::-1])) for line in f]

print(sum(values1))  # first star
print(sum(values2))  # second star
