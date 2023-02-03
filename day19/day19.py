INPUT_TEST = r"input_test_day19.txt"
INPUT_REAL = r"input_real_day19.txt"

from collections import deque
from typing import Generator

class Queue(deque):
    def __init__(self,*a):
        super().__init__(a)
    def push(self, item):
        self.append(item)
    def pop(self):
        return self.popleft()
    def is_empty(self):
        return not self

def get_list_of_lists_of_threeples(fname: str = INPUT_TEST) -> list[list[tuple[str,str,str]]]:
    list_of_lists_of_threeples = []
    cube = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            elif line.startswith("---"):
                if cube:
                    list_of_lists_of_threeples.append(cube)
                    cube = []
            else:
                cube.append(tuple(int(e) for e in line.split(",")))
        list_of_lists_of_threeples.append(cube)
    return list_of_lists_of_threeples

def test_file_reader():
    list_of_lists_of_threeples = get_list_of_lists_of_threeples(INPUT_TEST)
    for e in list_of_lists_of_threeples:
        print(e)

def part1(fname: str = INPUT_TEST) -> int:
    cubes = get_list_of_lists_of_threeples(fname)
    cube0 = cubes[0]
    cubes_correct = [cube0]
    cubes_left = Queue(*cubes[1:])
    offsets = [(0,0,0)]
    # continuously go through cubes_left and try to fit to a member of cubes_correct
    # if a cube fits, add it to cubes_correct and remove it from cubes_left
    # if a cube does not fit, add it back to cubes_left and check against the next member of cubes_correct
    while cubes_left:
        loops = 0
        cube_candidate = cubes_left.pop()
        # print(f"{cube_candidate[0] = }")
        cube_fitted = None
        for cube_correct in cubes_correct:
            cube_fitted, offset = fit_cube(cube_candidate, cube_correct)
            if cube_fitted:
                cubes_correct.append(cube_fitted)
                print(f"{len(cubes_correct) = }  {len(cubes_left) = }")
                offsets.append(offset)
                loops = 0
                break
        if not cube_fitted:
            cubes_left.push(cube_candidate)
            loops += 1
            # print(f"failed:  {len(cubes_left) = }  {loops = }")
            if loops > len(cubes_left):
                raise ValueError(f"{len(cubes_left)} cubes were not fit")
    coordinates_set = set()
    for cube in cubes_correct:
        for coordinate in cube:
            coordinates_set.add(coordinate)
    biggest_offset = 0
    for x0,y0,z0 in offsets:
        for x1,y1,z1 in offsets:
            dx,dy,dz = x1-x0, y1-y0, z1-z0
            biggest_offset = max(biggest_offset, abs(dx) + abs(dy) + abs(dz))
    return len(coordinates_set), biggest_offset

def fit_cube(cube_candidate: list[tuple[int,int,int]], cube_correct: list[tuple[int,int,int]], overlap_criteria: int = 12) -> list[tuple[int,int,int]]:
    for x0,y0,z0 in cube_correct:
        for cube1 in get_cube_rotations(cube_candidate):
            for x1,y1,z1 in cube1:
                dx,dy,dz = x1-x0, y1-y0, z1-z0
                cube1_normalized = [(x-dx,y-dy,z-dz) for x,y,z in cube1]
                if len(set(cube_correct) & set(cube1_normalized)) >= overlap_criteria:
                    return cube1_normalized, (dx,dy,dz)
    return None, None

def get_cube_rotations(cube: list[tuple[int,int,int]]) -> Generator[list[tuple[int,int,int]],None,None]:
    # generator that yields all 24 orientations of the points in cube around the origin (0,0,0)
    # orientations do not include reflections
    # twist around x-axis
    for _ in range(4):
        cube = [(x,-z,y) for x,y,z in cube]
        # twist around y-axis
        for _ in range(4):
            cube = [(z,y,-x) for x,y,z in cube]
            yield cube
    # twist around z-axis
    for _ in range(4):
        cube = [(-y,x,z) for x,y,z in cube]
        if _%2 == 1: continue
        # twist around y-axis
        for _ in range(4):
            cube = [(z,y,-x) for x,y,z in cube]
            yield cube
    
def test_get_cube_rotations():
    cube = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    ix = 0
    for cube1 in get_cube_rotations(cube):
        ix += 1
        print(f"rotation-------- {ix}")
        for line in cube1:
            print(line)
        # print(cube1)
    
if __name__ == "__main__":
    # test_file_reader()
    print(f"{part1(INPUT_TEST) = } | 79, 3621")
    print(f"{part1(INPUT_REAL) = }")

    # test_get_cube_rotations()

    