# 연습문제1
'''
stack = []
stack.append(1)  # push(1)
stack.append(2)  # push(2)
stack.append(3)  # push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
'''
# --------------------------------
'''
STACK_SIZE = 10
stack = [0]*STACK_SIZE
top = -1

top += 1        # push(1)
stack[top] = 1
top += 1        # push(2)
stack[top] = 2
top += 1        # push(3)
stack[top] = 3

top -= 1        # pop()
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top -= 1
'''
# 연습 문제 2
# 풀어보기

# -------------------------
# 순서대로 받는다 (stack 그림 그리며 생각해보기)
def f2(d, c):
    return d - c

def f1(b, a):
    c = a + b
    d = 10
    return f2(c, d)

a = 10
b = 20
print(f1(a, b))

# ------------------------------
# 재귀 호출
# 팩토리얼
def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return
    else:
        f(n-1)

cnt = 0
f(5)
print(cnt)

print(f(5))


# 모든 배열 원소에 접근하기
def f(i, N):        # i 현재 인덱스, N 크기
    if i == N:      # 배열을 벗어난 경우
        return
    else:
        print(arr[i])
        f(i+1, N)
        return      # 함수의 마지막 return은 생략해도 처리됨



## 오프라인 정리
## 스택 Stack
# 먼저 들어온 데이터가 나중에 나간다 (FILO; First-In-Last-Out)
# 우리가 사용하는 메모리 구조 -> 스택 메모리라고 부른다.
# 문제 유형
#   - 괄호 유효성 검사
#   - 후위 표기법 문제(계산기)
#   - 재귀 + 메모이제이션
#   - DP
# 데이터를 쌓아나가며(append), 위에서부터 제거(pop)하면서 풀면 되는 문제
# 문제에서 이 구조를 찾아내는게 어렵다(핵심)
# IM에서도 자주 나오는 유형!

# 큐 Queue
# 먼저 들어온 데이터가 먼저 나간다 (FIFO; First-In-First-Out)
# 다음주 내용!

# 재귀 함수
#   - 자기 자신을 호출하는 함수
#   - 특징
#   1. 반드시 종료 조건을 가진다.
#   2. 반복문보다 '많이' 느리다.

# 팩토리얼
N = 5
# 1. 파라미터: 시작점을 기준으로 생각
def factorial(num):
    # 2. 종료 조건
    if num == 1:
        return num
    # 3. 재귀함수 호출
    # - 호출 전 (이 문제에는 X)
    # - 다음 호출 (num - 1 값을 줘야한다.)
    # - 호출 후 (이 문제에는 X)
    return num * factorial(num-1)

print(factorial(N))

# 피보나치 수열
# N번째 숫자는?

# 해결 방법1. 앞에서 부터 쌓아나가는 방식 (Bottom-up) - 반복문
#   - 설계가 어렵다.(식을 만족하는 규칙(점화식)을 찾아야 한다)
#   - 속도가 재귀에 비해 빠르다.
#   - 이게 DP(Dynamic Programming) 다.
#       - 계산한 결과를 저장해두고 한 번 더 쓰자
N = 10

fibo = [0, 1] + ([0]*(N + 1))
for i in range(2, N + 1):
    # 이전 값을 구해서 저장해 놓았으므로, 바로 가져와 사용한다.
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[N])

# 해결 방법2. 위에서부터 쪼개면서 내려오는 방식(Top-down) - 재귀
#   - 구현이 쉽다.
#   - 속도가 느리다.
#      -> 문제점: 여러번 같은 값을 계산한다! 매우 비효율적 O(2^N)
#      -> N값이 22~23 이상이면 1초 내로 해결 못한다!
#      -> 해결법. 값을 저장해두고 쓰는 기법: 메모이제이션(memoization) O(N)
N = 10
def fibo(num):
    # 종료 조건
    if num < 2:
        return num

    return fibo(num - 1) + fibo(num - 2)

print(fibo(N))

# 메모이제이션 적용
def fibo2(num):
    # 종료 조건
    if num < 2:
        return num

    # 이미 계산된 값이면 계산된 값을 return
    if memo.get(num):
        return memo[num]

    # 계산이 안 된 값이면 저장 + return
    memo[num] = fibo(num - 1) + fibo(num - 2)
    return memo[num]

memo = {}
print(fibo2(N))

# 그래프
# 그래프란?
#   - 자료 구조 중 하나. 데이터 사이의 관계를 표현하기 위해 사용함
#   - 관계 (relation)
#     - 데이터끼리 연결되어있다.
#     - ex) 경로가 있다, 비례한다 등등
#   - 현실에서 연결되어 있는 데이터들을 표현하기 위해 사용하는 자료구조
#     - ex) 주식(시간-가격), 지하철(역1-역2), SNS(사용자1-사용자2) 등
# 용어
#   - 정점(Vertex), 노드(Node)
#     - 데이터(객체)를 나타내는 요소
#   - 간선(Edge)
#     - 두 정점 사이의 연결(관계)를 나타내는 요소
#     - 방향이 있는 간선, 방향이 없는(양방향) 간선이 존재함
#       - 방향이 있는 간선 -> 방향 그래프
#       - 양방향 간선 -> 무방향 그래프
# 그래프 종류
#   - 무방향 그래프
#     - 간선에 방향이 없는 그래프
#     - ex) 친구 관계, 인터넷, 도로 등
#   - 방향 그래프
#     - 간선에 방향이 있는 그래프
#     - ex) 팔로우/팔로워, 웹페이지 링크 등
#   - 가중치 그래프
#     - 간선 사이에 가중치(거리, 시간 등)가 존재하는 그래프
#     - ex) 네비게이션, 최소 가중치, 최소 비용 문제 등
#   - 연결 그래프
#     - 모든 정점이 서로 연결되어 있는 그래프 (특수한 경우)
# 이걸 어떻게 코드로 표현할까?
#   - 데이터와 연결 여부를 코드로 표현해야한다.
#   - 크게 두 가지 방법이 있다.
#   1. 인접 행렬
#     - (V * V) 이차원 리스트로 표현
#     - 간선 존재 여부를 모두 2차원 리스트에 저장
#     - 'graph[i][j] == 0' 이라면 i, j 사이에 간선이 존재하지 않음
#     - 'graph[i][j] == 1' 이라면 i, j 사이에 간선이 존재함

# 해당 그래프 그림은 mm
graph = [
    [0, 1, 1, 0, 0],     # 1번의 연결 정보
    [1, 0, 0, 1, 1],     # 2번의 연결 정보
    [1, 0, 0, 1, 0],     # 3번의 연결 정보
    [0, 1, 1, 0, 0],     # 4번의 연결 정보
    [0, 1, 0, 0, 0],     # 5번의 연결 정보
]
#     - 장점: 구현이 쉽다. 특정 간선 존재 여부를 한 번에 알 수 있다.
#     - 단점: 메모리를 너무 많이 차지한다.(공간 효율성이 안 좋다.)

#   2. 인접 리스트
#     - 연결되어있는 정점에 대한 정보만 저장하는 방식
#     - 'graph[i]' : i 정점에서 갈 수 있는 정점들에 대한 정보

graph = [
    [1, 2],     # 1번의 연결 정보
    [0, 3, 4],     # 2번의 연결 정보
    [0, 3],     # 3번의 연결 정보
    [1, 2],     # 4번의 연결 정보
    [1],     # 5번의 연결 정보
]
#     - 장점: 메모리가 효율적으로 관리된다.
#     - 단점: 특정 간선 존재 여부 확인이 느리다.
#   - 문제 상황마다 둘 다 활용 가능해야함
#   - 보통은 인접 리스트 방식이 효율적.
# 어떻게 활용될까?
#   - 위와 같은 구조로 만든 데이터 전체를 탐색하는 기법
#   - 즉, 그래프의 완전 탐색 기법
#     - DFS(Depth First Search) 깊이 우선 탐색
#       - 갈 수 있는 방향으로 끝까지 탐색
#       - 더 이상 갈 수 없다면 되돌아와서 가능한 곳으로 다시 반복
#       - 구현: 재귀, 스택(stack) (재귀가 훨씬 많이쓰임. 더 쉬움)
#       - ex) 미로 탐색
#     - BFS(Breadth First Search) 너비 우선 탐색
#       - 현재 정점에서 주변을 우선으로 탐색하면서 나아가는 방식
#       - 구현: 큐(queue)
#       - ex) 지하철 노선 검색






