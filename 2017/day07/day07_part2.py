from collections import Counter


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
        self.disc_weight = 0
        self.total_weight = 0

    def compute_weight(self):
        if not self.children:
            self.total_weight = self.weight
            return self.total_weight
        else:
            for child in self.children:
                self.disc_weight += child.compute_weight()
            self.total_weight = self.disc_weight + self.weight
            return self.total_weight


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
            if name in lookup_table.keys():
                lookup_table[name].weight = weight
            else:
                lookup_table[name] = Node(name, weight)
            children = []
            for child in [child.strip(',') for child in line[3:]]:
                if child not in lookup_table.keys():
                    lookup_table[child] = Node(child, parent=lookup_table[name])
                children.append(lookup_table[child])
                lookup_table[child].parent = lookup_table[name]
            lookup_table[name].children = children

    return lookup_table


def balanced(node):
    weights = Counter([child.total_weight for child in node.children])
    (target, _), (failure, _) = weights.most_common()
    for child in node.children:
        if child.total_weight == target:
            pass
        else:
            grandchildren_weights = Counter([grandchild.total_weight for grandchild in child.children])
            if len(grandchildren_weights) == 1:
                return child
            else:
                return balanced(child)


def solve(input):
    tree = construct_tree(input)

    parent = tree[[node for node in tree.keys() if tree[node].parent is None][0]]

    parent.compute_weight()

    failed_node = balanced(parent)

    (target, _), (failure, _) = Counter([child.total_weight for child in failed_node.parent.children]).most_common()

    new_weight = failed_node.weight

    if target > failed_node.total_weight:
        new_weight = failed_node.weight + (target - failed_node.total_weight)
    elif failed_node.total_weight > target:
        new_weight = failed_node.weight - (failed_node.total_weight - target)

    return new_weight


if __name__ == "__main__":
    main()
