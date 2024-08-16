# 21704 .바이러스 죽이기

# 이차원 리스트 + 델타 탐색
# 십자가 아닌 다른 모양의 경우는 어떻게 되는지 생각해보기. (x자, 사각형 등)
"""
바이러스가 한 마을을 집어삼켰다

여기에 차르봄바라는 아주 강력한 백신 폭탄을 떨어뜨려, 최대한 많은 바이러스를 제거하려고 한다.

차르봄바는 P 크기만큼으로 가로, 세로 방향으로 퍼져나가면서 해당 영역의 바이러스를 제거할 수 있다.

N x N 크기의 마을의 한 위치에 차르봄바를 떨어뜨려, 가장 많은 바이러스를 제거했을 때 제거된 바이러스의 수를 구하여라
[제약사항]

3 <= N <= 100
1 <= P < N
0 <= 각 위치의 바이러스의 개수 <= 1,000

[testcase input]
4
7 3
1 8 1 4 2 5 1
1 5 2 6 7 2 3
7 9 5 5 1 9 8
3 7 0 9 8 0 7
5 5 3 9 5 1 4
2 5 9 3 3 6 8
0 1 4 1 8 4 0
7 2
3 3 8 8 5 5 0
4 3 9 6 0 2 5
0 8 6 2 0 3 8
5 1 0 8 2 9 6
1 7 5 3 9 2 0
8 4 2 9 5 5 3
2 3 6 2 9 1 4
5 3
9 3 0 4 0
3 9 4 0 4
0 4 9 4 0
4 0 4 9 3
0 4 0 3 9
5 4
1 2 3 4 9
2 3 4 5 9
3 4 5 6 9
4 5 6 7 9
9 9 9 9 9
[testcase output]
#1 75
#2 47
#3 40
#4 81

"""
# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]
    ans = 0  # 최대 바이러스 제거 합 변수 초기화
    # 모든 위치 탐색
    for i in range(N):
        for j in range(N):
            temp = village[i][j]  # 선택 칸 포함. 미포함이면 0
            for y in range(4):  # 델타 방향 순회
                for x in range(1, P + 1):  # 1부터 P까지 십자 거리
                    new_i = i + di[y] * x
                    new_j = j + dj[y] * x
                    # 제약 조건 continue
                    if 0 > new_i or new_i >= N or 0 > new_j or new_j >= N:
                        continue
                    # 선택 위치 합계
                    temp += village[new_i][new_j]

            # 최대 바이러스 제거 합 갱신
            if temp > ans:
                ans = temp

    print(f"#{tc} {ans}")
