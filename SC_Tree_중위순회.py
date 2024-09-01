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


T = int(input())

for tc in range(1,T+1):
    N, M, L = map(int,input().split())

    tree = [0]*(N+1)

    for _ in range(M):
        n, v = map(int,input().split())
        tree[n] = v

    for node in range(N,0,-2):
        p = node//2
        l,r = p*2, p*2+1
        if r > N:
            r=0
        tree[p] = tree[l] + tree[r]

    print(f'#{tc} {tree[L]}')

#----------------------------------


def dp_tree(num, arr, target):
    if num <= target:
        return arr
    if num % 2 == 1:
        arr[(num - 1) // 2] = arr[num - 1] + arr[num]
        return dp_tree(num - 2, arr, target)
    else:
        arr[num // 2] = arr[num]
        return dp_tree(num - 1, arr, target)


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    number = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        number[a] = b

    number = dp_tree(N, number, L)
    print(f'#{tc} {number[L]}')