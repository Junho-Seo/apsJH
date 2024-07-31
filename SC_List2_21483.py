# 21483. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
# 참조. (https://velog.io/@yunhlim/SWEA-4836.-파이썬-SW-문제해결-기본-2일차-색칠하기-D2)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())                        # 색칠할 영역의 개수
    arr = [[0]*10 for _ in range(10)]       # 빈 10x10 배열
    counts = 0                              # 겹쳐지는 영역의 칸 수
    for _ in range(1, N+1):
        # 영역 정보
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 배열 값이 0(빈 칸)일 경우 해당 칸에 color 값을 넣는다.
                if arr[i][j] == 0:
                    arr[i][j] = color
                # 배열 값이 0이 아닐 경우 이미 색이 있는 칸이므로 counts에 1을 더한다.
                else:
                    counts += 1

    print(f'#{test_case} {counts}')
