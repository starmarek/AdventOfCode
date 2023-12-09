from collections import defaultdict
from itertools import batched
from math import ceil, log10

DESTINATION = 0
SOURCE = 1
LENGTH = 2

maps = defaultdict(list)


def load_map(map_name, f):
    for nest_line in f:
        if not nest_line.strip():
            break

        maps[map_name].append(tuple(map(int, nest_line.split())))


def slide(start, stop, step):
    min_location, min_seed = min(
        [(localize_seed(seed), seed) for seed in range(start, stop, step)],
        key=lambda x: x[0],
    )

    if step == 1:
        return min_location
    else:
        a = slide(min_seed - step, min_seed, step // 10)
        b = slide(min_seed, min_seed + step, step // 10)

        return min(a, b)


def localize_seed(seed):
    soil = get_destination("seed-to-soil", seed)
    fertilizer = get_destination("soil-to-fertilizer", soil)
    water = get_destination("fertilizer-to-water", fertilizer)
    light = get_destination("water-to-light", water)
    temperature = get_destination("light-to-temperature", light)
    humidity = get_destination("temperature-to-humidity", temperature)
    return get_destination("humidity-to-location", humidity)


def get_destination(map_name, prev_destination):
    for range_ in maps[map_name]:
        source_range = range(range_[SOURCE], range_[SOURCE] + range_[LENGTH] + 1)
        if prev_destination in source_range:
            source_position = source_range.index(prev_destination)
            destination_range = range(
                range_[DESTINATION], range_[DESTINATION] + range_[LENGTH] + 1
            )
            return destination_range[source_position]

    return prev_destination


with open("input.txt") as f:
    for line in f:
        if "seeds" in line:
            seeds = list(map(int, line[6:].split()))
            seeds_batched = list(batched(seeds, 2))
        elif "seed-to-soil" in line:
            load_map("seed-to-soil", f)
        elif "soil-to-fertilizer" in line:
            load_map("soil-to-fertilizer", f)
        elif "fertilizer-to-water" in line:
            load_map("fertilizer-to-water", f)
        elif "water-to-light" in line:
            load_map("water-to-light", f)
        elif "light-to-temperature" in line:
            load_map("light-to-temperature", f)
        elif "temperature-to-humidity" in line:
            load_map("temperature-to-humidity", f)
        elif "humidity-to-location" in line:
            load_map("humidity-to-location", f)

print(min(localize_seed(seed) for seed in seeds))  # first star
print(  # second star
    min(
        slide(
            batch[0],
            batch[0] + batch[1],
            int(pow(10, ceil(log10(max(s[1] for s in seeds_batched) / 100)))),
        )
        for batch in seeds_batched
    )
)
