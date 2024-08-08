# 21686. 콜라츠 추측
'''
특정 자연수가 아래 과정을 거치면 무조건 1이 된다. (콜라츠 추측)
짝수 : 현재 수를 2로 나눈 몫
홀수 : 현재 수에 3을 곱하고, 그 수에 1을 더한 값

양수인 정수 N이 주어질 때 콜라츠 추측의 과정을 몇 번 거쳐야 1이되는지 구하는 프로그램을 작성하시오.

[입력]
첫번째 줄에 테스트 케이스의 수 T 가 주어집니다.
각 테스트 케이스의 첫 번째 줄에 양의 정수 N(1 ≤ N ≤ 10,000)이 주어집니다.

[출력]
N이 1이되는 콜라츠 추측의 과정 횟수를 출력합니다.
'''
# 반복문


def collatz(N):
    cnt = 0
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = (N * 3) + 1
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {collatz(N)}')


# 반복문 + 메모이제이션
memo = {}


def collatz_memo(N):
    if N in memo:
        return memo[N]
    cnt = 0
    original_N = N  # 원래의 N값 저장
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = (N * 3) + 1
        cnt += 1
        # 중간 과정의 N이 이미 memo에 있는 경우, 그 값을 이용해 cnt 업데이트
        if N in memo:
            cnt += memo[N]
            break
    # 계산된 과정 횟수를 메모에 저장
    memo[original_N] = cnt
    return cnt  # 총 과정 횟수 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {collatz_memo(N)}')


# 재귀 + 메모이제이션
memo = {}  # 메모이제이션용 딕셔너리 초기화


def collatz_rec(N):
    if N in memo:       # 이미 N이 메모에 있는 경우,
        return memo[N]      # 저장된 값 반환
    if N == 1:      # N이 1인 경우 0 반환
        return 0
    if N % 2 == 0:      # 짝수
        cnt = 1 + collatz_rec(N//2)
    else:       # 홀수
        cnt = 1 + collatz_rec(3 * N + 1)

    # 계산된 과정 횟수를 메모에 저장
    memo[N] = cnt
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc} {collatz_rec(N)}')
