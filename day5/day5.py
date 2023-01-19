from collections import defaultdict

INPUT_TEST = r"input_test_day5.txt"
INPUT_REAL = r"input_real_day5.txt"

def return_list_of_pairs_of_tuples_from_file(input_file: str = INPUT_TEST):
    with open(input_file) as f:
        list_of_pairs_of_tuples = []
        for line in f:
            pairs = line.strip().split(" -> ")
            left = tuple(int(e) for e in pairs[0].split(","))
            right = tuple(int(e) for e in pairs[1].split(","))
            list_of_pairs_of_tuples.append([left, right])
    return list_of_pairs_of_tuples


def get_overlaps(input_file = INPUT_TEST, diagonal=False):
    # consider all points in the range of each pair of points, and count how many occur twice or more
    list_of_pairs_of_tuples = return_list_of_pairs_of_tuples_from_file(input_file)
    counter = defaultdict(int)
    overlaps = 0
    for pair in list_of_pairs_of_tuples:
        maxx = max(pair[0][0], pair[1][0])
        maxy = max(pair[0][1], pair[1][1])
        minx = min(pair[0][0], pair[1][0])
        miny = min(pair[0][1], pair[1][1])
        if not (maxx == minx or maxy == miny): #only consider straight lines
            if not diagonal:
                continue
            else:
                deltax = (pair[1][0] - pair[0][0]) / abs(pair[1][0] - pair[0][0])
                deltay = (pair[1][1] - pair[0][1]) / abs(pair[1][1] - pair[0][1])
                x0 = pair[0][0]
                y0 = pair[0][1]
                for i in range(maxx-minx+1):
                    counter[(x0+i*deltax, y0+i*deltay)] += 1
                    if counter[(x0+i*deltax, y0+i*deltay)] == 2:
                        overlaps += 1
                continue
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                counter[(x,y)] += 1
                if counter[(x,y)] == 2:
                    overlaps += 1
    return overlaps

def part1(input_file = INPUT_TEST):
    return get_overlaps(input_file)

def part2(input_file = INPUT_TEST):
    return get_overlaps(input_file, diagonal=True)

if __name__ == "__main__":
    print(f"{part1() = }")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2() = }")
    print(f"{part2(INPUT_REAL) = }")