# 1330 두 수 비교하기

# A, B = map(int, input().split())
# if A > B:
#     print(">")
# if A < B:
#     print("<")
# if A == B:
#     print("==")

# 9498. 시험 성적

# score = int(input())
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# 2753. 윤년
# y = int(input())
#
# if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
#     print("1")
# else:
#     print("0")

# 14681. 사분면 고르기
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print("1")
# if x < 0 and y > 0:
#     print("2")
# if x < 0 and y < 0:
#     print("3")
# if x > 0 and y < 0:
#     print("4")

# 2884. 알람 시계
# H, M = map(int, input().split())
#
# if 0 < H <= 23:
#     if M > 45:
#         print(f"{H} {M-45}")
#     elif M == 45:
#         print(f"{H} {0}")
#     else:
#         print(f"{H-1} {60-(45-M)}")
# else:
#     if M > 45:
#         print(f"{H} {M-45}")
#     elif M == 45:
#         print(f"{H} {0}")
#     else:
#         print(f"{23} {60-(45-M)}")

# #다른 풀이
# h,m=  map(int,input().split())
# if m >= 45:
#     print(h, m-45)
# else:       # 분이 45보다 작을 때
#     m += 15     # 60분 주기에서 45분을 뺀 것 = 15분 더한 것
#     if h == 0:      # 시간 조정 및 예외처리
#         h = 23
#     else:
#         h -= 1
#     print(h, m)


# 2525. 오븐 시계
# A, B = map(int, input().split())
# C = int(input())
#
# A += C // 60
# B += C % 60
#
# if B >= 60:
#     A += 1
#     B -= 60
# if A >= 24:
#     A -= 24
#
# print(A, B)

