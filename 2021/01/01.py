import os

with open(os.path.dirname(__file__) + "/input.txt") as data_file:
    data = [int(line.rstrip("\n")) for line in data_file]

increases_count = 0
for measurement1, measurement2 in zip(data, data[1:]):
    if measurement1 - measurement2 < 0:
        increases_count += 1

print(increases_count)  # first star

increases_count = 0
sums_of_sliding_windows = [sum((x, y, z)) for x, y, z in zip(data, data[1:], data[2:])]
for sum_1, sum_2 in zip(sums_of_sliding_windows, sums_of_sliding_windows[1:]):
    if sum_1 - sum_2 < 0:
        increases_count += 1

print(increases_count)  # second star
