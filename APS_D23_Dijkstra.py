# 그래프는 D23 노션 확인
'''
[input]
6 9
0 1 2
0 2 5
1 3 1
2 3 10
1 4 3
2 5 20
3 5 15
3 4 20
4 5 4
'''


from heapq import heappop, heappush

def dijkstra(start):
    # 최단 누적 거리들을 저장할 리스트
    dists = [1e9] * (N) # 필요 인덱스에 따라 N+1

    # 출발지 초기화
    dists[start] = 0
    # 우선순위 큐
    pq = [(0, start)]

    while pq:
        # 현재 지점
        dist, now = heappop(pq)
        # now로부터 인접한 노드들을 확인
        for next_dist, next_node in graph[now]:
            # 현재 거리 + 다음으로 가는 거리
            new_dist = dist + next_dist

            # 갈 수 없다면 (누적 거리보다 기존 거리가 더 짧으면) pass
            # == 기존에 더 짧은 거리로 온 적이 있다면
            if new_dist >= dists[next_node]:
                continue
            # 갈 수 있다면
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    print(dists)


# 노드 수, 간선 수
N, M = map(int,input().split())
graph = [[] for i in range(N)] # 인접리스트 저장

for _ in range(M):
    # start, end, weight
    s, e, w = map(int,input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))
for i in range(N):
    print(graph[i])
# 0에서 시작했을 때 index 정점까지의 최단 거리
dijkstra(0)  # [0, 2, 5, 3, 5, 9]

# [개인적 궁금증] 다익스트라 그리디 증명 찾아보기 (귀납법 이용)
# MST (지난 A형 2번, 다음주 수요일 내용)