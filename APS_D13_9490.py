# 9490. 풍선팡

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 행, 열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 풍선별 꽃가루 수

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 선택한 위치에서의 꽃가루 개수
            for k in range(4):      # 델타 방향 순회
                for l in range(1, arr[i][j]+1):  # 주변 방향으로 추가로 터지는 풍선과의 거리
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')