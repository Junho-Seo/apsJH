# 4615. 재미있는 오셀로 게임


def f(i, j, color, N):
    board[i][j] = color     # 지정된 돌 놓기
    for di, dj in [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]:
        ni, nj = i + di, j + dj
        tmp = []  # 뒤집을 돌의 인덱스를 저장
        while 0<=ni<N and 0<=nj<N and board[ni][nj] == op[color]:  #반대 색 돌이면
            tmp.append((ni, nj))  # 뒤집을 돌을 저장하고
            ni, nj = ni + di, nj + dj  # 현재 방향으로 계속 이동
        if 0<=ni<N and 0<=nj<N and board[ni][nj] == color:
            for p, q in tmp:
                board[p][q] = color


# 흑돌1 백돌2
B = 1
W = 2
op = [0, 2, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N 보드 크기, M 놓는 횟수
    play = [list(map(int, input().split()))for _ in range(M)]

    board = [[0]*N for _ in range(N)]# 보드 준비, 0 -> N-1 인덱스 사용
    # 중심부 돌 배치 (고정값)
    board[N//2 - 1][N//2 - 1] = W
    board[N//2 - 1][N//2] = B
    board[N//2][N//2 - 1] = B
    board[N//2][N//2] = W

    # 돌 놓기
    for col, row, color in play:  # 입력 순서 주의. col, row는 1부터 시작, board는 0부터 시작
        f(row-1, col-1, color, N)

    bcnt = wcnt = 0  # 검은 돌 개수, 흰돌 개수
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')  # 흑돌 백돌의 개수를 출력
