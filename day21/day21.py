INPUT_REAL = (6,8)
INPUT_TEST = (4,8)

from random import randint
from collections import defaultdict, Counter, deque
from itertools import product

class Die:
    def __init__(self, sides: int = 100):
        self.sides = sides
        self.value = 100
        self.rolls = 0
    
    def roll(self) -> int:
        self.value += 1
        if self.value > 100:
            self.value = 1
        self.rolls += 1
        return self.value

def part1(starts: tuple[int,int] = INPUT_TEST) -> int:
    p1,p2 = starts[0]-1, starts[1]-1
    s1,s2 = 0,0
    die = Die()
    # print(f"{p1 = } | {p2 = } | {s1 = } | {s2 = } | {die.rolls = }")
    while s1 < 1000 and s2 < 1000:
        move1 = sum([die.roll() for _ in range(3)])
        p1 = (p1 + move1) % 10
        s1 += p1+1
        if s1 >= 1000:
            break
        move2 = sum([die.roll() for _ in range(3)])
        p2 = (p2 + move2) % 10
        s2 += p2+1
        # print(f"{p1 = } | {p2 = } | {s1 = } | {s2 = } | {die.rolls = }")
    return min(s1,s2) * die.rolls


def part2(starts: tuple[int,int] = INPUT_TEST) -> int:
    p1,p2 = starts[0]-1, starts[1]-1
    s1,s2 = 0,0
    p1state = (p1,s1,0) # position, score, turns
    p2state = (p2,s2,0)
    p1_states_all: defaultdict[tuple[int,int,int],int] = get_all_states(p1state, points=21)
    print(f"{len(p1_states_all) = }")
    # for k,v in p1_states_all.items():
        # print(f"{k = } | {v = }")
    p2_states_all: defaultdict[tuple[int,int,int],int] = get_all_states(p2state, points=21)
    p1wins=0
    p2wins=0
    for (p1,s1,t1),p1_counts in p1_states_all.items():
        for (p2,s2,t2),p2_counts in p2_states_all.items():
            if t2 == t1-1 and s1 >= 21 and s2 < 21:
                p1wins += p1_counts * p2_counts
            elif t1 == t2 and s1 < 21 and s2 >= 21:
                p2wins += p1_counts * p2_counts
    return p1wins, p2wins

def get_all_states(state: tuple[int,int,int], points: int = 21) -> defaultdict[tuple[int,int,int],int]:
    all_states: defaultdict[tuple[int,int,int],int] = defaultdict(int)
    moves = Counter([sum(e) for e in list(product([1,2,3],repeat=3))])
    moves = [(k,v) for k,v in moves.items()]
    all_states[state] = 1
    states_frontier = deque([state])
    while states_frontier:
        state = states_frontier.popleft()  # position, score, turns
        moves_current = all_states[state]
        p,s,t = state
        for move,move_count in moves:
            p_new = (p + move) % 10
            s_new = s + p_new + 1
            t_new = t + 1
            all_states[(p_new,s_new,t_new)] += moves_current * move_count
            if s_new < points and (p_new,s_new,t_new) not in states_frontier:
                states_frontier.append((p_new,s_new,t_new))
        # all_states.pop(state)
    return all_states

        



if __name__ == "__main__":
    print(f"{part1(INPUT_TEST) = } | 739785")
    print(f"{part1(INPUT_REAL) = }")

    print()

    print(f"{part2(INPUT_TEST) = } | 444356092776315")
    print(f"{part2(INPUT_REAL) = }")

        

