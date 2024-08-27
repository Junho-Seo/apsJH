# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open("input중위순회.txt", "r")
sys.stdout = open("output중위순회.txt", "w")


# 중위 순회 dfs
def dfs(node):
    if node == -1:
        return

    dfs(graph[node][0])
    # result에 중위 순회 노드의 알파벳 추가
    result.append(graph[node][2])
    dfs(graph[node][1])


for tc in range(1, 11):
    N = int(input())
    # 인접 리스트
    graph = [[] for _ in range(N+1)]

    for i in range(N):
        arr = list(map(str, input().split()))
        # 자식이 없는 경우 -1로 표시되도록 추가
        while len(arr) < 4:
            arr.append("-1")
        # 해당 노드 숫자, 해당 노드 알파벳, 왼쪽 자식, 오른쪽 자식
        num, word, c1, c2 = int(arr[0]), arr[1], int(arr[2]), int(arr[3])

        graph[num].append(c1)
        graph[num].append(c2)
        graph[num].append(word)

    result = []

    dfs(1)
    print(f'#{tc}', end=' ')
    print(''.join(result))
