import os

with open(os.path.dirname(__file__) + "/input.txt") as data_file:
    data = [line.split() for line in data_file]

COMMAND_INDEX = 0
VALUE_INDEX = 1

horizontal_pos = 0
depth = 0
for instruction in data:
    match instruction[COMMAND_INDEX]:
        case "down":
            depth += int(instruction[VALUE_INDEX])
        case "up":
            depth -= int(instruction[VALUE_INDEX])
        case "forward":
            horizontal_pos += int(instruction[VALUE_INDEX])

print(horizontal_pos * depth)  # first star

horizontal_pos = 0
depth = 0
aim = 0
for instruction in data:
    match instruction[COMMAND_INDEX]:
        case "down":
            aim += int(instruction[VALUE_INDEX])
        case "up":
            aim -= int(instruction[VALUE_INDEX])
        case "forward":
            horizontal_pos += int(instruction[VALUE_INDEX])
            depth += aim * int(instruction[VALUE_INDEX])

print(horizontal_pos * depth)  # second star
