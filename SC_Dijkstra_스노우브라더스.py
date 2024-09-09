# 상하 이동 시 게이지 칸당 1 필요
# 보석을 먹기 위한 최소 limit를 구하시오

# N-1행의 위치에서 출발하여 최단거리로 보석을 먹을 때의 게이지를 구하고
# 그 중 최소값을 찾는다.

# 최단거리 찾기. bfs+우선순위큐
# 무조건 N-1행(가장 아래)에서 시작, N-1 행은 끊김이 없음.
# 1. 수직 상방 이동이 가능한 가장 가까운 위치로 수평이동
# 2. 보석의 행까지 수직 이동.
# 3. 보석 위치까지 수평 이동.
# 4. 길이 끊긴 경우 수직 이동 경우의 수 확인
import heapq

# 좌 우 상 하
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def dijkstra(y, x):
    # 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, y, x))
    # 최단 누적 거리 저장 리스트
    dist = [[1e9]*M for _ in range(N)]
    # 출발지 초기화
    dist[y][x] = 0

    while pq:
        now_cost, now_y, now_x = heapq.heappop(pq)

        # 도착
        if now_y == diry and now_x == dirx:
            return now_cost

        # 좌우
        for i in range(2):
            nx = now_x + dx[i]
            # 맵 탈출, 땅이 없는 경우, 다른 경로가 있는 경우
            if nx < 0 or nx >=M or map_info[now_y][nx] == 0 or dist[now_y][nx] <= now_cost:
                continue
            dist[now_y][nx] = now_cost
            heapq.heappush(pq, (now_cost, now_y, nx))

        # 상하
        for i in range(2, 4):
            for d in range(N):
                ny = now_y + dy[i]*d
                # 맵 밖으로 벗어나면 break
                if ny < 0 or ny >= N:
                    break
                # 허공이면 계속 진행
                if map_info[ny][now_x] == 0:
                    continue
                nc = max(d, now_cost)
                if dist[ny][now_x] <= nc:
                    continue
                dist[ny][now_x] = nc
                heapq.heappush(pq, (nc, ny, now_x))
    # 못 가는 경우 없음
    return -1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    y = x = diry = dirx = 0
    for i in range(N):
        for j in range(M):
            # 스노우맨 위치
            if map_info[i][j] == 2:
                y = i, x = j
            # 보석 위치
            if map_info[i][j] == 3:
                diry = i, dirx = j

    result = dijkstra(y, x)
    print(f'#{tc} {result}')