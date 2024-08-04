# 1210 .[S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open("input1210.txt", "r")
sys.stdout = open("output1210.txt", "w")

for _ in range(10):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # # 도착점 좌표 탐색
    # end_point = 0
    # for j in range(100):
    #     if ladder[99][j] == 2:
    #         end_point = j       # 도착점은 (j, 99)

    # 방향 설정 (좌 우 위)
    di = [0, 0, -1]
    dj = [-1, 1, 0]
    # 시작 인덱스 설정. 도착점부터 위로 진행
    new_i = 99
    new_j = ladder[99].index(2)

    while new_i != 0:       # 0 번째 행에 올 때까지 반복
        for k in range(3):
            ni = new_i + di[k]
            nj = new_j + dj[k]
            # 사다리 범위를 벗어나면 통과
            if ni < 0 or nj < 0 or ni >= 100 or nj >= 100:
                continue
            if ladder[ni][nj] == 1:
                ladder[new_i][new_j] = 0        # 지나온 좌표는 다시 가지 않도록 0 할당
                new_i = ni
                new_j = nj
                break

    print(f'#{test_case} {new_j}')
    # for k in range(99 , 0, -1):
    #     if end_point


    # 출발점을 찾기 위해 도착점부터 거꾸로 올라간다.
    # 1을탐색하며 올라가고 좌우 탐색이 상단 탐색보다 우선된다.

# # 석주
# for _ in range(10):
#     test_case = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     col = ladder[99].index(2);
#     row = 99
#
#     while row != 0:
#         if col > 0 and ladder[row][col - 1] == 1:
#             while col > 0 and ladder[row][col - 1] == 1:
#                 col -= 1
#         elif col < 99 and ladder[row][col + 1] == 1:
#             while col < 99 and ladder[row][col + 1] == 1:
#                 col += 1
#         row -= 1
#
#     print(f'#{test_case} {col}')
#
# # 고운
# for i in range(1, 11):
#     test_case = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#
#     di = [0, 0, 1]
#     dj = [1, -1, 0]
#
#     for j in range(100):
#         visited = [[False] * 100 for _ in range(100)]
#         if ladder[0][j] == 1:
#
#             x, y = 1, j
#             while x < 99:
#                 visited[x][y] = True
#
#                 for dx, dy in zip(di, dj):
#                     nx, ny = dx + x, dy + y
#                     if -1 < nx < 100 and -1 < ny < 100 and ladder[nx][ny] != 0 and not visited[nx][ny]:
#                         x, y = nx, ny
#                         break
#
#             if ladder[x][y] == 2:
#                 print(f"#{test_case} {j}")