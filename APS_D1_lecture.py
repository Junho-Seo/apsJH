# 빅오표기법:O(1)
#       - 상수번만큼 loop를 돈다
for i in range(100000000000):
    pass

# 빅오 표기법 O(N)
N= 1000
for i in range(N):
    pass

N=100
# 실제 실행: 10000*100
# 빅오 표기법 O(N)
for i in range(N):
    for j in range(10000):
        pass

num = [1, 2, 3]
# in 키워드: 빅오표기법: 0(N)
#       - 실제 연산 횟수 == 리스트 길이
if 2 in num:
    print(2)

# 실제 실행: 100 + 200
# 빅오 표기법: O(N + M)
N, M = 100, 200
for i in range(N):
    pass

for j in range(M):
    pass

# 실제 실행: 약 7번 (log2(100))
# 빅오 표기법: O(logN)
N = 100

def example(N):
    i = 1
    while i < N:
        i *= 2

example(N)


# 실제 실행: 100 * 7 = 약 700번
# 빅오표기법: O(NlogN)
N = 100

def example1(N):
    for j in range(N): # 100번
        i = 1          # 7번
        while i < N:
            i *= 2

example1(N)


N = 10

def example3(N):
    if N == 1:
        return

    example3(N - 1)

example3(N)

# 실제 실행: 5!(120번)
# 빅오표기법: O(N!)
N = 5

def example4(N):
    if N == 0:
        return

    for i in range(N):
        example4(N-1)

# 1초: 최대 N은?
# 11넘으면 터진다! 팩토리얼 빅오는 주의.


# %%
N = 6
arr = [7, 2, 5, 3, 4, 1]

for i in range(N - 1, 0, -1):  # 각 구간의 끝 인덱스 i
    for j in range(i):  # 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 왼쪽 원소가 더 크면 교환

print(*arr)