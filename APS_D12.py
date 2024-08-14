# 교안 BFS 연습문제
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7

output
1 2 3 4 5 7 6
'''

def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    # 준비
    visited = [0] * (V+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    # 탐색
    while q:        # 큐에 정점이 남아있으면, (선형 큐의 경우 front != rear)
        t = q.pop(0)    # 디큐
        print(t)        # 방문한 정점에서 할일(이 문제에서는 출력)
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1
                # -> 이렇게 하면 visited 값 = 시작점에서 각 정점까지의 최단 간선 수 +1
                # bfs의 응용문제 기본형으로 생각하면 좋다 (최단 시간, 거리 구하기)
    print(visited)      # [0, 1, 2, 2, 3, 3, 4, 3]
V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, V)


# ================================
# DFS -> 재귀, 스택으로 해결
# BFS -> 큐
# 맨 앞 데이터 = 다음에 방문할 정점
#  -> 꺼낸 후 "갈 수 있는 정점"을 큐에 추가. 먼저 온게 먼저 나간다!


