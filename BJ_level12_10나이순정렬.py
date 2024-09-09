N = int(input())
ordered = []

for _ in range(N):
    x, y = input().split()
    # 여기서 sort 전에 x를 int 처리하지 않아 반례 발생
    ordered.append([int(x), y])

ordered.sort(key=lambda x: x[0])

for i in ordered:
    print(i[0], i[1])

'''
int 처리 반례
입력
2
9 a
11 b

출력
11 b
9 a
'''