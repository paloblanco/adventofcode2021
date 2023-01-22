INPUT_TEST = r"input_test_day12.txt"
INPUT_REAL = r"input_real_day12.txt"

from collections import defaultdict, Counter

def return_adjacency_dict_from_file(fname: str = INPUT_TEST) -> dict[str,str]:
    adjacency_dict = defaultdict(list)
    with open(fname) as f:
        for line in f:
            a,b = line.strip().split("-")
            adjacency_dict[a].append(b)
            adjacency_dict[b].append(a)
    return adjacency_dict

def part2(fname: str = INPUT_TEST) -> int:
    # start at "start" and find all paths to "end"
    # return the number of paths
    # a path may not touch a lower-case node more than twice
    # a path may not touch "start" or "end more than once each
    # a path may touch upper-case nodes any number of times
    adjacency_dict = return_adjacency_dict_from_file(fname)
    frontier = [["start"]]
    paths = 0
    while frontier:
        current_path = frontier.pop()
        node = current_path[-1]
        for neighbor in adjacency_dict[node]:
            if neighbor == "end":
                paths += 1
            elif neighbor == "start":
                continue
            elif neighbor.islower() and neighbor in current_path:
                if [e for e in Counter(current_path).most_common() if e[0].islower()][0][1] > 1:
                    continue
                else:
                    frontier.append(current_path + [neighbor])
            else:
                frontier.append(current_path + [neighbor])
    return paths

def part1(fname: str = INPUT_TEST) -> int:
    # start at "start" and find all paths to "end"
    # return the number of paths
    # a path may not touch a lower-case node more than once
    # a path may touch upper-case nodes any number of times
    adjacency_dict = return_adjacency_dict_from_file(fname)
    frontier = [["start"]]
    paths = 0
    while frontier:
        current_path = frontier.pop()
        node = current_path[-1]
        for neighbor in adjacency_dict[node]:
            if neighbor == "end":
                paths += 1
            elif neighbor == "start":
                continue
            elif neighbor.islower() and current_path.count(neighbor):
                continue
            else:
                frontier.append(current_path + [neighbor])
    return paths

if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 226")
    print(f"{part1(INPUT_REAL) = }")

    print(f"{part2(INPUT_TEST) = } | 3509")
    print(f"{part2(INPUT_REAL) = }")