INPUT_TEST = r"input_test_day13.txt"
INPUT_REAL = r"input_real_day13.txt"

def return_set_of_tuples_from_file(fname: str = INPUT_TEST) -> set[tuple[int,int]]:
    coordinates = set()
    folds = []
    with open(fname) as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            elif line.startswith("fold"):
                entry = line.split(" ")[-1].split("=")
                folds.append((entry[0],int(entry[1])))
            else:
                coordinates.add(tuple((int(e) for e in line.split(","))))
    return coordinates, folds

def print_file_reader(fname: str = INPUT_TEST) -> None:
    coordinates, folds = return_set_of_tuples_from_file(fname)
    print(coordinates)
    print(folds)

def print_fold_coordinates(coordinates: set[tuple[int,int]]) -> None:
    maxx = max(coordinates, key=lambda x: x[0])[0]
    maxy = max(coordinates, key=lambda x: x[1])[1]
    template = [["." for _ in range(maxx+1)] for _ in range(maxy+1)]
    for x,y in coordinates:
        template[y][x] = "#"
    for row in template:
        print("".join(row))

def part1(fname: str = INPUT_TEST) -> int:
    # fold the coordinates according to the folds
    # only execute the first fold
    # return the number of coordinates that are left
    coordinates, folds = return_set_of_tuples_from_file(fname)
    fold = folds[0]
    coordinates = fold_coordinates(coordinates, fold)
    # print_fold_coordinates(coordinates)
    return len(coordinates)

def part2(fname: str = INPUT_TEST) -> int:
    # fold the coordinates according to the folds
    # execute all folds
    # return the number of coordinates that are left
    coordinates, folds = return_set_of_tuples_from_file(fname)
    for fold in folds:
        coordinates = fold_coordinates(coordinates, fold)
    print_fold_coordinates(coordinates)
    return len(coordinates)

def fold_coordinates(coordinates: set[tuple[int,int]], fold: tuple[str,int]) -> set[tuple[int,int]]:
    # fold the coordinates according to the fold
    # return the new coordinates
    new_coordinates = set()
    axis, fold_location = fold
    for x,y in coordinates:
        if axis == "x":
            xadd = 0
            if x > fold_location:
                xadd = fold_location - x
            new_coordinates.add((x + 2*xadd,y))
        else:
            yadd = 0
            if y > fold_location:
                yadd = fold_location - y
            new_coordinates.add((x,y + 2*yadd))
    return new_coordinates

if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 17")
    print(f"{part1(INPUT_REAL) = }") # 763 correct
    print("")
    print(f"{part2(INPUT_TEST) = }")
    print(f"{part2(INPUT_REAL) = }")

