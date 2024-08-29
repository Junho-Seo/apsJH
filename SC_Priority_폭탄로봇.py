# 건이와 성재의 폭탄 설치 로봇 D3

'''
로봇을 사용하여 땅에 폭탄을 설치하고 터트려보려 합니다.


로봇에 입력할 수 있는 명령어는 다음과 같습니다.



[B] [Y] [X] : 폭탄 설치
[B]는 폭탄의 ID 를 의미합니다.
ID는 1 이상의 값으로 배정됩니다.
[B]번 폭탄 하나를 땅 Y, X 좌표에 설치합니다.

숫자 0 : 폭파
폭파 가능한 폭탄 중 가장 낮은 번호의 폭탄 하나를 터트립니다.
폭탄이 터지면 설치된 위치와 십자로 인접한 곳까지, 총 다섯 곳에 폭발이 일어납니다.



폭탄이 터진 장소는 끊임없이 불타오르게 됩니다.
그리고 불타는 땅에 설치된 폭탄은 즉시 고장 납니다.
고장 난 폭탄은 결코 터지지 않습니다.

그 후, 불타오르는 곳에도 폭탄을 설치할 수 있습니다.
다만, 이 폭탄은 설치 즉시 고장이 나며 결코 터지지 않습니다.

1,000 x 1,000 크기의 실험 공간에서 폭탄 설치 로봇의 명령어가 주어졌을 때,


터진 폭탄의 번호를 출력하는 프로그램을 제작해주세요.



[유의사항]


1. 폭탄 번호(ID)는 고유의 값을 가집니다. 같은 번호를 가진 폭탄은 없습니다.

2. 동일한 위치에 여러 개의 폭탄을 설치할 수 있습니다.

[입력]

첫 번째 줄에는 테스트 케이스의 수 T (1 <= N <= 4) 가 주어집니다.

각 테스트 케이스의 첫 번째 줄에는 폭탄 설치 명령어의 수(N)과 폭파 명령어의 수(M)이 주어집니다. (1 <= N, M <= 100,000)

그 후 총 N + M개의 줄에 걸쳐, 폭탄 설치 및 폭파 명령어가 입력됩니다.

폭탄 설치 명령어는 B Y X의 형태로 주어집니다. (0 < B <= 1,000,000)

이는 (Y, X) 위치에 B번의 폭탄을 설치함을 의미합니다. (0 <= Y, X < 1,000)


폭파 명령어는 0 으로 입력됩니다.

설치되어 터질 수 있는 폭탄 중, 가장 작은 번호의 폭탄을 터트립니다.

[출력]

폭파 명령어가 주어질 때 마다 폭파 된 폭탄의 번호를 테스트 케이스 번호와 함께 공백으로 구분하여 출력합니다.

만약 폭파 명령어를 수행했지만, 터질 폭탄이 없는 경우 -1을 출력합니다.

아래 코드는 위 문제의 정답코드야. 이해하기 쉽게 한글 주석을 상세히 작성해줘
'''

# bomb_id의 앞부터 순서대로 탐색.
# 0이 나오면 그 이전의 숫자들 중 가장 작은 숫자의 폭탄을 폭파
# 폭파된 좌표 + 십자로 한 칸씩 방문체크
# 방문체크된 좌표의 폭탄은 불발
# 탐색 반복

import sys
sys.stdin = open("input폭탄로봇.txt", "r")
sys.stdout = open("output폭탄로봇.txt", "w")


# di = [0, -1, 0, 1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     # 폭탄 번호
#     bomb_id = []
#     # 폭탄의 좌표
#     graph = [[] for _ in range(N+M+1)]
#     # 장소 리스트
#     ground = [[0]*1000 for _ in range(1000)]
#
#     for i in range(N+M):
#         arr = list(map(int, input().split()))
#
#         bomb_id.append(arr[0])
#         if bomb_id[i] != 0:
#             graph[bomb_id[i]].append(arr[1])
#             graph[bomb_id[i]].append(arr[2])
#
#     print(bomb_id)
#     print(graph)
#---------------------------------------------
# import heapq
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     # 실험공간 리스트
#     # 초기 값 0
#     place = [[0] * 1000 for _ in range(1000)]
#
#     # 방향 벡터
#     di = [1, -1, 0, 0]
#     dj = [0, 0, 1, -1]
#
#     # 폭탄 관리용 최소 힙
#     heap = []
#     for _ in range(N + M):
#         arr = list(map(int, input().split()))
#         # 폭탄인 경우
#         if arr[0]:
#             # 이미 불타고 있는 곳이라면 설치하지 않는다
#             if place[arr[1]][arr[2]] == -1:
#                 continue
#             # 최소 힙에 폭탄 정보 추가
#             heapq.heappush(heap, arr)
#             print(heap)
#             # 설치 위치에 폭탄 ID 기록
#             place[arr[1]][arr[2]] = arr[0]
#         # 폭파 명령어인 경우
#         else:
#             # 터질 수 있는 폭탄이 없으면 -1 출력
#             if not heap:
#                 print(f'#{tc} -1')
#                 continue
#             # 터질 수 있는 가장 작은 번호의 폭탄을 힙에서 꺼낸다
#             a, y, x = heapq.heappop(heap)
#             print(heap)
#             # 만약 꺼낸 폭탄이 이미 불타는 곳에 설치됐다면
#             # 폭파 가능한 폭탄이 나올 때까지 반복
#             while heap and place[y][x] == -1:
#                 if not heap:
#                     print(f'#{tc} -1')
#                     continue
#                 a, y, x = heapq.heappop(heap)
#                 print(heap)
#
#             # 터진 폭탄 번호 출력
#             print(f'#{tc} {a}')
#
#             # 폭탄이 터진 위치를 0에서 -1로 변경
#             place[y][x] = -1
#             # 인접 좌표도 -1로 변경
#             for k in range(4):
#                 ni = y + di[k]
#                 nj = x + dj[k]
#                 # 실험 공간 범위 확인
#                 if 0 <= ni < 1000 and 0 <= nj < 1000:
#                     place[ni][nj] = -1
#-----------------------------------------------
import heapq

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ground = [[0] * 1000 for _ in range(1000)]

    di = [0, 0, -1, 0, 1]
    dj = [0, 1, 0, -1, 0]

    heap = []

    for _ in range(N + M):
        arr = list(map(int, input().split()))
        # 폭탄인 경우
        if arr[0]:
            # 폭탄 정보 추출
            bomb_id, y, x = arr
            # 이미 불타는 곳에는 설치하지 않는다
            # 불타는 곳은 -1로 표시
            if ground[y][x] == -1:
                continue
            # 최소 힙에 폭탄 정보 추가
            heapq.heappush(heap, (bomb_id, y, x))
            # 설치된 위치에 폭탄 번호 기록
            ground[y][x] = bomb_id
        # 폭파 명령어인 경우
        else:
            # 폭탄이 없다면 -1 출력
            if not heap:
                print(f'#{tc} -1')
                continue
            # 폭탄이 있다면 힙에서 꺼낸다
            while heap:
                bomb_id, y, x = heapq.heappop(heap)
                # 폭파가 가능한 위치라면 해당 폭탄을 터트린다
                if ground[y][x] != -1:
                    print(f'#{tc} {bomb_id}')
                    # 해당 위치와 인접 좌표를 불타는 상태로 변경
                    for k in range(5):
                        ni = y + di[k]
                        nj = x + dj[k]
                        # 실험공간의 범위이면서 아직 불타지 않는 경우에만 변경
                        if 0 <= ni < 1000 and 0 <= nj < 1000 and ground[ni][nj] != -1:
                            ground[ni][nj] = -1
                    break
            # 힙에서 꺼낸 모든 폭탄의 좌표가 이미 불타고 있는 경우 -1 출력
            else:
                print(f'#{tc} -1')