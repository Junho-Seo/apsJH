# 21996. [파이썬 S/W 문제해결 기본] 8일차 - subtree

'''
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를
알아내는 프로그램을 만드시오.
'''

import sys
sys.stdin = open("inputsubtree.txt", "r")
sys.stdout = open("outputsubtree.txt", "w")


def dfs(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    # dfs(child1[node])
    # dfs(child2[node])
    # dfs(graph[node][0])
    # dfs(graph[node][1])
    for next_node in graph[node]:
        dfs(next_node)

# bfs로도 풀이 가능


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    graph = [[] for _ in range(E+2)]
    # child1 = [0] * (E + 2)
    # child2 = [0] * (E + 2)


    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        graph[p].append(c)

    # for i in range(E+2):
    #     while len(graph[i]) < 2:
    #         graph[i].append(0)
        # if child1[p] == 0:
        #     child1[p] = c
        # else:
        #     child2[p] = c

    dfs(N)
    print(f"#{tc} {cnt}")
    print(graph)
