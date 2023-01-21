from collections import Counter

INPUT_TEST = r"input_test_day7.txt"
INPUT_REAL = r"input_real_day7.txt"

def return_list_of_integers_from_file(input_file: str = INPUT_TEST):
    with open(input_file) as f:
        list_numbers = next(f).strip().split(",")
        list_numbers = [int(num) for num in list_numbers]
    return list_numbers


def part1(input_file = INPUT_TEST):
    list_numbers = return_list_of_integers_from_file(input_file)
    # find the integer in the range min(list_numbers) to max(list_numbers) that is the shortest distance from all other numbers in list_numbers
    # if there are multiple numbers with the same shortest distance, return the smallest of them
    counter_list_numbers = Counter(list_numbers)
    best_answer = sum(list_numbers)
    current_answer = None
    for candidate in range(min(list_numbers), max(list_numbers)+1):
        sum_distance = sum([abs(cnt*(num-candidate)) for num,cnt in counter_list_numbers.items()])
        if sum_distance < best_answer:
            best_answer = sum_distance
            current_answer = candidate
    return best_answer


def part2(input_file = INPUT_TEST):
    list_numbers = return_list_of_integers_from_file(input_file)

    # list_numbers = [1,2,5]
    # find the integer in the range min(list_numbers) to max(list_numbers) that is the shortest distance from all other numbers in list_numbers
    # distance is calculated as triangular number, n(n+1)/2
    # if there are multiple numbers with the same shortest distance, return the smallest of them
    counter_list_numbers = Counter(list_numbers)
    best_answer = sum(list_numbers)**2
    current_answer = None
    for candidate in range(min(list_numbers), max(list_numbers)+1):
        sum_distance = sum([cnt*((abs(num-candidate)*(abs(num-candidate)+1))//2) for num,cnt in counter_list_numbers.items()])
        if sum_distance < best_answer:
            best_answer = sum_distance
            current_answer = candidate
    return best_answer

if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = }  and it should be 37")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2(INPUT_TEST) = }  and it should be 168")
    print(f"{part2(INPUT_REAL) = }")