INPUT_TEST = r"data_test_day3.txt"
INPUT_REAL = r"data_real_day3.txt"

def return_list_of_integers_from_binary_file(fname=INPUT_TEST) -> list[int]:
    with open(fname) as f:
        return [int(line,2) for line in f.readlines()]

def part1(fname=INPUT_TEST) -> int:
    data = return_list_of_integers_from_binary_file(fname)
    max_bit_length = len(bin(max(data))) - 2
    gamma = 0
    for i in range(max_bit_length):
        # for each number in data, check if the bit at position i is 1  or 0
        # if 1 occurs more than 0, then gamma is 1 at position i
        # if 0 occurs more than 1, then gamma is 0 at position i
        gamma += 2**i * (sum([1 for number in data if number & 2**i]) > len(data)/2)
    # epsilon is a binary number with length max_bit_length and is the opposite of gamma
    epsilon = 2**max_bit_length - gamma - 1
    return gamma * epsilon

def part2(fname=INPUT_TEST) -> int:
    data = return_list_of_integers_from_binary_file(fname)
    max_bit_length = len(bin(max(data))) - 2
    candidates_o2 = [n for n in data]
    candidates_co2 = [n for n in data]
    for i in range(max_bit_length)[::-1]:
        # i+=1
        most_common_bit_o2 = sum([1 for number in candidates_o2 if number & 2**i]) >= len(candidates_o2)/2
        least_common_bit_co2 = sum([1 for number in candidates_co2 if number & 2**i]) < len(candidates_co2)/2
        candidates_o2 = [n for n in candidates_o2 if n & 2**i == most_common_bit_o2*2**i]
        candidates_co2 = [n for n in candidates_co2 if n & 2**i == least_common_bit_co2*2**i]
        if len(candidates_o2) == 1:
            o2_rating = candidates_o2[0]
        if len(candidates_co2) == 1:
            co2_rating = candidates_co2[0]
    return o2_rating * co2_rating

if __name__ == "__main__":
    print(f"{part1(INPUT_TEST)=}")
    print(f"{part1(INPUT_REAL)=}")

    print(f"{part2(INPUT_TEST)=}")
    print(f"{part2(INPUT_REAL)=}")