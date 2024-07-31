# 1209. [S/W 문제해결 기본] 2일차 - Sum

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    print(len(arr))
    sum_row = 0
    sum_col = 0
    sum_leftdia = 0
    sum_rightdia = 0

    for i in range(100):
        for j in range(100):
            sum_row += arr[i][j]
        print(sum_row)
    for i in range(101):
        for j in range(101):
            sum_col += arr[j][i]
    for i in range(101):
        sum_leftdia += arr[i][i]
    for i in range(101):
        sum_rightdia += arr[i][101-i-1]


    # 각 합들을 하나의 리스트에 담은 후
    # 비교 정렬하여 최댓값 출력 혹은 max
