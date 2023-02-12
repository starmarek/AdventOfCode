import copy
import math
import typing
from collections import defaultdict
from functools import reduce
from operator import mul


class Monkey:
    def __init__(
        self,
        items: list[int],
        operation: str,
        divisible_by: int,
        monkey_if_true: int,
        monkey_if_false: int,
    ):
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.number_of_inspections = 0

    def inspect_items(self, lcm=None):
        self.number_of_inspections += len(self.items)
        monkey_to_item = defaultdict(list)
        for item in self.items:
            old = item  # noqa
            item = eval(self.operation)

            if lcm:
                item %= lcm
            else:
                item //= 3

            next_monkey = (
                self.monkey_if_true
                if item % self.divisible_by == 0
                else self.monkey_if_false
            )
            monkey_to_item[next_monkey].append(item)

        self.items.clear()
        return monkey_to_item


monkeys: list[Monkey] = []
with open("input.txt") as f:
    for line in f:
        if "Monkey" in line:
            items = next(f).strip().replace("Starting items: ", "").split(", ")
            items = [int(item) for item in items]

            operation = next(f).strip().replace("Operation: new = ", "")

            divisible_by = int(next(f).strip().replace("Test: divisible by ", ""))
            monkey_if_true = int(
                next(f).strip().replace("If true: throw to monkey ", "")
            )
            monkey_if_false = int(
                next(f).strip().replace("If false: throw to monkey ", "")
            )

            monkeys.append(
                Monkey(
                    items=items,
                    operation=operation,
                    divisible_by=divisible_by,
                    monkey_if_true=monkey_if_true,
                    monkey_if_false=monkey_if_false,
                )
            )


def simulate(n: int, monkeys: list[Monkey], lcm: typing.Optional[int] = None):
    for _ in range(n):
        for monkey in monkeys:
            monkey_to_items = monkey.inspect_items(lcm)
            for target_monkey, items in monkey_to_items.items():
                monkeys[target_monkey].items.extend(items)

    inspections = [monkey.number_of_inspections for monkey in monkeys]
    inspections.sort()
    return reduce(mul, inspections[-2:])


print(simulate(20, copy.deepcopy(monkeys)))  # first star
print(
    simulate(10000, monkeys, math.lcm(*[monkey.divisible_by for monkey in monkeys]))
)  # second star
