with open("input.txt") as f:
    data = f.read()

for i in range(len(data) - 4 + 1):
    window = data[i : i + 4]  # noqa E203
    if len(set(window)) == 4:
        print(i + 4)  # first star
        break

for i in range(len(data) - 14 + 1):
    window = data[i : i + 14]  # noqa E203
    if len(set(window)) == 14:
        print(i + 14)  # second star
        break
