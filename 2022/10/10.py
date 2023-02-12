data = []
with open("input.txt") as f:
    data = [line.split() for line in f.read().splitlines()]


cycle = 0
registry = 1
signal_strengths = []
for instruction in data:
    if instruction[0] == "noop":
        to_cycle = 1
        to_registry = 0
    else:
        to_cycle = 2
        to_registry = int(instruction[1])

    for _ in range(to_cycle):
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * registry)

    registry += to_registry

print(sum(signal_strengths))  # first star


CRT = []
cycle = 0
registry = 1
for instruction in data:
    if instruction[0] == "noop":
        to_cycle = 1
        to_registry = 0
    else:
        to_cycle = 2
        to_registry = int(instruction[1])

    for _ in range(to_cycle):
        if registry - 1 <= cycle <= registry + 1:
            CRT.append("#")
        else:
            CRT.append(".")
        if (cycle + 1) % 40 == 0:
            CRT.append("\n")
            cycle = 0
            continue
        cycle += 1

    registry += to_registry

print("".join(CRT))  # second star
