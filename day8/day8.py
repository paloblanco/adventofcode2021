INPUT_TEST = r"input_test_day8.txt"
INPUT_REAL = r"input_real_day8.txt"

def get_display_tuples_from_file(fname: str = INPUT_TEST) -> list[tuple[list[str],list[str]]]:
    with open(fname) as f:
        return [(line.split(" | ")[0].strip().split(" "),line.split("|")[-1].strip().split(" ")) for line in f.readlines()]

def part1(fname: str = INPUT_TEST) -> int:
    display_tuples = get_display_tuples_from_file(fname)
    digits_1478 = 0
    for _,outs in display_tuples:
        for digit in outs:
            if len(digit) in [2,4,3,7]: # line segs in 1,4,7,8
                digits_1478 += 1
    return digits_1478

def part2(fname: str = INPUT_TEST) -> int:
    display_tuples = get_display_tuples_from_file(fname)
    # for each tuple, determine the four digit number that is displayed
    # return the sum of all four digit numbers
    displayed_numbers = []
    for keys,outs in display_tuples:
        displayed_numbers.append(get_displayed_number(keys,outs))
    return sum(displayed_numbers)

def get_displayed_number(keys: list[str],outs: list[str]) -> int:
    # print(f"{keys = } | {outs = }")
    str_to_digit = get_str_to_digit_dict(keys)
    digit_str = ""
    for out in outs:
        # if out is an anagram of a key in str_to_digit, then get the corresponding digit
        for k,v in str_to_digit.items():
            if set(k) == set(out):
                digit_str += v
                break
    # print(f"{outs = } | {digit_str = }")
    return int(digit_str)

def get_str_to_digit_dict(keys: list[str]) -> dict[str,str]:
    str_to_digit = {}
    # knock out the easy ones first
    for k in keys:
        match len(k):
            case 2:
                str_to_digit[k] = "1"
            case 4:
                str_to_digit[k] = "4"
            case 3:
                str_to_digit[k] = "7"
            case 7:
                str_to_digit[k] = "8"
    # 6segs = [0,6,9], 5segs = [2,3,5]
    digit_to_str_easy = {v:k for k,v in str_to_digit.items()}
    for k in keys:
        if len(k) == 6:
            if len(set(k) & set(digit_to_str_easy["1"])) == 1:
                str_to_digit[k] = "6"
            elif len(set(k) & set(digit_to_str_easy["4"])) == 4:
                str_to_digit[k] = "9"
            else:
                str_to_digit[k] = "0"
        elif len(k) == 5:
            if len(set(k) & set(digit_to_str_easy["1"])) == 2:
                str_to_digit[k] = "3"
            elif len(set(k) & set(digit_to_str_easy["4"])) == 3:
                str_to_digit[k] = "5"
            else:
                str_to_digit[k] = "2"
    return str_to_digit


def print_display_tuples(fname: str = INPUT_TEST) -> None:
    display_tuples = get_display_tuples_from_file(fname)
    for ins,outs in display_tuples:
        print(f"input: {ins} | output: {outs}")

if __name__ == "__main__":
    # print_display_tuples(INPUT_TEST)
    print(f"{part1(INPUT_TEST) = }, should be 26")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2(INPUT_TEST) = }, should be 61229")
    print(f"{part2(INPUT_REAL) = }")