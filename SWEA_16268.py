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
    max_cnt = 0     # 최대 합을 저장할 변수 초기화

    for i in range(N):  # 배열의 모든 행에 대해 반복
        for j in range(M):  # 배열의 모든 열에 대해 반복
            temp = 0  # 임시 합계를 저장할 변수 초기화
            for k in range(5):  # 현재 위치와 상하좌우 4방향에 대해 반복
                ni = i + di[k]  # 이동한 행 위치 계산
                nj = j + dj[k]  # 이동한 열 위치 계산
                if ni < 0 or nj < 0 or ni >= N or nj >= M:  # 이동한 위치가 배열 범위를 벗어나면 건너뜀
                    continue
                temp += arr[ni][nj]  # 이동한 위치의 값을 temp에 더함
            if temp > max_cnt:  # 현재 temp 값이 최대값보다 크면
                max_cnt = temp  # 최대값 업데이트

    print(f'#{test_case} {max_cnt}')  # 각 테스트 케이스에 대해 최대 합을 출력