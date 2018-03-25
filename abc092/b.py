N = int(input())
D, X = list(map(int, input().split()))
A = [int(input()) for _ in range(N)]

print(sum([(D - 1) // n + 1 for n in A]) + X)
