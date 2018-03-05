from itertools import chain

H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
exam = [list(map(int, input().split())) for _ in range(Q)]

x_a = [0] * (H*W)
y_a = [0] * (H*W)

for i, ax in enumerate(A):
    for j, ay in enumerate(ax):
        x_a[ay-1] = i
        y_a[ay-1] = j

S = [0] * (H*W)
for i in reversed(range(H*W-D)):
    S[i] = abs(x_a[i] - x_a[i+D]) + abs(y_a[i] - y_a[i+D]) + S[i + D]

for L, R in exam:
    print(S[L-1] - S[R-1])

