def main():
    # solve for puzzle input
    input = open("day07_input.txt").read().splitlines()

    print(solve(input))


class Node:
    def __init__(self, name, weight=0, children=[], parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent

def construct_tree(input):
    lookup_table = {}
    for line in input:
        line = line.split()
        name = line[0]
        weight = int(line[1][1:-1])
        if len(line) == 2:
            # no children
            if name in lookup_table.keys():
                lookup_table[name].weight = weight
            else:
                lookup_table[name] = Node(name, weight)
        else:
            children = []
            for child in [child.strip(',') for child in line[3:]]:
                if child not in lookup_table.keys():
                    lookup_table[child] = Node(child, parent=name)
                children.append(lookup_table[child])
                lookup_table[child].parent = [name]
            if name in lookup_table.keys():
                lookup_table[name].weight = weight
                lookup_table[name].children = children
            else:
                lookup_table[name] = Node(name, weight, children)

    return lookup_table


def solve(input):
    tree = construct_tree(input)

    for node in tree.keys():
        if tree[node].parent == None:
            return node


if __name__ == "__main__":
    main()
