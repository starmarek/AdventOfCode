from anytree import Node, PreOrderIter

with open("input.txt") as f:
    root = Node("/")
    current_node = None
    for line in f.read().splitlines():
        if line.startswith("$ cd"):
            if "/" in line:
                current_node = root
            elif ".." in line:
                current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.name == line.split()[2]:
                        current_node = child
                        break
            continue

        if line.startswith("dir"):
            Node(line.split()[1], parent=current_node)
            continue

        if line[0].isdigit():
            Node(line.split()[0], parent=current_node)
            continue

sizes_of_each_dir = []
file_sizes = []
for node in PreOrderIter(root):
    if not node.name[0].isdigit():
        c = 0
        for descendant in node.descendants:
            if descendant.name[0].isdigit():
                c += int(descendant.name)
        sizes_of_each_dir.append(c)
    else:
        file_sizes.append(int(node.name))

total_occupied_memory = sum(file_sizes)
memory_needed_for_update = 30000000
total_size = 70000000
space_required_to_be_freed = memory_needed_for_update - (
    total_size - total_occupied_memory
)

print(sum(filter(lambda x: x <= 100000, sizes_of_each_dir)))  # first star
print(
    min(filter(lambda x: x >= space_required_to_be_freed, sizes_of_each_dir))
)  # second star
