# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# 강사님 풀이

# 현재값과 최신값을 비교한다 --> 스택 활용하기

# 다른 언어의 경우 배열 사이즈가 필요하다.
# 하지만 파이썬은 필요없음!

# 1.그림 2.구현 3.검증(디버깅)
for test_case in range(1, 11):
    arr = input().split()
    stack = []

    for num in arr[1]:
        # 스택이 비어있다면
        # if not stack:
        # if stack == []:
        if len(stack) == 0:
            # stack 에 쌓아준다
            stack.append(num)
        else:
            # 최신 값과 현재 값이 같다면 pop
            if num == stack[-1]:
                stack.pop()
            # 다르다면 append
            else:
                stack.append(num)
    print(f"#{test_case} {''.join(stack)}")
