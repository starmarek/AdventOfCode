with open("input.txt", "r") as f:
    data = [item for item in f.read().splitlines()]

valid_pass_count_1_star = 0
valid_pass_count_2_star = 0
for expr in data:
    splitted = expr.split(":")

    password = splitted[1].lstrip()
    letter = splitted[0][-1]
    (lower, upper) = map(int, splitted[0][:-2].split("-"))

    if lower <= password.count(letter) <= upper:
        valid_pass_count_1_star += 1

    if (
        password[lower - 1] == letter
        and not password[upper - 1] == letter
        or not password[lower - 1] == letter
        and password[upper - 1] == letter
    ):
        valid_pass_count_2_star += 1

print(valid_pass_count_1_star, valid_pass_count_2_star)
