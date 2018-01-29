import sys
l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]

dat = []

#per_dis = [[ 0 for n in range(N+1)] for n in range(N+1)]

per_dis = [ [] for n in range(N+1)]

for n in range(M):
    x = list(map(int, input().split()))
    dat.append(x)

def bfs(start, goal):
    visited = []
    unvisited = [(start, 0)]
    while unvisited:
        now = unvisited[0]
        unvisited = unvisited[1:]
        for next in per_dis[now[0]]:
            if next[0] not in visited:
                if next[0] == goal:
                    return now[1] + next[1]
                unvisited.append((next[0], now[1] + next[1]))
                visited.append(next[0])
    return None

for x in dat:
    if None == bfs(x[0], x[1]):
        per_dis[x[0]].append((x[1],x[2]))
        per_dis[x[1]].append((x[0],-x[2]))
    elif  x[2] != bfs(x[0], x[1]):
        print("No")
        sys.exit(0)

print("Yes")
