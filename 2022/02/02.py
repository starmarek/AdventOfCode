from enum import Enum


class Opponent(str, Enum):
    A = "A"  # rock
    B = "B"  # paper
    C = "C"  # scissors


class You(str, Enum):
    X = "X"  # rock, loose
    Y = "Y"  # paper, draw
    Z = "Z"  # scissors, win


WIN_SCENARIOS = [[Opponent.A, You.Y], [Opponent.B, You.Z], [Opponent.C, You.X]]
DRAW_SCENARIOS = [[Opponent.A, You.X], [Opponent.B, You.Y], [Opponent.C, You.Z]]
LOSE_SCENARIOS = [[Opponent.A, You.Z], [Opponent.B, You.X], [Opponent.C, You.Y]]

with open("input.txt") as f:
    data = [line.split() for line in f.read().splitlines()]


c = 0
for scenario in data:
    if scenario in WIN_SCENARIOS:
        c += 6
    elif scenario in DRAW_SCENARIOS:
        c += 3

    match scenario[1]:
        case You.X:
            c += 1
        case You.Y:
            c += 2
        case You.Z:
            c += 3
print(c)  # first star


c = 0
for scenario in data:
    match scenario[1]:
        case You.X:
            your_choice = list(
                filter(lambda x: x[0] == scenario[0], LOSE_SCENARIOS)
            ).pop()[1]
        case You.Y:
            your_choice = list(
                filter(lambda x: x[0] == scenario[0], DRAW_SCENARIOS)
            ).pop()[1]
            c += 3
        case You.Z:
            your_choice = list(
                filter(lambda x: x[0] == scenario[0], WIN_SCENARIOS)
            ).pop()[1]
            c += 6

    match your_choice:
        case You.X:
            c += 1
        case You.Y:
            c += 2
        case You.Z:
            c += 3
print(c)  # second star
