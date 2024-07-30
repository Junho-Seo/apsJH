# SWEA solving club DAT 삼성 시의 버스 노선
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    # 수를 세야 한다. or 있는지 없는지 여부 체크 ==> 대부분 DAT로 접근 가능
    counts = [0] * 5001     # 1~5000 번의 정류장에 '지나가는 노선 수'를 저장할 리스트
    N = int(input())

    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for num in range(Ai, Bi + 1):
            counts[num] += 1

    # print(counts[:10])
    result = []
    P = int(input())
    for _ in range(P):
        target = int(input())
        result.append(counts[target])

    print(f'#{test_case}', *result)


# 버스 정류장에는 1~5000 번호 부여
# 버스 노선은 N개
# i번째 버스 노선은 번호가 Ai 이상, Bi 이하인 모든 정류장만을 다닌다.
#   i = 5 -> A5 ~ B5
# P개의 버스정류장에 대해 각 정류장에 몇 개의 노선이 다니는가?

# 정수 N 입력 : 버스 노선의 개수
# N개의 줄의 i번째 줄 > 두 정수가 공백 하나로
# 다음 줄에는 하나의 정수P