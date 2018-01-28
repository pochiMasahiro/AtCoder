N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

result = []

for n in range(N):
    a1 = sum(A1[:n+1])
    a2 = sum(A2[n:])
    result.append(a1+a2)

print(max(result))
