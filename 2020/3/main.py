with open("input.txt", "r") as f:
    data = [line * 200 for line in f.read().splitlines()]

tree1, tree2, tree3, tree4, tree5 = 0, 0, 0, 0, 0
for index in range(1, len(data)):
    tree1 += data[index][index] == "#"
    tree2 += data[index][index * 3] == "#"
    tree3 += data[index][index * 5] == "#"
    tree4 += data[index][index * 7] == "#"
    try:
        tree5 += data[index * 2][index] == "#"
    except IndexError:
        pass

print(tree2)
print(tree1 * tree2 * tree3 * tree4 * tree5)
