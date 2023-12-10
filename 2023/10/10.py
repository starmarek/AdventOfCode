with open("input.txt") as f:
    arr = [[item for item in row] for row in f]


start_node = (112, 18)
previous_item = start_node
current_item = (112, 19)
next_item = None
path = [start_node]
while next_item != start_node:
    path.append(current_item)
    c0 = current_item[0]
    c1 = current_item[1]
    label = arr[c0][c1]
    if label == "-":
        LEFT = (c0, c1 - 1)
        RIGHT = (c0, c1 + 1)
        if LEFT == previous_item:
            next_item = RIGHT
        else:
            next_item = LEFT
    elif label == "|":
        TOP = (c0 - 1, c1)
        BOTTOM = (c0 + 1, c1)
        if TOP == previous_item:
            next_item = BOTTOM
        else:
            next_item = TOP
    elif label == "L":
        TOP = (c0 - 1, c1)
        RIGHT = (c0, c1 + 1)
        if TOP == previous_item:
            next_item = RIGHT
        else:
            next_item = TOP
    elif label == "J":
        TOP = (c0 - 1, c1)
        LEFT = (c0, c1 - 1)
        if TOP == previous_item:
            next_item = LEFT
        else:
            next_item = TOP
    elif label == "7":
        BOTTOM = (c0 + 1, c1)
        LEFT = (c0, c1 - 1)
        if BOTTOM == previous_item:
            next_item = LEFT
        else:
            next_item = BOTTOM
    elif label == "F":
        BOTTOM = (c0 + 1, c1)
        RIGHT = (c0, c1 + 1)
        if BOTTOM == previous_item:
            next_item = RIGHT
        else:
            next_item = BOTTOM
    previous_item = current_item
    current_item = next_item

print(len(path) // 2)  # first star


from matplotlib.path import Path

p2 = 0
p = Path(path)
for y in range(len(arr)):
    for x in range(len(arr[0])):
        if (x, y) in path:
            continue
        if p.contains_point((x, y)):
            p2 += 1

print(p2)  # second star
