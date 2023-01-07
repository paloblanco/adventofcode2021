INPUT_TEST = r"data_test_day2.txt"
INPUT_REAL = r"data_real_day2.txt"

def return_tuples_from_file(fname=INPUT_TEST) -> list[tuple[str, int]]:
    with open(fname) as f:
        return [(line.split()[0], int(line.split()[1])) for line in f.readlines()] 

def part1(fname=INPUT_TEST) -> int:
    data = return_tuples_from_file(fname)
    horizontal = 0
    depth = 0
    for direction, distance in data:
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
    return horizontal * depth

def part2(fname=INPUT_TEST) -> int:
    data = return_tuples_from_file(fname)
    horizontal = 0
    depth = 0
    aim = 0
    for direction, distance in data:
        if direction == "forward":
            horizontal += distance
            depth += aim*distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return horizontal * depth

if __name__ == "__main__":
    print(f"{part1(INPUT_TEST)=}")
    print(f"{part1(INPUT_REAL)=}")

    print("")

    print(f"{part2(INPUT_TEST)=}")
    print(f"{part2(INPUT_REAL)=}")