import itertools
import sys


def solve(C):
    for cc, cn in itertools.combinations(C, 2):
        for c_c, c_n in itertools.combinations(zip(cc, cn), 2):
            if c_c[0] + c_n[1] != c_c[1] + c_n[0]:
                return "No"
    else:
        return "Yes"
        
if __name__ == "__main__":
    C = [list(map(int, input().split())) for _ in range(3)]
    print(solve(C))
