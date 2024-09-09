# check: https://omins.tistory.com/34
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    PS = list(map(str, input().rstrip()))
    stack = []
    check = True

    for i in PS:
        # i가 여는 괄호일 때 stack에 넣는다
        if i == '(':
            stack.append('(')
        if i == ')':
            # i가 닫는 괄호일 때 stack(여는 괄호)이 있다면
            # 쌍을 이루므로 pop
            if stack:
                stack.pop()
            # i가 닫는 괄호일 때 stack이 없는 경우
            # 여는 괄호 없이 닫는 괄호가 있는 것이므로
            # check=False 저장 후 반복 종료
            elif not stack:
                check = False
                break
    # PS를 모두 검사 후
    # stack이 없고(모두 쌍을 이뤄 pop) check가 True면 YES 출력
    if not stack and check:
        print('YES')
    # stack(여는 괄호)이 남아있거나 check가 False면 NO 출력
    elif stack or not check:
        print('NO')
