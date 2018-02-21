from collections import deque

def bfs(x, graph, people):
    if people[x] is not None:
        return
    unvisited = deque([x])
    people[x] = 0
    while unvisited:
        now = unvisited.popleft()
        for next, d in graph[now]:
            if people[next] is None:
                people[next] =  people[now] + d
                unvisited.append(next)

def main():
    N, M = list(map(int, input().split()))

    graph = [ [] for n in range(N+1)]
    people = [None] * (N+1)

    for n in range(M):
        L, R, D = list(map(int, input().split()))
        graph[L].append((R, D))
        graph[R].append((L, -D))
    for i in range(1, N+1):
        bfs(i, graph, people)

    for i in range(1, N+1):
        for j, d in graph[i]:
            if people[j] - people[i] != d:
                print("No")
                exit()
    else:
        print("Yes")


if __name__ == "__main__":
    main()
