# 오늘 공유된 코드
# 1. 가장 사용이 쉽고
# 2. 시간적으로 효율적인 방식!
#   - 다양한 방식의 더 좋은 코드도 있을 수 있다.

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop

# 정리하자면 BFS + 그리디(최소 비용 정점을 먼저 선택)
def prim(start):
    heap = list()
    MST = [0] * (V)     # visited 랑 똑같다 (강의 가독성)

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    # heappush(heap, (start, 0))  # 이렇게 쓰면 정점 번호를 기준으로 정렬이 되기 때문에 안 된다!
    heappush(heap, (0, start))  # 시작점은 가중치가 0이다.

    while heap:
        weight, v = heappop(heap)  # 현재 시점에서 가중치가 가장 작은 정점 pop
        
        # 이미 방문한 지점이면 통과
        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())
# 인접 행렬로 구현
# 인접 리스트가 더 좋다며?
#   - 인접 리스트로 변경은 '반드시 직접' 해봐라 [과제]
graph = [[0] * (V) for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  # 가중치가 있는 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')  # 최소 비용 = 175