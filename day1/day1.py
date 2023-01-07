INPUT_TEST = r"data_test_day1.txt"
INPUT_REAL = r"data_real_day1.txt"

def return_list_of_ints(fname=INPUT_TEST):
    with open(fname) as f:
        return [int(line) for line in f.readlines()]

def count_times_number_increases(data: list[int]) -> int:
    return sum([1 for i in range(len(data)-1) if data[i] < data[i+1]])

def rolling_sum_from_list(data: list[int], window: int = 3) -> list[int]:
    return [sum(data[i:i+window]) for i in range(len(data)-window+1)]

def part1(fname=INPUT_TEST):
    data = return_list_of_ints(fname)
    return count_times_number_increases(data)

def part2(fname=INPUT_TEST):
    data = return_list_of_ints(fname)
    rolling_sum = rolling_sum_from_list(data)
    return count_times_number_increases(rolling_sum)


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST)=}")
    print(f"{part1(INPUT_REAL)=}")

    print("")

    print(f"{part2(INPUT_TEST)=}")
    print(f"{part2(INPUT_REAL)=}")