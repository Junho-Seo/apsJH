# 교안 연습문제 1-2

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0
for i in range(N):
    for j in range(N):      # NxN 배열의 모든 원소에 대해
        s = 0               # 문제에서 원소와 주변 인접 원소의 차의 절대값의 합
        # i, j 원소의 4방향 원소에 대해
        for k in range(4):
            ni = i + di[k]
            nj = i + dj[k]
            if 0 <= ni < N and 0 <= nj < N:     # 실존하는 인접 원소 ni, nj
                # abs(arr[i][j] - arr[ni][nj])
                s += arr[i][j] - arr[ni][nj]
        total += s
print(total)