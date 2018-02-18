import sys
import functools
import itertools
import math

N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = sum(a for a in A[::2]) - sum(a for a in A[1::2])

print(ans)


