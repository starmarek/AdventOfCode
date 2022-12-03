import math

with open("input.txt", "r") as f:
    data = [item for item in f.read().splitlines()]


def lower(rang):
    rang[1] -= math.ceil((rang[1] - rang[0]) / 2)
    return rang


def upper(rang):
    rang[0] += math.ceil((rang[1] - rang[0]) / 2)
    return rang


mapp = {"F": lower, "B": upper, "L": lower, "R": upper}
sidlist = []
for line in data:
    rang = [0, 127]
    sid = 8
    for item in line[:7]:
        rang = mapp[item](rang)
    sid *= rang[0]
    rang = [0, 7]
    for item in line[7:]:
        rang = mapp[item](rang)
    sid += rang[0]
    sidlist.append(sid)
sidlist.sort()
print(max(sidlist))
print(set(range(sidlist[0], sidlist[-1])).difference(sidlist))
