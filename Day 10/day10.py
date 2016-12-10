

class Bot:
    def __init__(self, chip):
        self.chips = [chip]

    def __getattr__(self, item):
        if item == 'high' and len(self.chips) == 2:
            return list(map(str, sorted(map(int, self.chips))))[1]
        elif item =='low' and len(self.chips) == 2:
            return list(map(str, sorted(map(int, self.chips))))[0]

    def has_two_chips(self):
        return len(self.chips) == 2

    def give_chips(self):
        if self.has_two_chips():
            chips = list(map(str, sorted(map(int, self.chips))))
            self.chips = []
            return chips
        else:
            print("ERROR: Do not have two chips to give.")

def solve(data, answer_chips=['17','61'], part2=False):
    bots = {}
    outputs = {}
    data = [line.split() for line in data]
    # give all the bots chips
    for line in data:
        if line[0] == 'value':
            print("LINE: \"{}\".".format(' '.join(line)))
            # ['value', '5', 'goes', 'to', 'bot', '2']
            if line[-1] in bots.keys():
                bots[line[-1]].chips.append(line[1])
                #print("Bot # {} gets its second chip with value: {}.".format(line[-1], line[1]))
            else:
                #print("Creating Bot #{} with value: {}.".format(line[-1], line[1]))
                bots[line[-1]] = Bot(line[1])
            #data.remove(line)
    data = [line for line in data if line[0] != 'value']
    print("Done giving bots chips.\n")
    part1 = 0
    action = 1
    new_data = []
    while action:
        action = 0
        for line in data:
            for key in bots.keys():
                if bots[key].has_two_chips():
                    if sorted(bots[key].chips) == answer_chips:
                        #print("Solved it with Bot #{} with chips: {}.".format(key, sorted(bots[key].chips)))
                        part1 = key
            if line[0] == 'bot':
                # ['bot', '200', 'gives', 'low', 'to', 'bot', '40', 'and', 'high', 'to', 'bot', '141']
                if line[1] in bots.keys():
                    giver = bots[line[1]]
                    if giver.has_two_chips():
                        print("LINE: \"{}\".".format(' '.join(line)))
                        print("Giver Bot #{} has chips: {}.".format(line[1], list(map(str, sorted(map(int, giver.chips))))))
                        low, high = giver.give_chips()
                        if line[5] == 'bot':
                            if line[6] in bots.keys():
                                print("It gives low chip {} to existing Bot #{}.".format(low, line[6]))
                                bots[line[6]].chips.append(low)
                            else:
                                print("It gives low chip {} to new Bot #{}.".format(low, line[6]))
                                bots[line[6]] = Bot(low)
                        elif line[5] == 'output':
                            outputs[line[6]] = low
                            print("Dumping low chip {} into output #{}.".format(low, line[6]))

                        if line[10] == 'bot':
                            if line[11] in bots.keys():
                                print("It gives high chip {} to existing Bot #{}.".format(high, line[11]))
                                bots[line[11]].chips.append(high)
                            else:
                                print("It gives high chip {} to new Bot #{}.".format(high, line[11]))
                                bots[line[11]] = Bot(high)
                        elif line[10] == 'output':
                            outputs[line[11]] = high
                            print("Dumping high chip {} into output #{}.".format(high, line[11]))

                        # exchange done, remove the line
                        #data.remove(line)
                        action = 1

                    else:
                        #print("Bot #{} doesn't have two chips.".format((line[1])))
                        new_data.append(line)
                else:
                    #print("Bot #{} has no chips yet.".format(line[1]))
                    new_data.append(line)
        data = new_data[:]
        new_data = []
    print("No more actions.")
    if part2:
        print(outputs)
        return int(outputs['0']) * int(outputs['1']) * int(outputs['2'])
    else:
        return part1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    print(solve(data, part2=True))