INPUT_TEST = r"input_test_day14.txt"
INPUT_REAL = r"input_real_day14.txt"

from collections import Counter, defaultdict

def return_starter_and_template_from_file(fname: str = INPUT_TEST) -> tuple[str,dict[str,str]]:
    template = {}
    with open(fname) as f:
        line = next(f).strip()
        starter = line
        next(f)
        for line in f:
            a,b = line.strip().split(" -> ")
            template[a] = b
    return starter, template

def part1(fname: str = INPUT_TEST, steps: int = 10) -> int:
    polymer, template = return_starter_and_template_from_file(fname)
    # for each step, insert new characters into polymer according to template
    # at the end, count the occurence of each letter in polymer
    # return the frequency of the most common letter minus the frequency of the least common letter
    for _ in range(steps):
        new_polymer = ""
        for i in range(len(polymer)-1):
            new_polymer += polymer[i]
            new_polymer += template.get(polymer[i:i+2],"")
        new_polymer += polymer[-1]
        polymer = new_polymer
    # print(polymer)
    return Counter(polymer).most_common()[0][1] - Counter(polymer).most_common()[-1][1]

def part2(fname: str = INPUT_TEST, steps: int = 40) -> int:
    polymer, template = return_starter_and_template_from_file(fname)
    polymer_pairs = Counter([polymer[i:i+2] for i in range(len(polymer)-1)])
    # for each step, insert new characters into polymer according to template
    # at the end, count the occurence of each letter in polymer
    # return the frequency of the most common letter minus the frequency of the least common letter
    print(polymer_pairs)
    for _ in range(steps):
        new_polymer_pairs = defaultdict(int, polymer_pairs)
        for pair, count in polymer_pairs.items():
            if pair in template:
                newletter = template[pair]
                newleft = pair[0] + newletter
                newright = newletter + pair[1]
                new_polymer_pairs[newleft] += count
                new_polymer_pairs[newright] += count
                new_polymer_pairs[pair] -= count
        polymer_pairs = new_polymer_pairs
    monomer_counter = defaultdict(int)
    for pair, count in polymer_pairs.items():
        monomer_counter[pair[0]] += count
        monomer_counter[pair[1]] += count
    monomer_counter = {k:v//2 for k,v in monomer_counter.items()}
    monomer_counter[polymer[0]] += 1
    monomer_counter[polymer[-1]] += 1
    monomer_counter = Counter(monomer_counter)
    return monomer_counter.most_common()[0][1] - monomer_counter.most_common()[-1][1]

    

def print_starter_and_template(starter: str, template: dict[str,str]) -> None:
    print("starter:", starter)
    print("template:")
    for k,v in template.items():
        print(k,":",v)

def test_reader() -> None:
    starter, template = return_starter_and_template_from_file(INPUT_TEST)
    print_starter_and_template(starter, template)


if __name__ == "__main__":
    # test_reader()
    print(f"{part1(INPUT_TEST, 10) = } | 1588")
    print(f"{part1(INPUT_REAL, 10) = }")

    print(f"{part2(INPUT_TEST, 40) = } | 2188189693529")
    print(f"{part2(INPUT_REAL, 40) = }")