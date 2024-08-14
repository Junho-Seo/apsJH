# Queue (bfs) 라이브강의 연습문제
# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

"""
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

sample input
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

sample output

#1 5
#2 5
#3 0

"""


def bfs(i, j, N):
    # 준비
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q =[]       # 큐생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 인큐 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)       #디큐
        if maze[ti][tj] == 3:       # visited(t)
            return visited[ti][tj] - 1 - 1  # 경로의 빈 칸 수, -1 추가
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고, 벽이 아니면
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj]) # 인큐
                visited[wi][wj] = visited[ti][tj] + 1       # 인큐 표시
    return 0   # 문제 생길 경우 디버깅 용

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input()))for _ in range(N)] # split이 없는 이유? input이 붙어서 나오기 때문(띄어쓰기가 없다)
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
