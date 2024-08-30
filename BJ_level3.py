# 2793. 구구단

# N = int(input())
#
# for i in range(1,10):
#     print(f"{N} * {i} = {N*i}")

# 10950. A+B-3

# T = int(input())
#
# for i in range(1, T+1):
#     A, B = map(int, input().split())
#     print(A+B)

# 8393. 합

# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     ans += i
#
# print(ans)

# 25304.영수증

# X = int(input())
# N = int(input())
#
# result = 0
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     result += a * b
#
# if X == result:
#     print("Yes")
# else:
#     print("No")

# 25314. 코딩은 체육과목입니다.

# N = int(input())
#
# for i in range(N//4):
#     words = [('long ')*(i+1), 'int']
#
# print(*words, sep='')
# # 다른 풀이
# n = int(input())
# answer = 'int'
# for i in range(n//4):
#     answer = 'long ' + answer
# print(answer)
# # 다른 풀이 2
# print(int(input())//4*'long ' + 'int')

# 15552. 빠른 A+B
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# T = int(input())
#
# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A+B)

# 11021. A+B-7
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# T = int(input())
#
# for tc in range(1, T+1):
#     A, B = map(int, input().split())
#     print(f'Case #{tc}: {A+B}')

# 11021. A+B-8
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# T = int(input())
#
# for tc in range(1, T+1):
#     A, B = map(int, input().split())
#     print(f'Case #{tc}: {A} + {B} = {A+B}')

# 2438. 별 찍기 -1
# N = int(input())
#
# for i in range(1, N+1):
#     stars = '*'*i
#     print(stars)

# 2439. 별 찍기 -2
# N = int(input())
#
# for i in range(1, N+1):
#     stars = ' '*(N-i) + '*'*i
#     print(stars)

# 10951. A+B -4
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break
# 다른 풀이
# https://kevinitcoding.tistory.com/entry/%EB%B0%B1%EC%A4%80Python-10951%EB%B2%88-AB-4-%EB%AC%B8%EC%A0%9C

#