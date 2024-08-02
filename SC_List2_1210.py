# 1210 .[S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open("input1210.txt", "r")
sys.stdout = open("output1210.txt", "w")

for _ in range(10):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 좌표 탐색
    end_point = 0
    for j in range(100):
        if ladder[99][j] == 2:
            end_point = j       # 도착점은 (j, 99)

    # 방향 설정 (좌 위 우)
    di = [0, -1, 0]
    dj = [1, 0, -1]
    # 시작 인덱스 설정
    new_i = 99
    new_j = end_point
    while new_i != 0:   # column 이 1이 아니면 끝
        for k in range(3):
            if ladder[new_i+di[k]][new_j+dj[k]] == 1:
                ladder[new_i][new_j] = 2
                new_i += di[k]
                new_j += dj[k]
                break
    # 범위를 벗어나면 끝남 (예외처리)
        if new_i < 0 or new_j < 0 or new_i >= 100 or new_j >= 100:
            break
    print(f'#{test_case} {new_j - 1}')
    # for k in range(99 , 0, -1):
    #     if end_point


    # 출발점을 찾기 위해 도착점부터 거꾸로 올라간다.
    # 1을탐색하며 올라가고 좌우 탐색이 상단 탐색보다 우선된다.


