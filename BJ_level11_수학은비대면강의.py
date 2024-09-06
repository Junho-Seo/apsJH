# 단계별 풀어보기 11. 브루트포스
# 19532 수학은 비대면 강의입니다.
# check 반복문을 이용한 브루트 포스 풀이

a, b, c, d, e, f = map(int, input().split())

# 방정식 풀이
# x = (b*f-c*e)/(b*d-a*e)
# y = (a*f-d*c)/(a*e-b*d)
#
# print(int(x), int(y))

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)