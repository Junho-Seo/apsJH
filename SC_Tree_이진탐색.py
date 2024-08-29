# 21999. [파이썬 S/W 문제해결 기본] Tree Day2 - 이진탐색

# 완전 이진 트리에 1~N 숫자 저장
# 규칙: 값의 크기가 왼쪽 서브트리 < 현재노드 < 오른쪽 서브트리
# => 1~N을 중위 순회하여 저장
import sys
sys.stdin = open("input이진트리.txt", "r")
sys.stdout = open("output이진트리.txt", "w")


T = int(input())


def inorder(node):
    global number
    if node < N+1:
        inorder(node * 2)  # 왼쪽 자식 노드 재귀 호출
        graph[node] = number  # 현재 노드에 number 할당
        number += 1  # number +1
        inorder(node * 2 + 1)  # 오른쪽 자식 노드 재귀 호출


for tc in range(1, T + 1):
    N = int(input())

    graph = [[0] for _ in range(N + 1)]

    number = 1
    inorder(1)

    print(f'#{tc}', graph[1], graph[N // 2])
