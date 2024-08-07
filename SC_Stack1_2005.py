# 2005. 파스칼의 삼각형

# https://devlibrary00108.tistory.com/280
test = int(input())
for test in range(1, test+1):
    n = int(input())
    pascal = [[] for _ in range(n)]
    pascal[0].append(1)                     # 첫 열은 1
    for i in range(1, n):                    # 2열부터 반복
        stack = pascal[i-1][:]              # stack에 i-1열을 복사
        pascal[i].append(1)                 # 모든 열의 첫 인자는 1
        for j in range(1, i):
            pascal[i].append(stack.pop()+stack[-1])
            # 파스칼 삼각형의 대칭성을 이용
            # 다음 인자부터는 stack(i-1열)의 [pop(i) + i-1번째 인자]를 i열에 순차적으로 삽입
        pascal[i].append(1)             # 모든 열의 마지막 인자는 1

    print(f'#{test}')
    for ans in pascal:
        print(*ans)

# 스택 아닌 방법도 찾아보기
