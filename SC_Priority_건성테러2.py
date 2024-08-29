# 건이와 성재의 폭탄테러2 D3
'''
N x N 필드 지역에 폭탄을 설치 하였습니다.
폭탄은 제자리, 위, 아래, 왼쪽, 오른쪽 영역으로 터지게 됩니다.
번호 순서대로 폭탄을 설치했고, 1초에 하나씩 폭탄이 터집니다.
1 초가 되면, 1번 폭탄이 터집니다.

예시로 다음의 4x4 필드 지역이 주어진다고 봅시다.

16 14 1 8
5 10 7 3
13 2 9 6
12 11 4 15

1 번 폭탄에 의하여, 14, 8, 7 번 지역도 터졌으며, 그곳에 있는 폭탄은 사라지게 됩니다.
2 초가 되었고, 아직 2번 폭탄은 동작되고 있는 상태입니다.
10, 13, 9, 11, 2번 지역에 폭탄이 터지게 되었습니다.
3초가 되었고, 아직 3번 폭탄은 동작되고 있는 상태입니다.
3번과 6번 지역에 폭탄이 터지게 되었습니다.
4초가 되었고, 4번과 15번 지역에 폭탄이 터지게 되었습니다.
5초가 되었고, 5번과 16번 지역에 폭탄이 터지게 되었습니다.
12초가 될 때 까지, 아무런 폭탄이 터지지 않습니다.
그리고 12초가 되어 남은 지역까지 모두 폭탄이 터지게 되었습니다.

적군 필지에 모든 폭탄이 터질 때 까지 걸리는 시간을 구해 출력해 주세요.

[입력]

첫 줄에는 테스트 케이스의 수가 입력되며,
두 번째 줄에는 N이 입력되고,
그 다음 줄부터 N x N 사이즈의 폭탄 설치 정보가 입력됩니다.

(1 <= N <= 1,000)

[출력]

총 몇 초만에 모든 폭탄이 터지는지 구하여 출력해 주세요.


다음은 작성중인 코드인데 문제점을 알고 싶어. 수정본과 이해를 위한 상세한 한글 주석을 작성해줘.


'''


import heapq
import sys
sys.stdin = open("input건성테러2.txt", "r")
sys.stdout = open("output건성테러2.txt", "w")

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#
#     # 방향 벡터
#     di = [0, 0, -1, 0, 1]
#     dj = [0, 1, 0, -1, 0]
#
#     # 최대 힙
#     heap = []
#
#     for i in range(N):
#         for j in range(N):
#             # 번호가 적혀있다면
#             if arr[i][j]:
#                 while len(heap) != N*N:
#                     heapq.heappush(heap, -arr[i][j])
#                     print(heap)
#                     for k in range(5):
#                         ni = i + di[k]
#                         nj = j + dj[k]
#                         if -1 < ni < N and -1 < ni < N and arr[ni][nj] != 0:
#                             arr[ni][nj] = 0
#             # 번호가 없다면
#             else:
#                 print(f'#{tc} {-heap[0]}초')

# --------------------------------------------

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    di = [0, 0, -1, 0, 1]
    dj = [0, 1, 0, -1, 0]

    heap = []

    ans = 0

    # 힙에 폭탄 정보 추가 (시간, 좌표)
    for i in range(N):
        for j in range(N):
            heapq.heappush(heap, (arr[i][j], i, j))

    while heap:
        # 가장 먼저 터질(숫자가 가장 작은) 위치 추출
        time, i, j = heapq.heappop(heap)
        # 해당 위치에 폭탄이 있는지 확인
        if arr[i][j] == 0:
            continue
        # 마지막으로 터진 폭탄(시간) 갱신
        ans = time
        # 해당 위치에 인접한 위치도 폭파 처리
        for k in range(5):
            ni = i + di[k]
            nj = j + dj[k]
            if -1 < ni < N and -1 < nj < N and arr[ni][nj] != 0:
                arr[ni][nj] = 0

    print(f'#{tc} {ans}sec')