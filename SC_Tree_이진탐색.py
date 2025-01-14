# 21999. [파이썬 S/W 문제해결 기본] Tree Day2 - 이진탐색

# 완전 이진 트리에 1~N 숫자 저장
# 규칙: 값의 크기가 왼쪽 서브트리 < 현재노드 < 오른쪽 서브트리
# => 1~N을 중위 순회하여 저장
'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.


N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과
N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
'''
import sys
sys.stdin = open("input이진트리.txt", "r")
sys.stdout = open("output이진트리.txt", "w")


T = int(input())


def inorder(node):
    global number
    if node < N+1:
        inorder(node * 2)  # 왼쪽 자식 노드 재귀 호출
        graph[node] = number  # 현재 노드에 number 할당
        number += 1  # numbAer +1
        inorder(node * 2 + 1)  # 오른쪽 자식 노드 재귀 호출


for tc in range(1, T + 1):
    N = int(input())

    graph = [0]*(N + 1)

    number = 1
    inorder(1)

    print(graph)
    print(f'#{tc}', graph[1], graph[N // 2])
