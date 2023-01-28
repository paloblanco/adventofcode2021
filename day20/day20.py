INPUT_TEST = r"input_test_day20.txt"
INPUT_REAL = r"input_real_day20.txt"

from collections import defaultdict
from itertools import product

def get_algorithm_and_image_from_file(fname: str = INPUT_TEST) -> tuple[str,str]:
    with open(fname) as f:
        algorithm = list(next(f).strip())
        next(f)
        image = defaultdict(int)
        y = 0
        for line in f:
            line = list(line.strip())
            for x,char in enumerate(line):
                if char == "#":
                    image[(x,y)] = 1
            y += 1
    return algorithm, image

def test_file_reader():
    algorithm, image = get_algorithm_and_image_from_file(INPUT_TEST)
    print(f"{algorithm = }")
    print(f"{image = }")

def print_image(image: dict[tuple[int,int],int]):
    xmin = min(x for x,y in image.keys())
    xmax = max(x for x,y in image.keys())
    ymin = min(y for x,y in image.keys())
    ymax = max(y for x,y in image.keys())
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            char = "." if image[(x,y)] == 0 else "#"
            print(char,end="")
        print()
    print()

def part1(fname: str = INPUT_TEST, enhancement_count: int = 2) -> int:
    algorithm, image = get_algorithm_and_image_from_file(fname)
    bulk = 0 # color of pixels that are beyond the edge of the image
    # for each enhancement, apply the algorithm to the image
    # return the total number of pixels that are on, defined as the sum of 1s in image values
    # print_image(image)
    for _ in range(enhancement_count):
        image = enhance_image(algorithm,image)
        if algorithm[0] == "#":
            bulk = 1- bulk
        image = defaultdict(lambda: bulk,image)
        # print_image(image)
    return sum(image.values())

def enhance_image(algorithm: list[str], image: dict[tuple[int,int],int]) -> dict[tuple[int,int],int]:
    image_new = defaultdict(int)
    # for each pixel in image, apply the algorithm to it
    xmin = min(x for x,y in image.keys())-1
    xmax = max(x for x,y in image.keys())+1
    ymin = min(y for x,y in image.keys())-1
    ymax = max(y for x,y in image.keys())+1
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            # apply algorithm to pixel
            image_new[(x,y)] = apply_algorithm_to_pixel(algorithm,image,(x,y))
    return image_new

def apply_algorithm_to_pixel(algorithm: list[str], image: dict[tuple[int,int],int], pixel: tuple[int,int]) -> int:
    x,y = pixel
    image_indices = []
    for yy in range(-1,2):
        for xx in range(-1,2):
            image_indices.append((x+xx,y+yy))
    # image_indices = [(x+xx,y+yy) for yy,xx in product([-1,0,1],[-1,0,1])]
    index_bin = ''.join([str(image[(xx,yy)]) for xx,yy in image_indices])
    index = int(index_bin,2)
    return 1 if algorithm[index] == "#" else 0


if __name__ == "__main__":
    # test_file_reader()
    print(f"{part1(INPUT_TEST,2) = } | 35")
    print(f"{part1(INPUT_REAL,2) = }") # 5860 too high

    print()
    print("PART 2")
    print(f"{part1(INPUT_TEST,50) = } | 3351")
    print(f"{part1(INPUT_REAL,50) = }") # 5860 too high