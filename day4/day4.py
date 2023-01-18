INPUT_TEST = r"input_day4_test.txt"
INPUT_REAL = r"input_day4_real.txt"

def return_list_and_boarrds_from_file(input_file: str = INPUT_TEST):
    with open(input_file) as f:
        list_numbers = next(f).strip().split(",")
        list_numbers = [int(num) for num in list_numbers]
        next(f)
        boards = []
        board = []
        for line in f:
            row = line.strip().replace("  "," ").split(' ')
            if len(row) == 1:
                boards.append(board)
                board = []
            else:
                row = [int(num) for num in row]
                board.append(row)
        boards.append(board)
    return list_numbers, boards

def check_if_board_wins(num_list: list[int], board: list[list[int]]) -> bool:
    # play bingo with board and num_list. If board wins return True, else False
    # if there is a row in board with all numbers in num_list, return True
    # if there is a column in board with all numbers in num_list, return True
    # else return False

    # check rows
    for row in board:
        if all(num in num_list for num in row):
            return True
    
    # check columns
    for i in range(len(board[0])):
        column = [row[i] for row in board]
        if all(num in num_list for num in column):
            return True
    
    return False


def sum_of_all_unmarked_numbers(num_list: list[int], board: list[list[int]]) -> int:
    # sum all numbers in board that are not in num_list
    sum_board = 0
    for row in board:
        for num in row:
            if num not in num_list:
                sum_board += num
    return sum_board


def part1(input_file = INPUT_TEST):
    list_numbers, boards = return_list_and_boarrds_from_file(input_file)
    num_list = []
    board_winning = None
    for num in list_numbers:
        num_list.append(num)
        for board in boards:
            if check_if_board_wins(num_list, board):
                board_winning = board
                # print(f"{board=}")
                break
        if board_winning:
            break
    sum_board = sum_of_all_unmarked_numbers(num_list, board_winning)
    # print(f"{sum_board=}")
    # print(f"{num_list=}")
    return sum_board*num_list[-1]

def part2(input_file = INPUT_TEST):
    list_numbers, boards = return_list_and_boarrds_from_file(input_file)
    num_list = []
    board_winning = None
    for num in list_numbers:
        num_list.append(num)
        for board in boards:
            if check_if_board_wins(num_list, board):
                boards.remove(board)
                if not boards:
                    board_winning = board
                    break
        if board_winning:
            break
    sum_board = sum_of_all_unmarked_numbers(num_list, board_winning)
    return sum_board*num_list[-1]


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST)=}") # test should be 4512        
    print(f"{part1(INPUT_REAL)=}") 
    print("")
    print(f"{part2(INPUT_TEST)=} should equal 1924") # test should be 4512
    print(f"{part2(INPUT_REAL)=}") 