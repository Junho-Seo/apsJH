T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bit = input()

    max_v = 1
    for i in range(1, N-1):
        j = 1
        while 0<=i-j and i+j<N and bit[i-j]==bit[i+j]:
            j += 1              # 중심원소 i주변으로 비교할 위치
        if max_v < (j-1)*2+1:   # 실패한 위치를 제외하고 양쪽(*2)+중심원소(+1)
            max_v = (j-1)*2+1
    print(f'#{tc} {max_v}')