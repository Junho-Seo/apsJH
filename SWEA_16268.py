# 16268. 풍선팡2

import sys
sys.stdin = open('input16268.txt', 'r')
sys.stdout = open('output16268.txt', 'w')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1, 0, 1]
    dj = [0, 1, 0, -1, 0]
    max_cnt = 0

    for i in range(N):
        for j in range(M):
            temp = 0
            for k in range(5):
                new_i = i + di[k]
                new_j = j + di[k]
                # if 0 <= new_i < N and 0 <= new_j < M:
                if new_i < 0 or new_j < 0 or new_i >= N or new_j >= M:
                    continue
                temp += arr[new_i][new_j]
            if temp > max_cnt:
                max_cnt = temp

    print(f'#{test_case} {max_cnt}')

