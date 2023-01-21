INPUT_TEST = r"input_test_day10.txt"
INPUT_REAL = r"input_real_day10.txt"

SCORING = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}

SCORING2 = {
    "(":1, # use the opening characters for convenience
    "[":2,
    "{":3,
    "<":4,
} 

def get_lines_from_file(fname: str = INPUT_TEST) -> list[str]:
    with open(fname) as f:
        return [line.strip() for line in f.readlines()]

def part1(fname: str = INPUT_TEST) -> int:
    lines = get_lines_from_file(fname)
    running_total = 0
    for line in lines:
        bad_character = check_syntax(line)
        if type(bad_character) == str:
            running_total += SCORING[bad_character]
    return running_total

def part2(fname: str = INPUT_TEST) -> int:
    lines = get_lines_from_file(fname)
    scores = []
    for line in lines:
        complete_string_list = check_syntax(line)
        if type(complete_string_list) == list:
            scores.append(get_score2(complete_string_list))
    # return the middle value in scores
    scores.sort()
    return scores[len(scores)//2]

def get_score2(complete_string: list[str]) -> int:
    score = 0
    while complete_string:
        score *= 5
        score += SCORING2[complete_string.pop()]
    return score


def check_syntax(line: str) -> str | list[str]:
    # check a line to make sure each opening character has a matching closing character
    # ( should be closed with ), [ should be closed with ], { should be closed with }, and < should be closed with >
    # if the wrong character closes a group, return the closing character
    # if the line is syntactically correct, return None
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            if len(stack) == 0:
                return c
            else:
                open_char = stack.pop()
                if open_char == "(" and c != ")":
                    return c
                elif open_char == "[" and c != "]":
                    return c
                elif open_char == "{" and c != "}":
                    return c
                elif open_char == "<" and c != ">":
                    return c
    return stack


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 26397")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2(INPUT_TEST) = } | 288957")
    print(f"{part2(INPUT_REAL) = }")