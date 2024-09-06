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



# 다른 풀이(gpt)
def sudoku(arr):
    # 각 가로줄, 세로줄, 3x3 서브그리드에 대해 중복 확인
    def is_valid_unit(unit):
        return len(unit) == len(set(unit))  # set으로 중복을 제거한 후 길이 비교

    # 가로 줄 확인
    for row in arr:
        if not is_valid_unit(row):  # 가로 줄에 중복이 있는지 확인
            return "0"

    # 세로 줄 확인
    for col in range(9):
        if not is_valid_unit([arr[row][col] for row in range(9)]):  # 세로 줄에 중복이 있는지 확인
            return "0"

    # 3x3 서브그리드 확인
    for i in range(0, 9, 3):  # 각 3x3 서브그리드의 시작 위치 설정
        for j in range(0, 9, 3):  # 각 3x3 서브그리드의 시작 위치 설정
            subgrid = [arr[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(subgrid):  # 서브그리드에 중복이 있는지 확인
                return "0"

    return "1"  # 모든 검사를 통과하면 1 반환


T = int(input())  # 테스트 케이스의 수 입력

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 퍼즐 입력
    result = sudoku(arr)  # 결과 계산
    print(f'#{tc} {result}')  # 결과 출력
