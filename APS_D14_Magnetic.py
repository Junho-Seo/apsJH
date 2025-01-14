"""
1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

많은쪽 자석이 밀고 넘어간다? -> 문제가 더 어려워진다.

1 N극, 2 S극, 윗부분에 N극, 아래부분에 S극
  -> 1은 아래로, 2는 위로

접근 방법 -> 노션 체크
"""
N_pole = 1 # 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체
S_pole = 2 # 테이블의 윗부분에 N극이 아래부분에 S극이 위치

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0     # 교착상태 수
    for j in range(100):  # 열 우선 순회
        np = 0  # 아래로 향하는 N극이 있는지 표시
        for i in range(100):
            if arr[i][j] == N_pole:
                np = 1
            elif arr[i][j] == S_pole and np == 1: # N극과 S극이 만나는 경우 교착
                cnt += 1
                np = 0
    print(f'#{tc} {cnt}')