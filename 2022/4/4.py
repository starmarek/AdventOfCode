with open("input.txt") as f:
    pairs = []
    for line in f.read().splitlines():
        elf1, elf2 = line.split(",")
        elf1_range1, elf1_range2 = list(map(int, elf1.split("-")))
        elf2_range1, elf2_range2 = list(map(int, elf2.split("-")))
        elf1_range = list(range(elf1_range1, elf1_range2 + 1))
        elf2_range = list(range(elf2_range1, elf2_range2 + 1))

        pairs.append([elf1_range, elf2_range])

c = 0
c2 = 0
for pair in pairs:
    elf1 = set(pair[0])
    elf2 = set(pair[1])

    if elf1.issubset(elf2) or elf2.issubset(elf1):
        c += 1
    if elf1 & elf2:
        c2 += 1
print(c)  # first star
print(c2)  # second star
