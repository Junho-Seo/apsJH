# 6. 사칙연산

# A, B = map(int, input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# 7. ??!
# a = input()
# print(f"{a}??!")
# # print(a+"??!")

# 8. 1998년생인 내가 태국에서는 2541년생?!
# y = int(input())
# print(y-543)

# 9. 나머지
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print( ((A%C) * (B%C))%C)

# 2588. 곱셈
"""
map(int, input().split())로 a, b변수를 입력 받고 a를 b의 일의 자리부터 곱하여 출력합니다.
마지막은 a*b연산을 그대로 출력합니다. b를 기본 입력으로 받으면 String 타입으로 저장되는데,
String을 한 글자씩 떼어 Int로 변환하고 곱하면 % 연산을 쓰지 않고도 계산이 가능합니다.
"""
# # 문자열을 이용한 풀이(반복문X)
# A = int(input())    # 정수형
# B = input()     # 문자열
#
# print(A*int(B[2]))
# print(A*int(B[1]))
# print(A*int(B[0]))
# print(A*int(B))
#
# # 문자열을 이용한 풀이(반복문)
# A = int(input())    # 정수형
# B = input()     # 문자열
#
# for i in range(3, 0, -1):   # (2, -1, -1) , B[i] 로 해도 가능
#     print(A * int(B[i - 1]))
# print(A * int(B))
#
# # 산술 연산자를 이용한 풀이
# A = int(input())
# B = int(input())
#
# print(A * (B % 10))
# print(A * (B % 100 // 10))
# print(A * (B // 100))
# print(A * B)

# 11382. 꼬마 정민
# A, B, C = map(int, input().split())
# print(A+B+C)

# 10171. 고양이
# print("\\    /\\ ")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# 10172. 개
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\\__|")

