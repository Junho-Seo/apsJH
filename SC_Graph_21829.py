# 21829. BFS 기초 - 방문 순서 출력하기
# 강사님 풀이
# 삭제가 많이 일어나는 bfs의 경우 리스트보다 덱 사용이 더 좋다.

from collections import deque

def bfs():
    q = deque([0])  # 주의점. 덱 안쪽에 [0] 넣어줘야함

    while q:
        now = q.popleft()  # 현재 지점
        print(now, end=' ')
        # 갈 수 있는 지점들을 모두 확인
        for next_idx in range(N):
            # 갈 수 없거나, 이미 방문했다면 통과
            if graph[now][next_idx] == 0 or visited[next_idx]:
                continue

            # next_idx: 갈 수 있는 정점 인덱스
            visited[next_idx] = 1
            q.append(next_idx)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 그래프 연결여부인데 0과 1이 모두 있다: 인접행렬
    graph = [list(map(int, input().split()))for _ in range(N)]

    # visited 전역으로 안 만드는 이유? 테케마다 초기화 해줘야하기 때문!
    visited = [0] * N  # 방문 체크용 리스트
    visited[0] = 1  # 출발점 방문 초기화
    print(f'#{tc}', end=' ')
    bfs()
    print()  # 개행 출력
