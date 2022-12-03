with open("input.txt") as f:
    l = [line for line in f.read().splitlines()]

c = 0
for line in l:
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]

    common_item = (set(first_half) & set(second_half)).pop()

    if common_item.isupper():
        c += (ord(common_item) - 38)
    else:
        c += (ord(common_item) - 96)
print(c) # first star

c = 0
for i in range(0, len(l), 3):
    elf_1, elf_2, elf_3 = l[i:i + 3]

    common_item = (set(elf_1) & set(elf_2) & set(elf_3)).pop()

    if common_item.isupper():
        c += (ord(common_item) - 38)
    else:
        c += (ord(common_item) - 96)
print(c) # second_star