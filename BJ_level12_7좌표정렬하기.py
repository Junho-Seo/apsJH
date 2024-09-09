N = int(input())
ordered = []

for _ in range(N):
    x, y = map(int, input().split())
    ordered.append([x, y])

ordered.sort()

for i in range(N):
    print(*ordered[i])