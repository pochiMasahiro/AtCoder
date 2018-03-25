import itertools as it

N = int(input())
A = [0] + list(map(int, input().split())) + [0]

L = 0
for i in range(N+1):
    L += abs(A[i+1] - A[i])
    
for i in range(1,N+1):
    print(L - (abs(A[i] - A[i-1]) + abs(A[i+1] - A[i])) + abs(A[i+1] - A[i-1]))
