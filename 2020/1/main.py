from itertools import combinations
from math import prod

with open("input.txt", "r") as f:
    data = [int(item) for item in f.read().splitlines()]


def get_prod(amount_of_numbers_in_combination):
    for combination in combinations(data, amount_of_numbers_in_combination):
        if sum(combination) == 2020:
            return prod(combination)


print(get_prod(2))
print(get_prod(3))
