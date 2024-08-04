# 18575. 풍선팡 보너스 게임

import sys
sys.stdin = open('input18575.txt', 'r')
sys.stdout = open('output18575.txt', 'w')

T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     final_score = 0
#
#     total = 0
#     for i in range(N):
#         for j in range(N):
#             temp = 0
#             total += arr[i][j]
#         print(total)
#
#         T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 받아오기
    counts = [[0] * N for _ in range(N)]  # 카운트 배열 생성

    for i in range(N):
        for j in range(N):
            # 행 저장
            counts[i][j] = sum(arr[i])

            # 열 저장
            for k in range(N):
                counts[i][j] += arr[k][j]

            # 중복값 (중앙) 제거
            counts[i][j] -= arr[i][j]

    # 최대, 최솟값 구하기
    max_cnt = counts[i][j]
    min_cnt = counts[i][j]
    for i in range(N):
        for j in range(N):
            if max_cnt < counts[i][j]:
                max_cnt = counts[i][j]
            elif min_cnt > counts[i][j]:
                min_cnt = counts[i][j]
    print(f'#{tc} {max_cnt - min_cnt}')


# 다른 풀이
T = int(input())  # 테스트 케이스 수를 입력받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    N = int(input())  # 배열의 크기를 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열을 입력받아 저장

    di = [1, 0, -1, 0]  # 상하좌우 이동을 위한 행 변화 값
    dj = [0, 1, 0, -1]  # 상하좌우 이동을 위한 열 변화 값

    max_v, min_v = 0, 1000001  # 최대값과 최소값을 저장할 변수 초기화
    for i in range(N):  # 배열의 모든 행에 대해 반복
        for j in range(N):  # 배열의 모든 열에 대해 반복
            temp = arr[i][j]  # 현재 위치의 값을 임시 변수에 저장
            for k in range(4):  # 상하좌우 4방향에 대해 반복
                a, b = i, j  # 현재 위치를 a, b에 저장
                if 0 <= a + di[k] < N and 0 <= b + dj[k] < N:  # 이동할 위치가 배열 범위 내에 있는지 확인
                    while 0 <= a + di[k] < N and 0 <= b + dj[k] < N:  # 이동할 위치가 배열 범위 내에 있는 동안 반복
                        temp += arr[a + di[k]][b + dj[k]]  # 이동한 위치의 값을 temp에 더함
                        a += di[k]  # 이동한 행 위치 업데이트
                        b += dj[k]  # 이동한 열 위치 업데이트
            if max_v < temp:  # 현재 temp 값이 최대값보다 크면
                max_v = temp  # 최대값 업데이트
            if min_v > temp:  # 현재 temp 값이 최소값보다 작으면
                min_v = temp  # 최소값 업데이트

    print(f'#{tc} {max_v - min_v}')  # 각 테스트 케이스에 대해 최대값과 최소값의 차이를 출력