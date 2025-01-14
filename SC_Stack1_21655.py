#21655. DFS 기초 - 방문 순서 출력하기
# 강사님 풀이

'''
배열 or 링크드리스트 자료구조는 for문으로 쉽게 탐색이 가능하지만,
그래프 같은 자료구조는 for문으로 탐색이 어렵습니다.

NxN 그래프를 인접행렬로 입력받고 DFS 탐색 순서대로 출력하세요.
단, 낮은 번호의 정점을 우선적으로 탐색합니다.
'''


# 재귀 이용 dfs
def dfs(now):
    print(now, end = ' ')
    # visited[1] = 1  # global을 쓰지 않아도 특정 위치의 값을 변경 가능.(전부 바꾸는건 불가능)
    # 갈 수 있는 경로를 탐색하면서 이동
    for i in range(N):
        # 없는 경로, 기존에 방문했던 경로: continue
        # continue 좋아하는이유: 불가한 부분을 지나가는 구조. 가독성이 좋아진다
        if graph[now][i] == 0 or visited[i]:
            continue
        visited[i] = 1  # 방문 처리
        dfs(i)  # 재귀 호출 (다음 정점으로 이동)

# 스택 이용 dfs (라이브보다 쉽고 직관적인 코드)
# 다음에 가야 할 정점을 스택에 쌓는다.
def dfs_stack(start):
    stack = [start]

    while stack:  # stack이 있을 때 까지 돌아라
        now = stack.pop()  # 현재 방문한 정점
        if visited[now]:   # 방문했던 정점이면 pass
            continue

        print(now, end=' ')  # 현재 정점을 출력
        visited[now] = 1     # 방문 처리

        for i in range(N-1, -1, -1):        # 높은 번호부터 거꾸로 담아서 2번(낮은 번호)부터 pop 되도록 (stack: 후입선출)
            if graph[now][i] == 0 or visited[i]:
                continue

            stack.append(i)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 1. 인접행렬
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 1.1 방문 기록 체크
    visited = [0] * (N + 1)  # 이 문제는 N개만 만들어도 되지만 정점이 1부터 시작하는 경우 때문에 N + 1 습관화
    # visited[0] = 1  # 정점 0을 방문했다. (= 출발점 표시)

    print(f'{tc}', end=' ')
    # dfs(0)
    dfs_stack(0)
    print()
    # 2. 인접 리스트로 변경 후 사용



