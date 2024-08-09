# 연습문제2
"""
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이
10인 부분집합을 구하시오
"""


def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1
    # 가지치기를 한 경우(백트래킹)
    if s > t:  # 1. 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:  # 2. 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:  # 3. 모든 원소 고려
        return
    # 가지치기를 하지 않은 경우
    # if i == k:        # 모든 원소 고려
    #     if s == t:
    #         cnt += 1
    else:
        bit[i] = 1
        f(i + 1, k, s + A[i], t)  # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t)  # A[i] 미포함


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
# A = [ i for i in range(1, N+1)

key = 55
cnt = 0  # 합이 key와 같은 부분집합의 수. key 55에서 1, key 10에서 10
bit = [0] * N
fcnt = 0    # 함수의 호출 횟수
f(0, N, 0, key)
print(cnt, fcnt)    # 가지치기를 한 경우 10, 349, 하지 않은 경우 10, 2047

# ==============================
# DFS와 백트래킹의 차이 (구분하기 힘들고 의미가 없긴하다. 비슷함.)
# 둘 다 재귀 베이스
# DFS -> 가능한 모든 경우의 수
# 백트래킹 -> 가지치기 (재귀 호출 수를 줄인다)

# 함께 구현하기
# 1. 부분집합
# 2. 순열
# 3. 조합.

# 1. 부분집합
elements = ['A', 'B', 'C', 'D']

# result = []     # 결과들을 한 눈에 보기 위해 사용
# subset = []     # 부분집합 하나 하나


# def recur(now):
#     result.append(subset[:])  # 출력을 위해 결과 리스트에 저장 (공집합)
#
#     # 다음에 뽑을 수 있는 것들을 반복
#     for i in range(now, len(elements)):
#         subset.append((elements[i]))  # i번째 요소를 뽑았다.
#         recur(i + 1)  # 다음 재귀(그 다음 요소를 뽑아야한다)
#         subset.pop()  # i번째 요소를 뽑기 전으로 돌려놓는 코드
#
# recur(0)
# print(result)       # 부분 집합 출력

# 2. 순열
subset = []  # 부분집합 하나 하나
result1 = []  # 결과들을 한 눈에 보기 위해 사용
K = 3  # 3개만 뽑는다. -> 종료 조건이 추가된 것


# 중복 순열
def recur1(cnt):
    # k 개를 뽑았다면 반복 중지
    if cnt == K:
        result1.append(subset[:])
        return

    for i in range(len(elements)):
        subset.append(elements[i])
        recur1(cnt + 1)
        subset.pop()


recur1(0)
print(result1)

# 순열
result2 = []
visited = [0] * len(elements)


def recur2(cnt):
    # k 개를 뽑았다면 반복 중지
    if cnt == K:
        result2.append(subset[:])
        return

    for i in range(len(elements)):
        if visited[i]:  # i 번째 요소를 사용했다면
            continue  # continue

        visited[i] = 1  # i번째 요소를 사용했다는 기록(중복체크)
        subset.append(elements[i])
        recur2(cnt + 1)
        subset.pop()
        visited[i] = 0  # i번째 요소 사용 기록을 제거


recur2(0)
print(result2)

# 3. 조합
result3 = []


def recur3(now):
    # k 개를 뽑았다면 반복 중지
    if len(subset) == K:
        result3.append(subset[:])
        return

    for i in range(now, len(elements)):
        subset.append(elements[i])
        recur3(i + 1)  # i 번째 다음부터 골라라
        subset.pop()


recur3(0)
print(result3)

# 참고. itertools <- 부분집합류 딸깍 가능
# 사용하지 말것. 역테에서 사용불가, 코테에서도 못 쓸 가능성 있음
