INPUT_TEST = r"input_test_day15.txt"
INPUT_REAL = r"input_real_day15.txt"

from heapq import heappush, heappop, heapify

def return_list_of_lists_of_ints_from_file(fname: str = INPUT_TEST) -> list[list[int]]:
    with open(fname) as f:
        return [[int(e) for e in line.strip()] for line in f]

def print_map_getter(fname: str = INPUT_TEST) -> None:
    for line in return_list_of_lists_of_ints_from_file(fname):
        print(line)

def print_map(risk_map: list[list[int]]) -> None:
    for line in risk_map:
        print(''.join([str(e) for e in line]))

class Location:
    def __init__(self, x: int, y: int, risk: int) -> None:
        self.x = x
        self.y = y
        self.risk = risk
    
    def __lt__(self, other: "Location") -> bool:
        return self.risk < other.risk

def part1(fname: str = INPUT_TEST) -> int:
    risk_map = return_list_of_lists_of_ints_from_file(fname)
    # find the lowest risk path from [0][0] to [-1][-1]
    # risk is calculated by adding the risk of each square that is entered
    frontier = []
    explored = {}
    end = (len(risk_map)-1, len(risk_map[0])-1)
    heappush(frontier, Location(0,0,0))
    explored[(0,0)] = 0
    while frontier:
        location = heappop(frontier)
        x,y,risk = location.x, location.y, location.risk
        if (x,y) == end:
            return risk
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        neighbors = [(x,y) for x,y in neighbors if 0 <= x < len(risk_map) and 0 <= y < len(risk_map[0])]
        for x1,y1 in neighbors:
            risk1 = risk + risk_map[x1][y1]
            if (x1,y1) not in explored or risk1 < explored[(x1,y1)]:
                explored[(x1,y1)] = risk1
                heappush(frontier, Location(x1,y1,risk1))
    return None

def expand_map(risk_map: list[list[int]]) -> list[list[int]]:
    # grow the map 5x in each dimension, increasing each element by 1
    # horizontal first:
    for i in range(len(risk_map)):
        original_row = [e for e in risk_map[i]]
        for j in range(1,5):
            risk_map[i] = risk_map[i] + [(((e-1)+j)%9)+1 for e in original_row]
    # now vertical
    height = len(risk_map)
    for i in range(1,5):
        for j in range(height):
            risk_map = risk_map + [[(((e-1)+i)%9)+1 for e in risk_map[j]]]
    return risk_map


def part2(fname: str = INPUT_TEST) -> int:
    risk_map = return_list_of_lists_of_ints_from_file(fname)
    risk_map = expand_map(risk_map)
    # print_map(risk_map)
    # find the lowest risk path from [0][0] to [-1][-1]
    # risk is calculated by adding the risk of each square that is entered
    frontier = []
    explored = {}
    end = (len(risk_map)-1, len(risk_map[0])-1)
    heappush(frontier, Location(0,0,0))
    explored[(0,0)] = 0
    while frontier:
        location = heappop(frontier)
        x,y,risk = location.x, location.y, location.risk
        if (x,y) == end:
            return risk
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        neighbors = [(x,y) for x,y in neighbors if 0 <= x < len(risk_map) and 0 <= y < len(risk_map[0])]
        for x1,y1 in neighbors:
            risk1 = risk + risk_map[x1][y1]
            if (x1,y1) not in explored or risk1 < explored[(x1,y1)]:
                explored[(x1,y1)] = risk1
                heappush(frontier, Location(x1,y1,risk1))
    return None


if __name__ == "__main__":
    # print_map_getter(INPUT_TEST)
    print(f"{part1(INPUT_TEST) = } | 40")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2(INPUT_TEST) = } | 315")
    print(f"{part2(INPUT_REAL) = }")