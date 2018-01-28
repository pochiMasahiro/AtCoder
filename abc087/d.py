import sys
l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]

dat = []

per_dis = [[ 0 for n in range(N+1)] for n in range(N+1)]

for n in range(M):
    x = list(map(int, input().split()))
    dat.append(x)
    
for x in dat:
    if per_dis[x[0]][x[1]] == 0 and per_dis[x[0]][x[1]] == 0:
        per_dis[x[0]][x[1]] = x[2]
        per_dis[x[1]][x[0]] = -x[2]
        for i in range(1,N):
            for j in range(i+1,N):
                if per_dis[i][j] != 0 and per_dis[i+1][j+1] != 0 and per_dis[i][j+1] == 0:
                    per_dis[i][j+1] = per_dis[i][j] + per_dis[i+1][j+1]
                    per_dis[j+1][i] = -per_dis[i][j+1]
                elif per_dis[i][j] == 0 and per_dis[i+1][j+1] != 0 and per_dis[i][j+1] != 0:
                    per_dis[i][j] = per_dis[i][j+1] - per_dis[i+1][j+1]
                    per_dis[j][i] = -per_dis[i][j]
                elif per_dis[i][j] != 0 and per_dis[i+1][j+1] == 0 and per_dis[i][j+1] != 0:
                    per_dis[i+1][j+1] = per_dis[i][j+1] - per_dis[i][j]
                    per_dis[j+1][i+1] = -per_dis[i+1][j+1]
    else:
        if abs(per_dis[x[0]][x[1]]) != x[2]:
            print("No")
            sys.exit(0)


print("Yes")
