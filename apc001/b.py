import sys

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

print(A)
print(B)
for x in zip(A,B):
    if (x[1]-x[0]) < 0:
        print("No")
        break
else:
    print("Yes")
