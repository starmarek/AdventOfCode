import re
from queue import LifoQueue

magazine = [
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
    LifoQueue(maxsize=50),
]
instructions = []

with open("input.txt") as f:
    for line in reversed(f.read().splitlines()):
        if line.startswith("move"):
            instructions.append(list(map(int, re.findall(r"\d+", line))))
        elif "[" in line:
            for i, column_number in enumerate(range(1, len(line), 4)):
                if line[column_number] != " ":
                    magazine[i].put(line[column_number])


def crate_mover_9000():
    for instruction in reversed(instructions):
        quantity, from_, to = instruction

        stack_from = magazine[from_ - 1]
        stack_to = magazine[to - 1]

        for _ in range(quantity):
            item = stack_from.get()
            stack_to.put(item)


def crate_mover_9001():
    for instruction in reversed(instructions):
        quantity, from_, to = instruction

        stack_from = magazine[from_ - 1]
        stack_to = magazine[to - 1]

        tmp = []
        for _ in range(quantity):
            item = stack_from.get()
            tmp.append(item)

        for item in reversed(tmp):
            stack_to.put(item)


def every_first_crate():
    every_first_crate = []
    for stack in magazine:
        every_first_crate.append(stack.get())

    print("".join(every_first_crate))


# comment out the one that you dont need
# crate_mover_9000()  # first star
crate_mover_9001()  # second star
every_first_crate()
