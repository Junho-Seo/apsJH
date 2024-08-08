import sys
sys.stdin = open('input.txt', 'r')


def infix_to_postfix(str):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}  # 연산자 우선 순위
    result = []     # 후위 표기법 연산 결과 저장 리스트
    operators = []  # 연산자를 저장할 스택

    for token in str:
        # 숫자라면 결과에 추가
        if token.isdigit():
            result.append(token)
        # 여는 괄호는 연산자 리스트에 추가
        elif token == '(':
            operators.append(token)
        # 닫는 괄호라면, 여는 괄호(우선 순위가 가장 높은 연산자) 를 찾을 때 까지 반복하면서
        # 1. 연산자 배열에서 꺼내기
        # 2. 여는 괄호가 아니라면 결과 리스트에 추가
        #   -> 순서가 확정되었다는 의미
        elif token == ')':
            top_token = operators.pop()
            while top_token != '(':
                result.append(top_token)
                top_token = operators.pop()
        # 연산자라면
        # 우선 순위가 높거나 같은 연산자들을 꺼내서 결과 리스트에 추가
        # -> 현재 연산자보다 우선순위가 높거나 같으면 계산 순서가 확정된다는 의미
        # 반복후에 연산자 배열에 현재 연산자 추가
        else:
            while operators and priority[operators[-1]] >= priority[token]:
                result.append(operators.pop())
            operators.append(token)

    while operators:
        result.append(operators.pop())

    return result


def cal_postfix(tokens):
    stack = []

    for token in tokens:
        # 숫자라면 stack 에 append
        if token.isdigit():
            stack.append(int(token))
        else:
            # 연산이 안된다면 -1
            if len(stack) < 2:
                return 'error'

            # 1. 숫자 2개 꺼내서 연산
            # 2. 연산 결과를 stack 에 추가
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 // num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    tokens = input().strip()
    formula = infix_to_postfix(tokens)
    # print(f"#{tc} {''.join(formula)}")
    result = cal_postfix(formula)
    print(f'#{tc} {result}')