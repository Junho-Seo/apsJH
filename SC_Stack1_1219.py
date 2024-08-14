# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
# stack + DFS. 복습필요

'''
 A 도시에서 출발하여 B 도시로 가는 길을 조사하라
 갈림길은 최대 2개, 모든 길은 일방통행
 A = 0, B = 99
 모든 길은 순서쌍으로 표현
 정점의 개수는 출발점과 도착점을 제외하고 98개를 넘어가지 않는다.

[데이터 저장 가이드]
정점(분기점)의 개수가 최대 100개 이기 때문에, size [100]의 정적 배열 2개을 선언하여,
각 정점의 번호를 주소로 사용하고, 저장되는 데이터는 각 정점에서 도착하는 정점의 번호를 저장한다.

[입력]
총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 공백으로 분리되어 주어진다.
그 다음 줄에는 순서쌍이 주어진다. 순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(가능 여부)을 출력한다.
가능할 경우 1, 불가능할 경우 0을 출력한다.

'''

# 1. 받은 경로 정보를 그래프 구조(인접 리스트)로 저장
# 2. DFS를 이용한 경로 탐색
# 3. 경로가 있으면 1 없으면 0 출력



for tc in range(1, 11):
    T, N = map(int, input().split())
    paths = list(map(int, input().split()))  # 경로 정보를 리스트로 입력 받음

    # 인접 리스트 생성 및 경로 추가
    adj_list = [[] for _ in range(100)]
    for i in range(0, len(paths), 2):
        adj_list[paths[i]].append(paths[i + 1])  # 주어진 경로 정보를 인접 리스트에 추가

    # DFS 탐색
    visited = [0] * 100  # 도시 번호 0부터 99까지의 방문 상태를 기록하기 위한 리스트
    stack = [0]  # DFS를 시작할 때 사용할 스택, 초기값은 출발점인 도시 0

    while stack:
        v = stack.pop()  # 스택에서 도시를 하나 꺼냄
        if v == 99:  # 만약 꺼낸 도시가 99번(목적지)이라면
            print(f"#{tc} 1")  # 경로가 존재하므로 1을 출력
            break  # 탐색 종료
        if not visited[v]: #if visited[v] == 0:  # 현재 도시를 방문하지 않았다면
            visited[v] = 1  # 방문한 것으로 표시
            stack.extend(adj_list[v])  # 현재 도시와 연결된 인접 도시들을 스택에 추가
    else:
        # 스택이 모두 비었는데도 목적지(99번)에 도달하지 못한 경우
        print(f"#{tc} 0")  # 경로가 없으므로 0을 출력