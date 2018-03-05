from itertools import combinations
from functools import reduce
from operator import mul

N = int(input())
S_row = [input() for _ in range(N)]

count = [0] * 5
for i, c in enumerate("MARCH"):
    count[i] = len(list(filter(lambda n: n[0] == c, S_row)))

print(sum(map(lambda x: reduce(mul, x), combinations(count, 3))))
