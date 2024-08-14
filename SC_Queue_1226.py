# 1226. [S/W 문제해결 기본] 7일차 - 미로1
# 1. DFS -> 재귀 + 델타탐색
# 2. DFS -> 스택 + 델타탐색
# 3. BFS -> 큐 + 델타탐색
# 문법 관련 gpt아카이브 확인
"""
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).

"""


import sys
sys.stdin = open("input1226.txt", "r")
sys.stdout = open("output1226.txt", "w")

# # 백터 탐색 (우 하 좌 상)
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# def dfs_rec(y, x):
#     global result
#     # 종료 조건
#     if y == 13 and x == 13:     # 도착점 (13,13)
#         result = 1
#         return
#     # 탐색
#     for i in range(4):
#         newi = y + di[i]
#         newj = x + dj[i]
#
#         # 미로 범위 밖이거나, 벽이거나, 방문 한 곳은 continue
#         if newi < 0 or newi >= 16 or newj < 0 or newj >= 16 or maze[newi][newj] == 1 or visited[newi][newj]:
#             continue
#
#         visited[newi][newj] = 1  # 방문 처리
#         dfs_rec(newi, newj)  # 다음 좌표 탐색
#
#
# for _ in range(1, 11):
#     tc = int(input())
#     maze = [list(map(int, input()))for _ in range(16)]
#     visited = [[0]*16 for _ in range(16)]  # 방문 기록용 배열
#     visited[1][1] = 1  # 시작점 방문 처리 (1,1)
#
#     result = 0
#     dfs_rec(1, 1)
#     print(f'#{tc} {result}')

# ===================
# 스택 dfs
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs_stack(y, x):
    global result
    stack = [(y, x)]
    visited = [[0] * 16 for _ in range(16)]
    visited[y][x] = 1  # 시작점 방문 처리

    while stack:
        now_y, now_x = stack.pop()

        # 종료 조건
        if now_y == 13 and now_x == 13:  # 도착점 (13,13)
            result = 1
            return

        # 4방향 탐색
        for i in range(4):
            newi = now_y + di[i]
            newj = now_x + dj[i]

            # 미로 범위 밖이거나, 벽이거나, 방문한 곳은 continue
            if newi < 0 or newi >= 16 or newj < 0 or newj >= 16 or maze[newi][newj] == 1 or visited[newi][newj]:
                continue

            visited[newi][newj] = 1  # 방문 처리
            stack.append((newi, newj))  # 스택에 다음 좌표 추가


for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0
    dfs_stack(1, 1)
    print(f'#{tc} {result}')

# ============================
# 큐 BFS (swea 런타임에러)
# from collections import deque
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# def bfs_queue(y, x):
#     global result
#     q = deque([(y, x)])
#     visited = [[0] * 16 for _ in range(16)]
#     visited[y][x] = 1  # 시작점 방문 처리
#
#     while q:
#         qy, qx = q.popleft()
#
#         # 종료 조건
#         if qy == 13 and qx == 13:  # 도착점 (13,13)
#             result = 1
#             return
#
#         # 4방향 탐색
#         for i in range(4):
#             newi = qy + di[i]
#             newj = qx + dj[i]
#
#             # 미로 범위 밖이거나, 벽이거나, 방문한 곳은 continue
#             if newi < 0 or newi >= 16 or newj < 0 or newj >= 16 or maze[newi][newj] == 1 or visited[newi][newj]:
#                 continue
#
#             visited[newi][newj] = 1  # 방문 처리
#             q.append((newi, newj))  # 큐에 다음 좌표 추가
#
#
# for _ in range(1, 11):
#     tc = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     result = 0
#     bfs_queue(1, 1)
#     print(f'#{tc} {result}')
