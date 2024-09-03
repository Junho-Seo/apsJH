# N Queen 문제 접근법
# 이전에 놨던 위치를 모두 저장 -> visited

# 현재 row, col 위치에 놓을 수 있는지 확인하는 함수
def check(row, col):    # i, j로 쓰면 해석이 어렵다. 참고.
    # 1. 세로줄에 존재하는 queen이 있는가
    for i in range(row):
        if visited[i][col]:     # 같은 세로줄에 둔 적이 있다면 False
            return False

    # 2. 좌측 대각선
    # zip을 활용한 for문 코드
    # for i,j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False
    i, j = row -1, col -1
    while i >= 0 and j >= 0:    # 대각선으로 한 칸씩 내려오며 확인
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 3. 우측 대각선
    i, j = row - 1, col + 1
    while i >= 0 and j < N:  # 대각선으로 한 칸씩 내려오며 확인
        if visited[i][j]:
            return False
        i -= 1
        j += 1
    # 모두 통과했다면 True 반환
    return True

def dfs(row):
    global cnt
    # 기저조건
    # 모든 줄을 다 고려했다면 return
    if row == N:
        cnt += 1
        return
    # 후보군
    for col in range(N):    #어느 세로열에 둘 것인가
        # col 자리에서 확인해야할 것 (def check)
        # 1. 세로줄에 존재하는 queen이 있는가
        # 2. 좌측 대각선
        # 3. 우측 대각선

        # 모두 통과하면 현재 col에 놓고 다음 row로 이동
        if check(row, col):
            visited[row][col] = 1
            dfs(row + 1)
            visited[row][col] = 0  # 초기화 필수!
        # continue 사용한 코드
        # if check(row, col) is False:
        #     continue
        # visited[row][col] = 1
        # dfs(row + 1)
        # visited[row][col] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    cnt = 0     # 가능한 수

    dfs(0)
    print(f'#{tc} {cnt}')