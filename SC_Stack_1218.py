# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
# 참조. https://velog.io/@bmlsj/SWEA-1218.-SW-문제해결-기본-4일차-괄호-짝짓기

for test_case in range(1, 11):
    N = int(input())
    arr = input()
    brakets = {'[':']', '{':'}', '(':')', '<':'>'}
    stack = []
    ans = 1

    for i in arr:
        if i in brakets.keys():     # i가 brakets 의 key 라면
            stack.append(i)         # stack에 넣는다.
        else:                       # 좌측 괄호(keys)가 아닐 경우
            if brakets[stack[-1]] == i:     # i가 brakets에서 stack의 마지막 값을 key 로 가진 value 와 같다면
                stack.pop()                 # stack의 마지막 값을 꺼낸다.
            else:       # 그 외의 경우
                ans = 0     # 유효하지 않다.

    print(f'#{test_case} {ans}')

    # for i in arr[0]:
    #     if i == '(':
    #         stack.append(i)
    #     elif i == ')' and len(stack):
    #         if '(' not in stack:
    #             stack.pop(stack.index('('))
    #         else:
    #             ans = 1
    #
    #     if i == '[':
    #         stack.append(i)
    #     elif i == ']' and len(stack):
    #         if '[' not in stack:
    #             stack.pop(stack.index('['))
    #         else:
    #             ans = 1
    #
    #     if i == '{':
    #         stack.append(i)
    #     elif i == '}' and len(stack):
    #         if '{' not in stack:
    #             stack.pop(stack.index('{'))
    #         else:
    #             ans = 1
    #
    #     if i == '<':
    #         stack.append(i)
    #     elif i == '>' and len(stack):
    #         if '<' not in stack:
    #             stack.pop(stack.index('<'))
    #         else:
    #             ans = 1
    #
    # print(f'#{test_case} {ans}')
