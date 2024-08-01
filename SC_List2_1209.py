# 1209. [S/W 문제해결 기본] 2일차 - Sum
import sys
sys.stdin = open("input1209.txt", "r")
sys.stdout = open("output1209.txt", "w")

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]

    sum_row = [0]*100
    sum_col = [0]*100
    sum_leftdia = 0
    sum_rightdia = 0

    for i in range(100):
        sum_leftdia += arr[i][i]
        sum_rightdia += arr[i][100-i-1]
        for j in range(100):
            sum_row[j] += arr[i][j]
            sum_col[j] += arr[j][i]

    total = sum_row + sum_col + [sum_leftdia] + [sum_rightdia]

    max_value = total[0]
    for value in total:
        if value > max_value:
            max_value = value

    print(f'#{test_case} {max_value}')
    # 각 합들을 하나의 리스트에 담은 후
    # 비교 정렬하여 최댓값
