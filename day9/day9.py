INPUT_TEST = r"input_test_day9.txt"
INPUT_REAL = r"input_real_day9.txt"

from collections import Counter

def get_list_of_lists_of_ints_from_file(fname: str = INPUT_TEST) -> list[list[int]]:
    with open(fname) as f:
        return [[int(n) for n in line.strip()] for line in f.readlines()]

def print_input(fname: str = INPUT_TEST):
    for line in get_list_of_lists_of_ints_from_file(fname):
        print(line)
    return

def part1(fname: str = INPUT_TEST) -> int:
    heightmap = get_list_of_lists_of_ints_from_file(fname)
    # for each number in heightmap, check if it is a local minimum
    # if it is, then add it to the list of local minima
    # return the sum of all local minima
    local_minima = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if is_local_minimum(heightmap,i,j):
                local_minima.append(heightmap[i][j])
    return sum(local_minima) + len(local_minima)

def part2(fname: str = INPUT_TEST) -> int:
    heightmap = get_list_of_lists_of_ints_from_file(fname)
    h = len(heightmap)
    w = len(heightmap[0])
    basinmap = [-1 for _ in range(h*w)] #flattened version of heightmap
    # find all basins in the heightmap
    # a basin is a group of numbers that are bounded by 9s or the edge of the heightmap
    # return a list of the sizes of the basins
    basin_ix = 0
    for i in range(h):
        for j in range(w):
            if heightmap[i][j] == 9 or basinmap[i*w+j] != -1:
                continue
            else:
                basinmap[i*w+j] = basin_ix
                basinmap = fill_basin(heightmap,basinmap,i,j,basin_ix)
                basin_ix += 1
    basin_count = Counter(basinmap)
    biggest_sizes = [e for ix,e in basin_count.most_common() if ix != -1][:3]
    print(f"{biggest_sizes = }")
    return biggest_sizes[0] * biggest_sizes[1] * biggest_sizes[2]

def fill_basin(heightmap: list[list[int]],basinmap: list[int],i: int,j: int,basin_ix: int) -> list[int]:
    # fill a basin in the basinmap
    # a basin is a group of numbers that are bounded by 9s or the edge of the heightmap
    # return the basinmap with the basin filled in
    h = len(heightmap)
    w = len(heightmap[0])
    neighbors = get_neighbors(heightmap,i,j)
    for i2,j2 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w: continue
        if heightmap[i2][j2] == 9: continue
        if basinmap[i2*w+j2] != -1: continue
        basinmap[i2*w+j2] = basin_ix
        basinmap = fill_basin(heightmap,basinmap,i2,j2,basin_ix)
    return basinmap


def is_local_minimum(heightmap: list[list[int]],i: int,j: int) -> bool:
    # check if the number at heightmap[i][j] is a local minimum
    # a local minimum is a number that is smaller than all of its neighbors
    # if it is, then return True
    # else return False
    neighbors = get_neighbors(heightmap,i,j)
    # print(f"{heightmap[i][j] = } | {neighbors = }")
    for n in neighbors:
        if heightmap[i][j] >= n:
            return False
    return True

def get_neighbors(heightmap: list[list[int]],i: int,j: int) -> list[int]:
    # get the neighbors of heightmap[i][j]
    # neighbors are the numbers in 4 adjacent squares (diag not included)
    # return a list of the neighbors
    neighbors = []
    if i > 0:
        neighbors.append(heightmap[i-1][j])
    if i < len(heightmap)-1:
        neighbors.append(heightmap[i+1][j])
    if j > 0:
        neighbors.append(heightmap[i][j-1])
    if j < len(heightmap[i])-1:
        neighbors.append(heightmap[i][j+1])
    return neighbors
    


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 15")
    print(f"{part1(INPUT_REAL) = }") # 576 is too low

    print(f"{part2(INPUT_TEST) = } | 1134")
    print(f"{part2(INPUT_REAL) = }") 