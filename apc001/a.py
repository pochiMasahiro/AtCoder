import sys

x, y = list(map(abs, list(map(int, input().split()))))

if x == y or x % y == 0 or y % x == 0:
    print(-1)
else:
    for i in range(2, x if x > y else y):
        if (i * x) % y != 0:
            print(i*x)
            break
