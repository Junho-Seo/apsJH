# 1979 .어디에 단어가 들어갈 수 있을까 D2

def checker(N, K, arr):
    cnt = 0  # K만큼 연속된 단어 수 확인
    # 가로와 세로 동시에 검사
    for i in range(N):
        row = col = 0
        for j in range(N):
            # 가로 검사
            if arr[i][j] == 1:  # 해당 칸이 흰 칸이면
                row += 1  # row += 1 하여 연속성 확인
            else:  # 해당 칸이 검은 칸이면
                if row == K:  # row가 K를 충족하면 cnt + 1
                    cnt += 1
                row = 0  # 연속성이 끊어지면 row 초기화
            # 세로 검사
            if arr[j][i] == 1:
                col += 1
            else:
                if col == K:
                    cnt += 1
                col = 0
        # 반복문 종료 시점에서 연속된 K가 있는지 검사
        # 가로 검사
        if row == K:
            cnt += 1
        # 세로 검사
        if col == K:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    result = checker(N, K, arr)
    print(f'#{tc} {result}')
