# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
'''
사칙연산 트리 > 중위 순회 inorder (좌>부모>우)

사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다.
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과에 해당 연산자를 적용한다.

사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.
계산 중간 과정에서의 연산은 모두 실수 연산으로 한다.

[입력]

총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 줄에는 정점의 개수 N(1≤N≤1000)이 주어진다.
그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.
정점이 정수면 정점 번호와 양의 정수가 주어지고, 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
정점 번호는 1부터 N까지의 정수로 구분된고 루트 정점의 번호는 항상 1이다.

[출력]

각 테스트케이스마다 '#t'(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 사칙연산을 계산한 결과값을 출력한다.
결과값은 소수점 아래는 버리고 정수로 출력한다.

'''


import sys
sys.stdin = open("input사칙연산.txt", "r")
sys.stdout = open("output사칙연산.txt", "w")


# 후위 순회 postorder
def postorder(node):
    # 현재 정점의 값이 숫자라면 int 로 변환하여 반환
    if node_value[node].isnumeric():
        return int(node_value[node])

    # 현재 정점이 연산자라면
    # 왼쪽 자식의 값을 재귀 호출
    left_value = postorder(graph[node][0])
    # 오른쪽 자식의 값을 재귀 호출
    right_value = postorder(graph[node][1])

    # 연산자에 따라 계산
    if node_value[node] == '+':
        return left_value + right_value
    elif node_value[node] == '-':
        return left_value - right_value
    elif node_value[node] == '*':
        return left_value * right_value
    elif node_value[node] == '/':
        return left_value / right_value


for tc in range(1, 11):
    N = int(input())
    node_value = [0] * (N+1)   # 각 정점의 값을 저장하는 배열
    graph = [[] for _ in range(N+1)]    # 각 정점의 자식 정보를 저장하는 그래프

    for _ in range(N):
        node_input = input().split()
        # 정점 번호를 인덱스로 정점 값 저장
        node_number = int(node_input[0])
        node_value[node_number] = node_input[1]

        # 자식 노드가 존재한다면 (= 연산자라면)
        if len(node_input) > 2:
            # 자식의 정점 번호를 그래프에 저장
            graph[node_number] = [int(node_input[2]), int(node_input[3])]

    result = int(postorder(1))

    print(f'#{tc} {result}')
