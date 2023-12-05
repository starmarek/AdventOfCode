from collections import defaultdict
from itertools import batched

DESTINATION = 0
SOURCE = 1
LENGTH = 2

maps = defaultdict(list)


def load_map(map_name, f):
    for nest_line in f:
        if not nest_line.strip():
            break

        maps[map_name].append(tuple(map(int, nest_line.split())))


with open("input.txt") as f:
    for line in f:
        if "seeds" in line:
            seeds = list(map(int, line[6:].split()))
            # seeds_batched = list(batched(seeds, 2))
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


locations1 = []
for seed in seeds:
    soil = get_destination("seed-to-soil", seed)
    fertilizer = get_destination("soil-to-fertilizer", soil)
    water = get_destination("fertilizer-to-water", fertilizer)
    light = get_destination("water-to-light", water)
    temperature = get_destination("light-to-temperature", light)
    humidity = get_destination("temperature-to-humidity", temperature)
    location = get_destination("humidity-to-location", humidity)

    locations1.append(location)
print(min(locations1))  # first star

# locations2 = []
# for batch in seeds_batched:
#     for seed in range(batch[0], batch[0] + batch[1] + 1):
#         soil = get_destination("seed-to-soil", seed)
#         fertilizer = get_destination("soil-to-fertilizer", soil)
#         water = get_destination("fertilizer-to-water", fertilizer)
#         light = get_destination("water-to-light", water)
#         temperature = get_destination("light-to-temperature", light)
#         humidity = get_destination("temperature-to-humidity", temperature)
#         location = get_destination("humidity-to-location", humidity)

#         locations2.append(location)
# print(min(locations2))  # first star
