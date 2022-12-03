from itertools import combinations

with open("input.txt") as f:
    data = [int(item) for item in f.read().splitlines()]
    # [19, 20, 22, 10, 11, 29, 4, 41, 38, 46, 7, 2, ...]


def is_sum_of_two(data, number):
    for comb in combinations(data, 2):
        if sum(comb) == number:
            return True
    return False


for i in range(26, len(data)):
    if not is_sum_of_two(data[i-25:i], data[i]):
        print(data[i])
        break


# part 2
number = 556543474
for i in range(len(data)):
    for j in range(i, len(data)):
        if sum(data[i:j]) == number and len(data[i:j]) > 1:
            print(max(data[i:j]) + min(data[i:j]))
            break
    else:
        continue
    break
