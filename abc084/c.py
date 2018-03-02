N = int(input())
stations = [ list(map(int, input().split())) for _ in range(N-1)]

time = [0] * N


for i, station in enumerate(stations):
    C, S, F = station
    for j in range(i + 1):
        if S > time[j]:
            time[j] = S + C
        elif time[j] % F == 0:
            time[j] += C
        else:
            time[j] += F - (time[j] % F) + C

[ print(t) for t in time ]
