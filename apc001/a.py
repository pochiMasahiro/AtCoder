import sys

x, y = list(map(abs, list(map(int, input().split()))))

if x == y or x % y == 0 or y % x == 0:
    print(-1)
else:
    print(x)
