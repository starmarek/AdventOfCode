with open("input.txt", "r") as f:
    data_one_star = [
        len(set("".join(group.split()))) for group in f.read().split("\n\n")
    ]
with open("input.txt", "r") as f:
    data_two_stars = [list(map(set, group.split())) for group in f.read().split("\n\n")]

answer_two_star = 0
for group in data_two_stars:
    answer += len(group[0].intersection(*group[1:]))

print(sum(data_one_star))
print(answer_two_star)
