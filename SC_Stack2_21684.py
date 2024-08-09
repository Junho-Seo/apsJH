#21684 . [파이썬 S/W 문제해결 기본] 5일차 - 미로
# 대표적인 쉬운 DFS 문제

# IM에서 A형으로 넘어가는 기본 유형
#   재귀 + 델타탐색 (매우 중요!)

# 1. 출발점에서 갈 수 있는 끝까지 확인.
# 2. 갈 수 있는 좌표로 되돌아온다.

# 특정 시점으로 "되돌아온다" => 재귀
# 상하좌우로 이동한다 => 델타 탐색

# 풀이법
# 1. 시작점과 도착점(종료)을 따로 저장해둔다.
# 2. 갈 수 있는 방향이면 이동.
#   - 갈 수 없는 조건: 벽, 범위, 방문기록 (if문 3개)

# 맨 처음좌표에서 위만 확인. (위는 예시)
# 쭉 진행
# 막히면 좌우 -> 막히면 한 칸 되돌아오기
# 시작점까지 되돌아왔다면 좌, 우, 하 중 다시 마찬가지로 탐색

# 이 문제의 경우는 방향 순서 상관없으므로 편한대로 설정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global result
    # base case 종료 조건(기저 조건)
    if y == endy and x == endx:
        result = 1  # 도착했다면 return에 1 할당
        return      # 함수 종료

    # next call 다음 재귀 호출
    for i in range(4):
        newy = y + dy[i]
        newx = x + dx[i]
        # dfs(newy, newx)     # 제한 조건이 없는 경우는 여기서 끝

        # 1번 조건. 범위 밖으로는 나가지 못함
        if newy < 0 or newy >= N or newx < 0 or newx >= N:
            continue        # 코드 가독성(짧게)을 위해 continue 쓰는걸 추천

        # 2번 조건. 벽이면 못감
        if graph[newy][newx] == 1:
            continue

        # 3번 조건. 방문한 지점은 못감
        if visited[newy][newx]:
            continue
        # 강의라 3가지 조건을 분리했지만 한 줄로 or로 작성해도 됨
        # if newy < 0 or newy >= N or newx < 0 or newx >= N or graph[newy][newx] == 1 or visited[newy][newx]:
        #     continue
        visited[newy][newx] = 1  # 방문처리
        dfs(newy, newx)  # 다음 좌표로 이동


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(graph)  # [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]

    # 시작점, 도착점을 좌표에 담는다
    starty, startx, endy, endx = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                starty, startx = i, j

            if graph[i][j] == 3:
                endy, endx = i, j
    # 제한 조건 벽, 범위는 graph, N으로 주어짐
    # 마지막 제한조건인 방문기록 작성
    visited = [[0] * N for _ in range(N)]
    visited[starty][startx] = 1  # 시작점
    result = 0
    dfs(starty, startx)
    print(f'#{tc} {result}')


# 라이브 강사님 풀이

# 벽으로 둘러쌓인 미로 vs 뚫린 미로
# 이문제는 뚫려있으므로 경계 처리까지 신경써야함

# 지나온 자리 처리
#   - 지나간 자리를 메꾸거나
#   - 배열을 따로 만들어 지나간 자리를 표시한다

# def dfs2(i, j, N):      # 재귀
#     visited[i][j] = 1       # 현재 위치를 방문표시
#     if maze[i][j] == 3:     # 목적지(3)에 도착하면,
#         return 1            # 1 반환
#     else:
#         # 이동 가능한 방향(우, 하, 좌, 상)으로 탐색
#         for di, dj in [[0,1], [1, 0], [0, 1], [-1, 0]]:
#             ni, nj = i+di, j+dj     # 다음 위치 계산
#             # 다음 위치가 미로 범위 내에 있고 벽(1)이 아니며 방문한 적이 없다면,
#             if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
#                 if dfs2(ni, nj, N):     # 다음 위치로 재귀 호출하여 목적지에 도착하면,
#                     return 1        # 1 반환
#         return 0        # 모든 방향 탐색에서 목적지에 도착하지 못하면 0 반환
#
# def fstart(N):
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:     # 출발지(2) 위치를 찾으면,
#                 return i, j     # 해당 위치 반환
#     return -1, -1       # 출발지(2)를 찾지 못하면 -1, -1 반환
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input().split())) for _ in range(N)]
#
#     # 출발지 위치 찾기
#     sti, stj = fstart(N)
#     # dfs2 용(방문 여부를 기록할 2차원 배열 초기화)
#     visited = [[0]*N for _ in range(N)]
#     # 결과 출력
#     print(f'#{tc} {dfs2(sti, stj, N)}')
