import sys
l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]


per_dis = [ [] for n in range(N+1)]
people = [None] * (N+1)

for n in range(M):
    x = list(map(int, input().split()))
    per_dis[x[0]].append((x[1], x[2]))
    per_dis[x[1]].append((x[0], -x[2]))

if M != 0:
    visited = []
    unvisited = [(x[0], 0)]
    people[x[0]] = 0
    while unvisited:
        now = unvisited[0]
        unvisited = unvisited[1:]
        for next in per_dis[now[0]]:
            if next[0] not in visited:
                people[next[0]] =  now[1] + next[1]
                unvisited.append((next[0], now[1] + next[1]))
                visited.append(now[0])

for i, x in enumerate(per_dis):
    if x != None:
        for y in x:
            if y[1] < 0:
                if people[y[0]] - people[i] != y[1]:
                    print("No")
                    sys.exit()
            else:
                if people[i] - people[y[0]] != -y[1]:
                    print("No")
                    sys.exit()


print("Yes")
                
