# SWEA solving club DAT 간단한 소인수분해

# 다 나눠봐야한다.
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

# while문 5번 사용한 방법
    # cnt_2 = 0
    # while N % 2 == 0:
    #     cnt_2 += 1
    #     N //= 2
    #
    # cnt_3 = 0
    # while N % 3 == 0:
    #     cnt_3 += 1
    #     N //= 3
    #
    # cnt_5 = 0
    # while N % 5 == 0:
    #     cnt_5 += 1
    #     N //= 5
    #
    # cnt_7 = 0
    # while N % 7 == 0:
    #     cnt_7 += 1
    #     N //= 7
    #
    # cnt_11 = 0
    # while N % 11 == 0:
    #     cnt_11 += 1
    #     N //= 11
    #
    # print(f'#{test_case} {cnt_2}, {cnt_3}, {cnt_5}, {cnt_7}, {cnt_11}')

    li = [2, 3, 5, 7, 11]
    counts = [0] * 5

    for i in range(5):
        while N % li[i] == 0:
            counts[i] += 1
            N //= li[i]
    print(f'#{test_case}', *counts)

#-------------------------------------------------------
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     # arr = list(map(int, input().split()))
# # 1. 주어진 N값을 11로 나눈다.
# #       나머지가 0일 경우 몫을 반환하여 다시 11로 나누는 것을 반복.
# #       나머지가 0이 아니거나 11보다 작을 경우 N을 그대로 반환.
# # 2. 1에서 받은 값을 7로 나눈다
# #       나머지가 0이 아니거나 7보다 작을 경우 받은 값을 그대로 반환
# # 3. 2까지 진행
#
#
#     print(f'#{test_case} { }')