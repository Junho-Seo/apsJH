# 1210 .[S/W 문제해결 기본] 2일차 - Ladder1

import sys
sys.stdin = open("input1210.txt", "r")
sys.stdout = open("output1210.txt", "w")

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 첫 번째 열에서 1이 들어있는 칸을 탐색 (좌측부터)
    # 2. 해당 칸에서 아래 방향으로 0이 나올때까지 탐색
    # 3. 0이 나올 경우 바로 전 칸에서 좌측 혹은 우측에 1이 있는 칸으로 0이 나올 때까지 탐색
    #   (첫 행에서는 좌측, 마지막 행에서는 우측으로는 진행 불가)
    # 4. 0을 만나면 다시 아래 방향으로 탐색
    # 5. 2~4 반복
    # 6. 2를 만나면 해당 인덱스 좌표 출력

