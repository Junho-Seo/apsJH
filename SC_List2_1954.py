# 1954. 달팽이 숫자
# im 기출
# 델타탐색의 응용
# 우측>하단>좌측>상단>...
# + 방문 체크(중복되지 않도록)
'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

# 강사님 풀이
# while문 4개? 구현 난이도 올라감.

# 현재 시점으로 어디부터 탐색할 것인가(델타배열 작성)
# 우 > 하 > 좌 > 상 >... (가운데 필요없음)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 숫자가 들어있는 곳은 다시 못 가도록
    # 방문 체크를 위한 빈 배열 작성
    snails = [([0] * N) for _ in range(N)]

    # 시작점(좌표, 진행 방향), 반복 조건(1~N*N) => 설계에서 가장 중요
    # 0, 0좌표 / dir: 시작 방향 (우측 = 0)
    y, x, dir = 0, 0, 0
    for i in range(1, N*N + 1):
        snails[y][x] = i
        # 다음 좌표 체크용
        new_y = y + dy[dir]
        new_x = x + dx[dir]

        # 범위를 넘어가거나, 이미 방문한 곳이라면
        # 방향을 변환
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N or snails[new_y][new_x]:
            # 4로 나누어 0 1 2 3을 반복하도록 한다.
            dir = (dir + 1) % 4

        y = y + dy[dir]
        x = x + dx[dir]

    print(f'#{test_case}')
    for i in range(N):
        print(*snails[i])










# 내 풀이
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # NxN 크기의 배열
    snail = [([0] * N) for _ in range(N)]
    print(snail)

    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            for k in range(5):
                new_i = i + di[k]
                new_j = j + dj[k]
                if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                    continue
                if j < N:
                    snail[i][j] = 1 + j
                    j += 1
                if j == N:
                    snail[j][i] = 2 + j
                    i += 1
    print(snail)
