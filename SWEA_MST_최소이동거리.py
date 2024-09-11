# E개의 '일방통행' 도로
# 연결지점 0~N번 번호
# 시작지점, 끝지점, 구간길이
# 0 -> N의 최소 거리를 구하라

# 정점 중심. 최소 거리를 파악 -> 다익스트라
import heapq


def dijkstra(start):
    pq = []
    # 시작 노드 정보 pq에 삽입 (가중치, 노드) -> 가중치 오름차순
    heapq.heappush(pq, (0, start))
    # 출발점 초기화
    distance[start] = 0

    while pq:
        # 가장 최단 거리인 노드에 대한정보 pop
        dist, now = heapq.heappop(pq)
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue
        # 현재 노드에 인접한 노드 확인
        for next in graph[now]:
            next_node = next[0]  # 다음 노드 번호
            cost = next[1]  # 다음 노드의 가중치

            # 현재까지의 누적값 + 다음 노드 가중치
            new_cost = dist + cost

            # 다음 노드를 가는 데 더 많은 비용이 드는 경우
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost  # next_node까지 가는데 비용은 new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 시작 노드 번호
    start = 0
    # 인접리스트
    graph = [[] for _ in range(N+1)]
    # 누적 거리 저장 테이블
    distance = [float('inf')] * (N+1)

    # 간선 정보 입력
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    dijkstra(start)
    print(f'#{tc} {distance[N]}')
