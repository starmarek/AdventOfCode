from contextlib import contextmanager

with open("input.txt") as f:
    data = [item.split(" ") for item in f.read().splitlines()]
    data = [[item[0], int(item[1])] for item in data]
    # [('acc', -7), ('acc', 2), ('acc', 20), ...]


def procedure(item):
    global accumulator
    global current_position
    if item[0] == "acc":
        current_position += 1
        accumulator += item[1]
    elif item[0] == "jmp":
        current_position += item[1]
    elif item[0] == "nop":
        current_position += 1


# part 1
current_position = 0
used_positions = set()
accumulator = 0
while True:
    if current_position not in used_positions:
        used_positions.add(current_position)
    else:
        break

    item = data[current_position]
    procedure(item)

print(accumulator)  # first star


@contextmanager
def stub_data(index, to_stub):
    original = data[index]
    data[index] = to_stub
    yield
    data[index] = original


success = False
for i in range(len(data)):
    if data[i][0] == "acc":
        continue
    to_stub = ("nop" if data[i][0] == "jmp" else "jmp", data[i][1])
    with stub_data(i, to_stub):
        used_positions = set()
        accumulator = 0
        current_position = 0
        while True:
            if current_position == len(data):
                success = True
                break
            if current_position not in used_positions:
                used_positions.add(current_position)
            else:
                break

            item = data[current_position]
            procedure(item)
        if success:
            break


print(accumulator)  # second star
