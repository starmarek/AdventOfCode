import bisect
from functools import cmp_to_key

with open("input.txt") as f:
    data = [line.split() for line in f]

trans_table = str.maketrans("TJQKA", "ABCDE")


def comp(line1, line2):
    hand1, _ = line1
    hand2, _ = line2

    hand1, hand2 = hand1.translate(trans_table), hand2.translate(trans_table)
    type_hand1, type_hand2 = calc_type(hand1), calc_type(hand2)

    if type_hand1 > type_hand2:
        return 1
    elif type_hand1 < type_hand2:
        return -1

    for card1, card2 in zip(hand1, hand2):
        ord1, ord2 = ord(card1), ord(card2)
        if ord1 > ord2:
            return 1
        elif ord1 < ord2:
            return -1
        else:
            continue
    return 0


def calc_type(hand):
    return sum(map(hand.count, hand))


values = []
for l in data:
    bisect.insort(values, l, key=cmp_to_key(comp))


print(sum(i * int(d[1]) for i, d in enumerate(values, 1)))  # first star
