# 27866	 문자와 문자열

# S = input()
# i = int(input())
# print(S[i-1])

# 2743	 단어 길이 재기

# S = input()
# print(len(S))

# 9086	 문자열

# T = int(input())
#
# for _ in range(T):
#     word = input()
#     print(word[0], word[-1], sep='')

# 11654	 아스키 코드
# print(ord(input()))

# 11720	 숫자의 합
# N = int(input())
# nums = list(map(int, input()))
# result = 0
#
# for i in range(N):
#     result += nums[i]
#
# print(result)

# 10809	 알파벳 찾기
# # check
# S = input()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabet)
# for i in alphabet:
#     if i in S:
#         print(S.index(i), end=' ')
#     else:
#         print(-1, end=' ')
# # 다른 풀이
# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(x), end = ' ')

# 2675	 문자열 반복
# # check
# T = int(input())
# for tc in range(1, T+1):
#     R, S = input().split()
#     for i in S:
#         print(i*int(R), end='')
#     print()

# 1152	 단어의 개수
# # check
# sentence = input().split()
# print(len(sentence))

# 2908	 상수
# # check
# A, B = input().split()
# rev_A = ''.join(reversed(A))
# rev_B = ''.join(reversed(B))
#
# if rev_A > rev_B:
#     print(rev_A)
# else:
#     print(rev_B)
# # 다른 풀이
# A, B = input().split()
# A = int(A[::-1])
# B = int(B[::-1])
#
# if A > B:
#     print(A)
# else:
#     print(B)


# 5622	 다이얼
# # check
# words = input()
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# times = 0
#
# for i in range(len(words)):
#     for j in dial:
#         if words[i] in j:
#             times += dial.index(j)+3
# print(times)

# 11718	 그대로 출력하기
# # check
# for i in range(100):
#     print(input(), sep='\n')  # 오답
# 다른 풀이
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
# 다른 풀이 2
# import sys
#
# while True:
#   s = sys.stdin.readline().rstrip()
#   if s == '':
#     break
#   else:
#     print(s)