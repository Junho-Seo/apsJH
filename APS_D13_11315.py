# 11315. 오목 판정
# 여러 형태의 input

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]


def f(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j  # 돌인지 확인할 위치
                while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    ni += di[k]
                    nj += dj[k]
    return 'NO'     # 모든 자리 i, j에서 모든 방향 k에 대해 실패하면


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 오목판 크기
    arr = [input() for _ in range(N)]
    ans = f(N)
    print(f'#{tc} {ans}')