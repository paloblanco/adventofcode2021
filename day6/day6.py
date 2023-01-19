from collections import defaultdict

INPUT_TEST = r"input_test_day6.txt"
INPUT_REAL = r"input_real_day6.txt"

def return_list_of_integers_from_file(input_file: str = INPUT_TEST):
    with open(input_file) as f:
        list_numbers = next(f).strip().split(",")
        list_numbers = [int(num) for num in list_numbers]
    return list_numbers

def return_dict_of_timers_and_counts_from_list(list_times: list[int]) -> dict[int, int]:
    # return a dict with keys = times and values = number of times that time appears in list_times
    dict_times = defaultdict(int)
    for time in list_times:
        dict_times[time] += 1
    return dict_times

def execute_turns(dict_times: dict[int, int], turns: int = 80) -> dict[int, int]:
    # for each turn, create a new dict whose keys are 1 less than the keys in dict_times
    # if a key is 0, the value is copied to both 6 and 8
    for turn in range(turns):
        new_dict = defaultdict(int,{k-1: v for k, v in dict_times.items() if k != 0})
        new_dict[6] += dict_times[0]
        new_dict[8] += dict_times[0]
        dict_times = new_dict
    return dict_times

def part1(input_file = INPUT_TEST):
    list_times = return_list_of_integers_from_file(input_file)
    dict_times = return_dict_of_timers_and_counts_from_list(list_times)
    dict_final = execute_turns(dict_times, turns=80)
    total_entries = sum(dict_final.values())
    return total_entries

def part2(input_file = INPUT_TEST):
    list_times = return_list_of_integers_from_file(input_file)
    dict_times = return_dict_of_timers_and_counts_from_list(list_times)
    dict_final = execute_turns(dict_times, turns=256)
    total_entries = sum(dict_final.values())
    return total_entries


if __name__ == "__main__":
    print(f"{part1() = }")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2() = }")
    print(f"{part2(INPUT_REAL) = }")