from dataclasses import dataclass
import re
from collections import defaultdict

INPUT_TEST = r"input_test_day22.txt"
INPUT_TEST2 = r"input_test2_day22.txt"
INPUT_REAL = r"input_real_day22.txt"

@dataclass
class Cube:
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int
    state: bool

    def return_all_tuples_within_bounds(self, xmin: int = -50, xmax: int = 50, ymin: int = -50, 
                                        ymax: int = 50, zmin: int = -50, zmax: int = 50) -> list[tuple[int,int,int]]:
        tuples = []
        for x in range(max(self.x0,xmin), min(self.x1,xmax) + 1):
            for y in range(max(self.y0,ymin), min(self.y1,ymax) + 1):
                for z in range(max(self.z0,zmin), min(self.z1,zmax) + 1):
                    tuples.append((x,y,z))
        return tuples

    def __str__(self):
        return f"Cube(x0={self.x0},x1={self.x1},y0={self.y0},y1={self.y1},z0={self.z0},z1={self.z1},state={self.state})"

    def __repr__(self):
        return self.__str__()

    def intersection(self, other: 'Cube') -> 'Cube':
        """
        Returns the intersection of two cubes, or None if they do not intersect.
        """
        if self.x0<=other.x1 and self.x1>=other.x0 and self.y0<=other.y1 and self.y1>=other.y0 and self.z0<=other.z1 and self.z1>=other.z0:
            return Cube(max(self.x0,other.x0),min(self.x1,other.x1),max(self.y0,other.y0),min(self.y1,other.y1),max(self.z0,other.z0),min(self.z1,other.z1),True)
        else:
            return None

    def subtract(self, other: 'Cube') -> list['Cube']:
        """
        Returns a list of cubes that are the result of subtracting the other cube from this cube.
        If there is no intersection, returns a list containing this cube.
        """
        intersection = self.intersection(other)
        if not intersection:
            return [self]
        cubes = []
        if self.x0 < other.x0:
            cubes.append(Cube(self.x0, other.x0 - 1, self.y0, self.y1, self.z0, self.z1, self.state))
        if self.x1 > other.x1:
            cubes.append(Cube(other.x1 + 1, self.x1, self.y0, self.y1, self.z0, self.z1, self.state))
        if self.y0 < other.y0:
            cubes.append(Cube(max(other.x0,self.x0), min(other.x1,self.x1), self.y0, other.y0 - 1, self.z0, self.z1, self.state))
        if self.y1 > other.y1:
            cubes.append(Cube(max(other.x0,self.x0), min(other.x1,self.x1), other.y1 + 1, self.y1, self.z0, self.z1, self.state))
        if self.z0 < other.z0:
            cubes.append(Cube(max(other.x0,self.x0), min(other.x1,self.x1), max(other.y0,self.y0), min(other.y1,self.y1), self.z0, other.z0 - 1, self.state))
        if self.z1 > other.z1:
            cubes.append(Cube(max(other.x0,self.x0), min(other.x1,self.x1), max(other.y0,self.y0), min(other.y1,self.y1), other.z1 + 1, self.z1, self.state))
        return cubes

    def volume(self) -> int:
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

BOUNDS_RGX = r"x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"

def get_cubes_from_file(fname: str = INPUT_TEST) -> list[Cube]:
    cubes = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            state = line.split(" ")[0] == "on"
            bounds = re.findall(BOUNDS_RGX, line.split(" ")[1])[0]
            bounds = [int(b) for b in bounds]
            cubes.append(Cube(*bounds, state))
    return cubes

def part1(fname: str = INPUT_TEST) -> int:
    cubes = get_cubes_from_file(fname)
    coordinates_on = defaultdict(lambda: False)
    for cube in cubes:
        for coords in cube.return_all_tuples_within_bounds():
            coordinates_on[coords] = cube.state
    return len([coords for coords, state in coordinates_on.items() if state])

def part2(fname: str = INPUT_TEST2) -> int:
    cubes = get_cubes_from_file(fname)
    # cube1 = Cube(0, 1, 0, 1, 0, 1, True)
    # cube2 = Cube(1, 2, 1, 2, 1, 2, True)
    # cube3 = Cube(1, 1, 1, 1, 1, 1, False)
    # cubes = [cube1, cube2, cube3, cube3]
    new_cubes = []
    for cube in cubes:
        if not new_cubes:
            new_cubes.append(cube)
            continue
        collisions = []
        intersections = []
        for new_cube in new_cubes:
            intersection = cube.intersection(new_cube)
            if intersection:
                collisions.append(new_cube)
                intersections.append(intersection)
        if not collisions:
            new_cubes.append(cube)
            continue
        next_cubes = [cube]
        for collision, intersection in zip(collisions, intersections):
            new_cubes.remove(collision)
            if cube.state: 
                new_cubes.append(intersection)
            new_cubes.extend(collision.subtract(intersection))
            new_next_cubes = []
            for new_next_cube in next_cubes:
                new_next_cubes.extend(new_next_cube.subtract(intersection))
            next_cubes = new_next_cubes
        if cube.state:
            new_cubes.extend(next_cubes)
    volume = 0
    for cube in new_cubes:
        if cube.state:
            volume += cube.volume()
    return volume

def test_cube2():
    cube1 = Cube(0, 1, 0, 1, 0, 1, True)
    cube2 = Cube(1, 2, 1, 2, 1, 2, True)
    intersection = cube1.intersection(cube2)
    print(f"{intersection = }")
    print(f"{cube1.subtract(cube2) = }")
    print(f"{cube1.subtract(intersection) = }")
    print(f"{cube2.subtract(cube1) = }")
    print(f"{cube2.subtract(intersection) = }")


def test_file_reader():
    cubes = get_cubes_from_file(INPUT_TEST2)
    for c in cubes:
        print(c)


if __name__ == "__main__":
    # print(f"{part1(INPUT_TEST) = } | 590784")
    # print(f"{part1(INPUT_REAL) = }")
    # test_file_reader()
    print(f"{part2(INPUT_TEST2) = } | 2758514936282235") # 2758514936286494 | 2758514936282235
    # test_cube2()
    print(f"{part2(INPUT_REAL) = }")