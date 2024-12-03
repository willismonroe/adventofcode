from math import prod



def main():
    raw_input = open('day16_input.txt').read()
    print("Part 1:", part1(raw_input))
    print("Part 2:", part2(raw_input))


example_input = """"""


class Bitstream:
    def __init__(self, data):
        rawdata = bytes.fromhex(data)

        self.pos = 0
        self.bits = ''.join(map('{:08b}'.format, rawdata))

    def decode_int(self, nbits):
        res = int(self.bits[self.pos:self.pos + nbits], 2)
        self.pos += nbits
        return res

    def decode_one_packet(self):
        version = self.decode_int(3)
        tid = self.decode_int(3)
        data = self.decode_packet_data(tid)
        return (version, tid, data)

    def decode_value_data(self):
        value = 0
        group = 0b10000

        while group & 0b10000:
            group = self.decode_int(5)
            value <<= 4
            value += group & 0b1111

        return value

    def decode_n_packets(self, n):
        return [self.decode_one_packet() for _ in range(n)]

    def decode_len_packets(self, length):
        end = self.pos + length
        pkts = []

        while self.pos < end:
            pkts.append(self.decode_one_packet())

        return pkts

    def decode_operator_data(self):
        ltid = self.decode_int(1)

        if ltid == 1:
            return self.decode_n_packets(self.decode_int(11))

        return self.decode_len_packets(self.decode_int(15))

    def decode_packet_data(self, tid):
        if tid == 4:
            return self.decode_value_data()
        return self.decode_operator_data()


def sum_version(packet):
    v, tid, data = packet
    
    if tid == 4:
        return v

    return v + sum(map(sum_version, data))


def evaluate(packet):
    _, tid, data = packet

    if tid == 4:
        return data

    values = map(evaluate, data)
    if tid == 0: return sum(values)
    if tid == 1: return prod(values)
    if tid == 2: return min(values)
    if tid == 3: return max(values)

    a, b = values

    if tid == 5: return int(a > b)
    if tid == 6: return int(a < b)
    return int(a == b)

def part1(raw_input):
    stream = Bitstream(raw_input)
    packet = stream.decode_one_packet()
    vsum = sum_version(packet)

    return vsum


def part2(raw_input):
    stream = Bitstream(raw_input)
    packet = stream.decode_one_packet()

    return evaluate(packet)


if __name__ == "__main__":
    main()
