# 21911 .그래프마스터 - 석주의 크리스마스 트리

'''
1번 패턴 (중위 순회 inorder)
A의 왼쪽에 연결된 장식들이 켜집니다.
A가 켜집니다.
A의 오른쪽에 연결된 장식들이 켜집니다.

2번 패턴 (전위 순회 preorder)
A가 켜집니다.
A의 왼쪽에 연결된 장식들이 켜집니다.
A의 오른쪽에 연결된 장식들이 켜집니다.

3번 패턴 (후위 순회 postorder)
A의 왼쪽에 연결된 장식들이 켜집니다.
A의 오른쪽에 연결된 장식들이 켜집니다.
A가 켜집니다.

입력된 크리스마스 트리에 대해 , 각 패턴으로 실행하였을 때 각 장식에 불이 켜지는 순서대로 장식 번호를 출력해주세요.

단, 불이 켜지기 시작하는 장식 번호는 1 입니다.
'''

import sys
sys.stdin = open("input석주트리.txt", "r")
sys.stdout = open("output석주트리.txt", "w")


def dfs(node):
    if node == -1:		# -1은 장식이 없는 경우이므로 종료
        return

    preorder.append(node)   # 전위 순회 리스트에 추가
    dfs(graph[node][0])     # 왼쪽 장식으로 재귀 호출
    inorder.append(node)    # 중위 순회 리스트에 추가
    dfs(graph[node][1])     # 오른쪽 장식으로 재귀 호출
    postorder.append(node)  # 후위 순회 리스트에 추가


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [[] for _ in range(N+1)]  # 경로를 담을 인접 리스트
    for i in range(N):
        arr = list(map(int, input().split()))
        # p 특정 장식(부모 노드) , c1 왼쪽 장식(왼쪽 자식 노드), c2 오른쪽 장식(오른쪽 자식 노드)
        p, c1, c2 = arr[0], arr[1], arr[2]

        graph[p].append(c1)
        graph[p].append(c2)

    preorder = []
    inorder = []
    postorder = []

    dfs(1)

    print(f"#{tc}")
    print(*inorder)
    print(*preorder)
    print(*postorder)
