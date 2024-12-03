import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.contents = []

    def __str__(self) -> str:
        return f"{self.name}"

    def get_path(self) -> str:
        pass

    def get_size(self) -> int:
        size = 0

        def walk(path):
            for p in path.contents:
                if isinstance(p, File):
                    yield p.size
                else:
                    yield from walk(p)

        return sum(walk(self))


def print_directory(d, indent="", with_size=False):
    for i in d.contents:
        if isinstance(i, Directory):
            print(
                "- "
                + indent
                + i.name
                + ":"
                + (str(sum(i.get_size())) if with_size else "")
            )
            print_directory(i, indent + "  ", with_size)
        else:
            print(indent + i.name + " " + str(i.size))


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = int(size)

    def __str__(self) -> str:
        return self.name


def parse_input(input):
    lines = input.splitlines()
    root = None
    cwd = None
    dir = []
    for line in lines:
        # print("_______________")
        # print(f"Line: \t{line}")
        # if root != None:
        #     print_directory(root)
        #     print()
        if line.startswith("$"):
            # command
            cmd = line.split()[1:]
            if cmd[0] == "cd":
                if cmd[1] == "..":
                    cwd = cwd.parent
                else:
                    if cwd != None:
                        cwd = [i for i in cwd.contents if cmd[1] == i.name][0]
                    else:
                        cwd = Directory(cmd[1], cwd)
                    if root == None:
                        root = cwd
        else:
            # directory listing
            a, b = line.split()
            # print("\tAdd file: \t", b, a)
            if a == "dir":
                cwd.contents.append(Directory(b, cwd))
            else:
                cwd.contents.append(File(b, a))
            # print(f"\t{cwd} Contents: ", list(map(str, cwd.contents)))
    return root


# example_input = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""
# a = parse_input(example_input)


def part1(input):
    root = parse_input(input)

    def walk(d):
        size = d.get_size()
        # print(f"{d} sum " + str(size))
        if size < 100000:
            # print(d.name + "**")
            yield size
        for i in d.contents:
            if isinstance(i, Directory):
                # print(f"{i} walk")
                yield from walk(i)

    return sum(walk(root))


def part2(input):
    root = parse_input(input)
    needed_space = 30000000 - (70000000 - root.get_size())

    def walk(d):
        size = d.get_size()
        # print(f"{d} sum " + str(size))
        if size >= needed_space:
            # print(d.name + "**")
            yield size
        for i in d.contents:
            if isinstance(i, Directory):
                # print(f"{i} walk")
                yield from walk(i)
    sizes = sorted(list(walk(root)))
    # print(sizes)

    return sizes[0]


if __name__ == "__main__":
    with open(PUZZLE_DIR / "input.txt") as f:
        input = f.read()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
