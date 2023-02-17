import numpy as np
from dijkstar import Graph, NoPathError, find_path

with open("input.txt") as f:
    array = np.array([list(item) for item in f.read().splitlines()])
max_y, max_x = array.shape


def get_neighbors(array, indices):
    if indices[0] == 0:
        top = None
    else:
        top = array[indices[0] - 1, indices[1]]

    if indices[0] == max_y - 1:
        bottom = None
    else:
        bottom = array[indices[0] + 1, indices[1]]

    if indices[1] == 0:
        left = None
    else:
        left = array[indices[0], indices[1] - 1]

    if indices[1] == max_x - 1:
        right = None
    else:
        right = array[indices[0], indices[1] + 1]

    return left, right, top, bottom


def should_add_edge(source, dest):
    if dest is None:
        return False

    if dest == "S":
        dest = "a"
    elif dest == "E":
        dest = "z"

    return ord(dest) - ord(source) <= 1


graph = Graph()
list_of_a = []
for i, idx_el in enumerate(np.ndenumerate(array)):
    idx, element = idx_el
    if element == "S":
        start = i
        element = "a"
    elif element == "E":
        end = i
        element = "z"

    if element == "a":
        list_of_a.append(i)

    left, right, top, bottom = get_neighbors(array, idx)

    if should_add_edge(element, left):
        graph.add_edge(i, i - 1, 1)

    if should_add_edge(element, right):
        graph.add_edge(i, i + 1, 1)

    if should_add_edge(element, top):
        graph.add_edge(i, i - max_x, 1)

    if should_add_edge(element, bottom):
        graph.add_edge(i, i + max_x, 1)

print(find_path(graph, start, end).total_cost)  # first star

costs = []
for a in list_of_a:
    try:
        costs.append(find_path(graph, a, end).total_cost)
    except NoPathError:
        continue
print(min(costs))  # second star
