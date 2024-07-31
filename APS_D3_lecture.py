# 안내사항

# 역량테스트 8/19
# 빈출문제

# 백준 삼성 im > 검색해보면 연습문제 나옴
# 백준 실버까지 올라오면 문제없음
# SWEA d3~d4 수준. d3무난하게 풀면 됨

# IM에서 가장 많이 나오는 유형
# 1. 다차원 배열 순회
#   - 범위 계산 (가장 큰 영역, 작은 영역, 특정 값을 만족하는영역...)
#   - 델타 배열, min, max, index, 슬라이싱 ...
# 2. 스택, 큐, deque, 자료구조 활용하는 문제들
# 3. 기초적인 재귀

'''
5
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
'''

# import sys
# sys.stdin = open('in.txt', 'r')
# sys.stdout = open('out.txt', 'w')

# 이차원 리스트 다뤄보기
N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

# 1. 가장 기본적인 방법: 가로 줄 우선으로 순회
# total = 0 총합
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        # total += arr[i][j]
    print()
print('----------------------------------')
# 2. 세로줄 우선 순회
for i in range(N):      # for문의 i,j 위치는 바꾸지 않는 것을 추천. 나중에 헷갈리지 않도록.
    # total = 0 세로 한 줄의 합
    for j in range(N):
        print(arr[j][i], end=' ')
        # total += arr[j][i]
    print()
print('----------------------------------')
# 3. 우하단 대각선 순회
for i in range(N):
    print(arr[i][i], end=' ')
print()
print('----------------------------------')
# 4. 좌하단 대각선 순회
for i in range(N):
    print(arr[i][N-i-1], end=' ')
    print()
print('----------------------------------')


# 십자가 모양의 합이 가장 큰 곳을 구하시오.

# 델타 배열; 방향 배열(상, 하, 좌, 우 순서)
di = [0, -1, 1, 0, 0]       # 맨 앞 0, 0 추가는 자기 자신을 포함시키는 경우
dj = [0, 0, 0, -1, 1]

result = -1
max_i, max_j = 0, 0
for i in range(N):
    for j in range(N):
        sum_cross = 0
        for k in range(5):
            new_i = i + di[k]
            new_j = j + dj[k]

            # 좌표 범위를 넘어갈 때 (모서리) 통과
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue
            # if 0 <= new_i <N and 0 <= new_j < N: 위 두 줄과 같은코드
            sum_cross += arr[new_i][new_j]

        # result = max(result, sum_cross)
        if sum_cross > result:
            result = sum_cross
            max_i = i
            max_j = j

    print(result, max_i, max_j) # 392 1 1

# 상하좌우에 대각선까지 포함하는 경우 델타배열 (예시는 12시부터 시계방향으로)
# di = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# dj = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# 이 경우 k의 range는 9


# 비트(0 or 1) 연산자
# - 2진수 계산

# 왼쪽 시프트 (왼쪽으로 민다)
print(1)  # 1
print(1 << 1)  # 2, 10(2) 2진수
print(1 << 2)  # 4, 100(2)
print(1 << 3)  # 8, 1000(2)
print(1 << 4)  # 16, 10000(2)
print(1 << 5)  # 32, 100000(2)

print(3 << 2)  # 1100(2)

print(5 << 3)  # 101000(2)

# & : 1이 공통으로 나오는 부분을 남긴다
# | : 1을 모두 남긴다
# 1100  1010
print(12 & 10)  # 1000 = 8
print(12 | 10)  # 1110 = 14

print('---------------------------')

arr = [1, 2, 3, 4]  # 부분 집합의 수 : 16가지 (2^4)

for i in range(1 << len(arr)):
    print(i, end='')  # 0부터 15까지 16개 찍힘

print('----------------------------')

# 전체 부분집합을 구해야 하는 문제 해결 방법
#   - 재귀
#   - 비트 연산
#   - itertools (보약, 이런게 있다 정도만 알아두기)

for i in range(1 << len(arr)):
    # i의 의미: i 번째 부분 집합
    print(i, end=' / ')
    for j in range(len(arr)):
        # print(j, end=' ')
        # print(1 << j, end=' ')
        # 1 << j: 0001 0010 0100 1000
        # 1 & (1 << j)
        #   - i 번째 부분집합에서 각 요소가 포함되어 있는지 아닌지
        #   - 포함 되어 있다면 출력해라
        if i & (1 << j):
            print(arr[j], end=' ')      # 전체 부분집합 출력
    print()



print('---------------------------')
# itertools
# 순열 조합 문제에서 딸깍하면 된다.
#   - 최대한 쓰지 마세요!
#   - 학습으로 안좋다.

arr = [1, 2, 3, 4]
import itertools

permutations = itertools.permutations(arr, 4)
for perm in permutations:
    print(perm)

print('---------------------------')
combinations = itertools.combinations(arr, 2)
for comb in combinations:
    print(comb)