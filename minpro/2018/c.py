import sys
import itertools
import math
import functools

N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))
V = list(map(int, input().split()))

wallet = 0
score = 0
buy_index = []
for _ in range(N):
    if len(buy_index) != 0:
        buy = max(V[buy_index])
        tmp1 = argmax(V[buy_index])
        tmp = V.index(buy)
        wallet -= C[tmp]
        score += V[tmp]
        buy_index.remove(tmp1)
    else:
        wallet += X.pop(0)
        buy_index = [ i for i ,_ in enumerate(C) if C[i] < wallet]
        block = functools.reduce(labmda x, y: C[x] if C[x] > C[y] else C[y], buy_index)
        blck_index = C.index(block)
        C.pop(block_index)
        V.pop(block_index)
        buy_index.remove(tmp)

print(score)
