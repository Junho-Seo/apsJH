# check: https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# import sys
# input = sys.stdin.readline
#
#
# def balance(word):
#     stack = []
#     if word == '.':  # . 이 들어오면 종료
#         return
#
#     for i in word:
#         if i == '(' or i == '[':
#             stack.append(i)
#         elif i == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#         elif i == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#
#     if not stack:
#         print('yes')
#     else:
#         print('no')
#
# while True:
#     PS = str(input().rstrip())
#     if not PS:
#         break
#     balance(PS)

# gpt 최적화
import sys
input = sys.stdin.readline


def balance(word):
    stack = []

    for i in word:
        # 여는 괄호는 스택에 추가
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            # 스택의 마지막이 '(' 일 때만 짝을 이루고 pop
            if stack and stack[-1] == '(':
                stack.pop()
            # 짝이 안 맞으면 False
            else:
                return False
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

    # 스택이 비어있다면 모든 괄호가 짝을 이룸 (True)
    return len(stack) == 0


while True:
    PS = input().rstrip()
    # '.'이 들어오면 종료
    if PS == '.':
        break

    # 균형 여부 확인
    if balance(PS):
        print('yes')
    else:
        print('no')