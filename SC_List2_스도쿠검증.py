# 1974 . 스도쿠 검증

def sudoku(arr):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            # 가로 검사
            row[arr[i][j]] += 1
            if row[arr[i][j]] == 2:
                return '0'
            # 세로 검사
            col[arr[j][i]] += 1
            if col[arr[j][i]] == 2:
                return '0'

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_arr = [0] * 10
            for k in range(3):
                for l in range(3):
                    sub_arr[arr[i+k][j+l]] += 1
                    if sub_arr[arr[i+k][j+l]] == 2:
                        return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku(arr)
    print(f'#{tc} {result}')