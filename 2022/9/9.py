import typing as t

data = []
with open("input.txt") as f:
    data = [line.split() for line in f.read().splitlines()]


class Knot:
    def __init__(self, next_: t.Optional["Knot"] = None):
        self.position = [0, 0]
        self.all_positions = [tuple(self.position)]
        self.next_ = next_

    def move(self):
        if (
            self.is_in_the_same_column_as(self.next_)
            and self.vertical_distance_from(self.next_) > 1
        ):
            if self.is_below(self.next_):
                self.position[1] += 1
            else:
                self.position[1] -= 1
        elif (
            self.is_in_the_same_row_as(self.next_)
            and self.horizontal_distance_from(self.next_) > 1
        ):
            if self.is_on_the_left(self.next_):
                self.position[0] += 1
            else:
                self.position[0] -= 1
        elif (
            not self.is_in_the_same_row_as(self.next_)
            and not self.is_in_the_same_column_as(self.next_)
            and not self.is_touching_with(self.next_)
        ):
            if self.is_below(self.next_):
                if self.is_on_the_left(self.next_):
                    self.position[0] += 1
                    self.position[1] += 1
                else:
                    self.position[0] -= 1
                    self.position[1] += 1
            else:
                if self.is_on_the_left(self.next_):
                    self.position[0] += 1
                    self.position[1] -= 1
                else:
                    self.position[0] -= 1
                    self.position[1] -= 1

        self.all_positions.append(tuple(self.position))

    def is_in_the_same_column_as(self, knot: "Knot") -> bool:
        return self.position[0] == knot.position[0]

    def is_in_the_same_row_as(self, knot: "Knot") -> bool:
        return self.position[1] == knot.position[1]

    def vertical_distance_from(self, knot: "Knot") -> int:
        return abs(knot.position[1] - self.position[1])

    def horizontal_distance_from(self, knot: "Knot") -> int:
        return abs(knot.position[0] - self.position[0])

    def is_below(self, knot: "Knot") -> bool:
        return self.position[1] < knot.position[1]

    def is_on_the_left(self, knot: "Knot") -> bool:
        return self.position[0] < knot.position[0]

    def is_touching_with(self, knot: "Knot") -> bool:
        return (
            self.horizontal_distance_from(knot) <= 1
            and self.vertical_distance_from(knot) <= 1
        )


def simulate(n):
    rope = [Knot()]
    for i in range(n - 1):
        head = rope[i]
        new_head = Knot()
        head.next_ = new_head
        rope.append(new_head)

    for direction, reps in data:
        for _ in range(int(reps)):
            if direction == "U":
                rope[-1].position[1] += 1
            elif direction == "D":
                rope[-1].position[1] -= 1
            elif direction == "L":
                rope[-1].position[0] -= 1
            elif direction == "R":
                rope[-1].position[0] += 1

            for knot in rope[-2::-1]:
                knot.move()

    return rope[0]


tail = simulate(2)
print(len(set(tail.all_positions)))  # first star

tail = simulate(10)
print(len(set(tail.all_positions)))  # second star
