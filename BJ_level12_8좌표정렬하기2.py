N = int(input())
ordered = []

for _ in range(N):
    x, y = map(int, input().split())
    ordered.append([x, y])

ordered.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(*ordered[i])
