import os


def main():
    os.chdir(os.path.dirname(__file__))

    input = open("day13_input.txt").read().splitlines()

    print(solve(input))


# class Layer:
#     def __init__(self, d, r):
#         self.d = d
#         self.r = r
#         self.loc = 0
#         self.dir = '+'
#
#     def move(self):
#         if self.loc == self.r - 1:
#             self.dir = '-'
#         if self.loc == 0:
#             self.dir = '+'
#         if self.dir == '+':
#             self.loc += 1
#         if self.dir == '-':
#             self.loc -= 1
#
#     def __str__(self):
#         return ''.join(['[S]' if i == self.loc else '[ ]' for i in range(self.r)])
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Firewall:
#     def __init__(self, input):
#         self.layers = {}
#         for line in input:
#             d, r = list(map(int, line.split(': ')))
#             self.layers[d] = Layer(d, r)
#
#         missing = [i for i in range(max(self.layers.keys())) if i not in self.layers.keys()]
#         for i in missing:
#             self.layers[i] = 'empty'
#
#         self.last = max(self.layers.keys())
#
#     def run(self):
#         for key in self.layers.keys():
#             if self.layers[key] != 'empty':
#                 self.layers[key].move()
#
#     def __str__(self):
#         output = ''
#         for layer in sorted(self.layers.keys()):
#             if layer != 'empty':
#                 output += f'{layer}: {self.layers[layer]}\n'
#             else:
#                 output += f'{layer}: ...\n'
#         return output


fw = {}

def check_collision(layer, depth):
    return layer % ((depth - 1) * 2) == 0

def solve(input):
    severity = 0
    for line in input:
        layer, depth = list(map(int, line.split(': ')))
        fw[layer] = depth
    for layer, depth in fw.items():
        if check_collision(layer, depth):
            severity += layer * depth
    # fw = Firewall(input)
    # pos = 0
    # severity = 0
    # while pos < fw.last + 1:
    #     if fw.layers[pos] != 'empty':
    #         if fw.layers[pos].loc == 0:
    #             severity += pos * fw.layers[pos].r
    #     fw.run()
    #     pos += 1
    #
    return severity


if __name__ == '__main__':
    main()
