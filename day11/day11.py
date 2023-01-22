from collections import defaultdict
from itertools import product

INPUT_TEST = r"input_test_day11.txt"
INPUT_REAL = r"input_real_day11.txt"

def return_list_of_lists_of_ints_from_file(fname: str = INPUT_TEST) -> list[list[int]]:
    with open(fname) as f:
        return [[int(n) for n in line.strip()] for line in f.readlines()]

def part1(fname: str = INPUT_TEST, turns = 100) -> int:
    grid = return_list_of_lists_of_ints_from_file(fname)
    # for each turn, update the grid
    flashes = 0
    for t in range(turns):
        grid,flashes_turn = update_grid(grid)
        flashes += flashes_turn
    return flashes

def part2(fname: str = INPUT_TEST) -> int:
    grid = return_list_of_lists_of_ints_from_file(fname)
    # for each turn, update the grid
    # when flashes_turn == len(grid)*len(grid[0]), return the number of turns
    t=0
    while True:
        grid,flashes_turn = update_grid(grid)
        t += 1
        if flashes_turn == len(grid)*len(grid[0]):
            return t

def update_grid(grid: list[list[int]]) -> tuple[list[list[int]],int]:
        # update the grid
        # return the new grid and the number of flashes
        flash_tracker = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1
                grid[i][j] *= 1-flash_tracker[(i,j)]
                if grid[i][j] > 9:
                    flash_cell(grid,i,j,flash_tracker)
        return grid,sum([v for v in flash_tracker.values()])

def flash_cell(grid: list[list[int]],i: int,j: int,flash_tracker: dict) -> None:        
    # flash a cell and its neighbors
    # return None
    grid[i][j] = 0
    flash_tracker[(i,j)] = 1
    for i2,j2 in product([i-1,i,i+1],[j-1,j,j+1]):
        if i2 < 0 or i2 >= len(grid) or j2 < 0 or j2 >= len(grid[i2]): continue
        if (i2,j2) == (i,j): continue
        grid[i2][j2] += 1
        grid[i2][j2] *= 1-flash_tracker[(i2,j2)]
        if grid[i2][j2] > 9:
            flash_cell(grid,i2,j2,flash_tracker)
    return


if __name__ == "__main__":
    print(f"{part1(INPUT_TEST,100) = } | 1656")
    print(f"{part1(INPUT_REAL,100) = }")
    print(f"{part2(INPUT_TEST) = } | 195")
    print(f"{part2(INPUT_REAL) = }")