import bisect

trans_table1 = str.maketrans("TJQKA", "ABCDE")
trans_table2 = str.maketrans("TJQKA", "A0CDE")


def calc_type(hand):
    return sum(map(hand.count, hand))


with open("input.txt") as f:
    data1 = []
    for line in f:
        hand, bid = line.split()
        hand = hand.translate(trans_table1)
        bisect.insort(data1, (calc_type(hand), hand, int(bid)))

with open("input.txt") as f:
    data2 = []
    for line in f:
        hand, bid = line.split()
        hand = hand.translate(trans_table2)
        bisect.insort(
            data2,
            (max(calc_type(hand.replace("0", r)) for r in hand), hand, int(bid)),
        )


print(sum(i * d[2] for i, d in enumerate(data1, 1)))  # first star
print(sum(i * d[2] for i, d in enumerate(data2, 1)))  # second star
