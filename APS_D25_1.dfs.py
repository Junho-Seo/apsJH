# page25. 연습문제1
import sys
sys.stdin = open("graph.txt", "r")

# 시작점: 1번부터 시작
# 끝점: 1번에서 갈 수 있는 모든 정점을 방문하면 종료
#       (visited 처리 덕분에, 기저조건 없어도 자연스럽게 종료됨)
def dfs(node):
    print(node, end=' ')  # 현재 노드 출력

    # 현재 정점에서 연결되어있는 노드들을 탐색
    # graph[node][::-1] : 숫자가 큰 노드부터 탐색 (후보군을 뒤집어주면 된다.)
    for next_node in graph[node]:
        if visited[next_node]:  # 이미 방문했다면 통과
            continue

        visited[next_node] = 1  # 방문 처리
        dfs(next_node)          # 다음 정점으로 이동
# for 문 안에 재귀가 있기 때문에 next_node에서 갈 수 있는 모든 경우의 수를 모두 찍으며 for문이 반복된다!
# 그림 + 디버깅 중요. dfs에서는 다음에 어딜 방문할지 확인하는게 중요하기 때문에
# line 16에 bp를 찍고 디버딩한다.
N, M = map(int, input().split())
# 1. 비어있는 리스트: 아직 갈 수 있는 곳이 없다.
# 2. N + 1번: 0번 인덱스를 버리기 위해
#   -> 인접 리스트를 만들기 위해 아래와 같이 정의
graph = [[] for _ in range(N + 1)]
# graph = [[0]*(N+1) for _ in range(N+1)]  # 인접 행렬 예시
visited = [0] * (N + 1)

# 연결 정보를 저장
for _ in range(M):
    s, e = map(int, input().split())
    # 양방향(무향) 그래프이므로, 시작<->끝점을 바꾸면서 저장
    graph[s].append(e)
    graph[e].append(s)  # 문제가 방향 그래프라면, 바꾼 정보를 저장하면 버그난다!

visited[1] = 1  # 출발지 방문 처리
dfs(1)
