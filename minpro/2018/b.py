import math
x, y = map(int, input().split())

for n in range(1,y+1):
    x -= x % int(math.pow(10,n))
else:
    x += int(math.pow(10, y))

print(x)

