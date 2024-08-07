n = 10

# 재귀
def fibo(num):
    if num < 2:
        return num

    return fibo(num - 1) + fibo(num - 2)

print(fibo(n))

# 메모이제이션
def fibo1(n):
    # global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))

# DP
def fibo2(n):
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# DFS 교안 연습문제 3
'''
다음은 연결되어있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐생 경로를 출력하시오
시작 정점을 1로 시작하시오
[입력]
1 tc
7 8 정점수 간선수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과
1 2 4 6 5 7 3
'''
def DFS(s, V):      # s 시작 정점, V 정점 개수(1번부터인 정점의 마지막 정점)
    visited = [0]*(V+1)     # 방문한 정점을 표시
    stack = []      # 스택 생성
    print(s)
    visited[s] = 1      # 시작 정점의 방문 표시
    v = s
    while True:
        for w in adjl[v]:  # v에 인접하고, 방문 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push하고
                v = w            # w에 방문
                print(v)
                visited[w] = 1      # w에 방문 표시
                break           # v부터 다시 탐색 (갈림길 선택)
        else:               # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack:       # 이전 갈림길을 스택에서 꺼내서... if TOP > -1
                v = stack.pop()
            else:       # 되돌아 갈 곳이 없거나 남은 갈림길이 없으면 탐색 종료(stack이 비어있으면)
                break   # while True에 대한 break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(V+1)]  # 비어있는 인접 리스트

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)

    # print(adjl)  # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

    DFS(1, V)  # 1 2 4 6 5 7 3   (되돌아간 지점은 찍히지 않고 방문 순서만 나옴)

# ===========================================
# (참고) append는 속도가 느리니 최대한 쓰지마라?
# 평균적인 시간복잡도: O(1). append는 좋다!
#  - 특수한 경우 O(N)만큼 시간이 걸리는 경우가 존재함

# 너무 많은 append가 발생하면
#   - 메모리 크기를 늘릴 때 시간이 추가로 발생
#   - 예측하지 못한 문제가 발생할 가능성이 올라감
# 결론: N값이 크지 않을 때(대략 1만 이하)만 append를 쓰자!

import sys
li =[]
print(sys.getsizeof(li))        # 56 (56 bytes; 빈 리스트) 큰 이유? 내장 메서드 포함하고있기 때문
for i in range(1, 100):
    li.append(i)
    # 메모리가 한번에 한 칸씩이 아닌 여러 칸씩(기하급수적으로) 확장
    # 따라서 데이터가 많을 수록 문제가 생길 가능성이 높아짐
    print(i, sys.getsizeof(li))

# 지금까지 배운 내용
# 1. 단순 구현
# 2. 효율적인 자료구조(스택)
# 3. 재귀 함수(top-down) -> 메모이제이션
# 4. DP(bottom-up)  => A형 기준 출제율 5~10% (거의 안나옴), B형에서 DP+DFS 활용 느낌 같은 거 나옴.
#   - 마스터하려면 많은 문제를 풀어보는 방법밖에 없다. (점화식 찾기)













