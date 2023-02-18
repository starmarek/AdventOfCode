from functools import reduce
from operator import mul

with open("input.txt") as f:
    data1 = [eval(line) for line in f.read().splitlines() if line]
    data2 = list(zip(*([iter(data1)] * 2)))


def compare_signals(sig1, sig2):
    for item1, item2 in zip(sig1, sig2):
        if isinstance(item1, int) and isinstance(item2, int):
            if item1 > item2:
                return False
            elif item1 < item2:
                return True
        elif isinstance(item1, list) and isinstance(item2, list):
            if (ret := compare_signals(item1, item2)) is not None:
                return ret
        elif isinstance(item1, list):
            if (ret := compare_signals(item1, [item2])) is not None:
                return ret
        else:
            if (ret := compare_signals([item1], item2)) is not None:
                return ret

    if len(sig1) < len(sig2):
        return True
    elif len(sig1) > len(sig2):
        return False


def bubble(array):
    new_array = [e for e in array]

    while True:
        swapped = False
        for i in range(0, len(new_array) - 1):
            if compare_signals(new_array[i + 1], new_array[i]):
                new_array[i], new_array[i + 1] = (
                    new_array[i + 1],
                    new_array[i],
                )
                swapped = True

        if not swapped:
            break

    return new_array


sum_ = 0
for idx, sig1_sig2 in enumerate(data2):
    sig1, sig2 = sig1_sig2
    if compare_signals(sig1, sig2):
        sum_ += idx + 1
print(sum_)  # first star


data1.extend([[[2]], [[6]]])
data1 = bubble(data1)
to_prod = []
for idx, item in enumerate(data1):
    if item == [[2]]:
        to_prod.append(idx + 1)
    elif item == [[6]]:
        to_prod.append(idx + 1)
print(reduce(mul, to_prod))  # second star
