# 2001. 파리 퇴치
# 참조. https://dev-astra.tistory.com/462

T = int(input())        # test case 개수
for test_case in range(1, T+1):
    # NxN 배열의 파리 영역
    # MxM 배열의 파리채
    N, M = list(map(int, input().split()))
    # 파리 영역 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리 영역 배열(NxN)을 파리채 영역(MxM)으로 순회하면서 합이 가장 큰 배열 탐색
    max_fly = 0        # 잡은 파리 합의 최대값
    for i in range(N-M+1):
        for j in range(N-M+1):

            sum_fly = 0           # 잡은 파리의 합
            for k in range(M):
                for l in range(M):
                    sum_fly += arr[i+k][j+l]
            if max_fly <= sum_fly:
                max_fly = sum_fly

    print(f'#{test_case} {max_fly}')