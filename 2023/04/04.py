from collections import defaultdict

with open("input.txt") as f:
    points_sum = 0
    num_dict = defaultdict(int)
    for idx, line in enumerate(f):
        num_dict[idx] += 1
        card = line[9:]
        winning_numbers, my_numbers = card.split("|")
        no_winning_numbers = len(set(winning_numbers.split()) & set(my_numbers.split()))

        if no_winning_numbers > 0:
            points_sum += 2 ** (no_winning_numbers - 1)
        for i in range(no_winning_numbers):
            num_dict[idx + i + 1] += num_dict[idx]

print(points_sum)  # first star
print(sum(num_dict.values()))  # second star
