# 21996. [파이썬 S/W 문제해결 기본] 8일차 - subtree

'''
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를
알아내는 프로그램을 만드시오.
'''

import sys
sys.stdin = open("inputsubtree.txt", "r")
sys.stdout = open("outputsubtree.txt", "w")

# 전위순회로 cnt+=1
def dfs(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    dfs(graph[node][0])
    dfs(graph[node][1])
    # for next_node in graph[node]:
    #     dfs(next_node)

# bfs로도 풀이 가능


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())    # 간선의 개수 E, 노드 N
    arr = list(map(int, input().split()))   # 노드 번호 쌍(부모, 자식)
    cnt = 0     # 자식 노드 개수 카운팅

    graph = [[] for _ in range(E+2)]    # 경로 인접 리스트

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        graph[p].append(c)

    for i in range(E+2):        # 자식이 두개 미만인 경우 0 추가
        while len(graph[i]) < 2:
            graph[i].append(0)

    dfs(N)
    print(f"#{tc} {cnt}")
    print(graph)
