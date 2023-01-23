INPUT_TEST = r"input_test_day16.txt"
INPUT_REAL = r"input_real_day16.txt"

def get_hex_from_file(fname: str = INPUT_TEST) -> str:
    with open(fname) as f:
        return f.read().strip()

def h2b(hex_string: str) -> str:
    return "".join([f"{int(e, 16):04b}" for e in hex_string])

def part1(fname: str = INPUT_TEST) -> int:
    hex_string = get_hex_from_file(fname)
    bit_string = h2b(hex_string)
    packet = Packet(bit_string)
    version_sum = 0
    packs = [packet]
    while packs:
        pack = packs.pop()
        version_sum += pack.version_value
        packs.extend(pack.sub_packets)
    return version_sum

def part2(fname: str = INPUT_TEST) -> int:
    hex_string = get_hex_from_file(fname)
    bit_string = h2b(hex_string)
    packet = Packet(bit_string)
    return packet.value

class Packet:

    def __init__(self, bit_string: str):
        self.version = bit_string[:3]
        self.version_value = int(self.version, 2)
        self.type_id = bit_string[3:6]
        self.payload = bit_string[6:]
        self.type = "value" if self.type_id == "100" else "operator"
        self.sub_packets = []
        self.value = None
        self.length_type = None # 0 means 15 next, 1 means 11 next
        self.leftover = ''
        if self.type == "operator":
            self.length_type = self.payload[0]
            self.payload = self.payload[1:]
            self.sub_packets, self.leftover = self.get_sub_packets()
            self.value = self.evaluate()
        else:
            self.value, self.leftover = self.get_value()

    def evaluate(self) -> int:
        match int(self.type_id,2):
            case 0:
                return sum([p.value for p in self.sub_packets])
            case 1:
                values = [p.value for p in self.sub_packets]
                product = 1
                for v in values:
                    product *= v
                return product
            case 2:
                return min([p.value for p in self.sub_packets])
            case 3:
                return max([p.value for p in self.sub_packets])
            case 5:
                return 1 if self.sub_packets[0].value > self.sub_packets[1].value else 0
            case 6:
                return 1 if self.sub_packets[0].value < self.sub_packets[1].value else 0
            case 7:
                return 1 if self.sub_packets[0].value == self.sub_packets[1].value else 0

    def get_value(self) -> int:
        reading = True
        group = 0
        bitstring = ""
        while reading:
            offset = group*5
            bitstring += self.payload[offset+1:offset+5]
            if self.payload[offset] == "0":
                reading = False
            group += 1
        leftover = self.payload[group*5:]
        return int(bitstring, 2), leftover

    def get_sub_packets(self) -> list['Packet']:
        packets = []
        if self.length_type == "0":
            length = int(self.payload[:15], 2)
            contents = self.payload[15:length+15]
            leftover = self.payload[length+15:]
            while contents:
                packet = Packet(contents)
                packets.append(packet)
                contents = packet.leftover
            return packets, leftover
        else:
            num_packets = int(self.payload[:11], 2)
            contents = self.payload[11:]
            for i in range(num_packets):
                packet = Packet(contents)
                packets.append(packet)
                contents = packet.leftover
            return packets, contents


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 31")
    
    hex1 = "D2FE28"

    p1 = Packet(h2b(hex1))
    print(f"{p1.version = } | 110")
    print(f"{p1.type_id = } | 100")
    print(f"{p1.value = } | 2021")
    print(f"{p1.leftover = } | 000")

    hex2 = "38006F45291200"
    p2 = Packet(h2b(hex2))
    print(f"{p2.version = } | 001")
    print(f"{p2.type_id = } | 110")
    print(f"{p2.leftover = } | 0000000")
    for p in p2.sub_packets:
        print(f"{p.value = }")
        print(f"{p.leftover = }")

    hex3 = "EE00D40C823060"
    p3 = Packet(h2b(hex3))
    print(f"{p3.version = } | 111")
    print(f"{p3.type_id = } | 011")
    print(f"{p3.leftover = } | 00000")
    for p in p3.sub_packets:
        print(f"{p.value = }")
        # print(f"{p.leftover = }")

    print(f"{part1(INPUT_TEST) = } | 31")
    print(f"{part1(INPUT_REAL) = }")

    h21 = "9C0141080250320F1802104A08"
    p = Packet(h2b(h21))
    print(f"{p.value = } | 1")

    print(f"{part2(INPUT_REAL) = }")