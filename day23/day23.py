

INPUT_TEST = r"input_test_day23.txt"
INPUT_REAL = r"input_real_day23.txt"

#input is: "LL,lm,m,rm,RR,AA,BB,CC,DD"
INPUT_STR_REAL =    ".......DBCCADBA"
INPUT_STR_TEST =    ".......BACDBCDA"
GOAL =              ".......AABBCCDD"

SCORING = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

EDGES = {
    ("A","B"): 4,
    ("A","C"): 6,
    ("A","D"): 8,
    ("A","left"): 2,
    ("A","right"): 8,
    ("A","lmid"): 2,
    ("A","rmid"): 6,
    ("A","mid"): 4,
    ("B","C"): 4,
    ("B","D"): 6,
    ("B","left"): 4,
    ("B","right"): 6,
    ("B","lmid"): 2,
    ("B","rmid"): 4,
    ("B","mid"): 2,
    ("C","D"): 4,
    ("C","left"): 6,
    ("C","right"): 4,
    ("C","lmid"): 4,
    ("C","rmid"): 2,
    ("C","mid"): 2,
    ("D","left"): 8,
    ("D","right"): 2,
    ("D","lmid"): 6,
    ("D","rmid"): 4,
    ("D","mid"): 2,
}

EDGES.update({(v,k):EDGES[(k,v)] for k,v in EDGES.keys()})

class State:

    def __init__(self, map: str):
        self.map = map
        self.fill_stacks()
        self.stacks = {
            "A": [],
            "B": [],
            "C": [],
            "D": [],
            "left": [],
            "right": [],
            "lmid": [],
            "rmid": [],
            "mid": [],
        }
    
    def fill_stacks(self):
        self.stacks = {
            "A": [],
            "B": [],
            "C": [],
            "D": [],
            "left": [],
            "right": [],
            "lmid": [],
            "rmid": [],
            "mid": [],
        }
        for i,char in enumerate(self.map):
            if char == ".":
                continue
            if i in [0,1]:
                self.stacks["left"].append(char)
            elif i == 2:
                self.stacks["lmid"].append(char)
            elif i == 3:
                self.stacks["mid"].append(char)
            elif i == 4:
                self.stacks["rmid"].append(char)
            elif i in [5,6]:
                self.stacks["right"].append(char)
            elif i in [7,8]:
                self.stacks["A"].append(char)
            elif i in [9,10]:
                self.stacks["B"].append(char)
            elif i in [11,12]:
                self.stacks["C"].append(char)
            elif i in [13,14]:
                self.stacks["D"].append(char)
        

def get_map_from_file(fname: str = INPUT_TEST) -> tuple[int,int,int,int,int,int,int,int]:
    """
    Returns a tuple of 16 ints, representing the 8 letters positions as x,y
    """
    with open(fname) as f:
        return f.read()

def part1(startmap: str = INPUT_STR_TEST) -> int:
    state = State(startmap)


def test_get_map_from_file(fname=INPUT_TEST):
    print(f"{get_map_from_file(fname) = }")
    return get_map_from_file(fname)

if __name__ == "__main__":
    m = test_get_map_from_file()
    print(m)