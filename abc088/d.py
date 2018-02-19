from collections import deque

def bfs(H, W, S):
    visited = [[False]*(W+2) for _ in range(H+2)]
    visited[1][1] = True
    unvisited = deque([(1,1)])
    dist = 1
    while unvisited:
        dist += 1
        un = deque()
        for x, y in unvisited:
            for t1, t2 in zip([-1,+1,0,0],[0,0,-1,1]):
                dx = x + t1
                dy = y + t2
                if S[dy][dx] != '#' and not visited[dy][dx]:
                    if dy == H and dx == W:
                        return dist
                    un.append((dx,dy))
                    visited[dy][dx] = True
        unvisited = un

    return -1

def main():
    H, W = map(int, input().split())
    S = ['#'+input()+'#' for _ in range(H)]
    S.insert(0,'#'*(W+2))
    S.append('#'*(W+2))
    step = bfs(H,W,S)
    white = sum([n.count('.') for n in S])
    if step == -1:
        print(step)
    else:
        print(white - step)

if __name__ == "__main__":
    main()
