# 단계별 풀어보기 11. 브루트포스
# 1018 체스판 다시 칠하기
# # 첫 풀이
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# N, M = map(int, input().split())
# arr = [list(input())for _ in range(M)]
# board = [[0]*8 for _ in range(8)]
# ans = []
#
# # 전체에서 8x8 범위 순회 후 확인할 보드 저장
# for i in range(M-7):
#     for j in range(N-7):
#         for k in range(i, 8):
#             for l in range(i, 8):
#                 board[k][l] = arr[i+k][j+l]
#
# cnt = 0  # 색칠한 칸의 수 카운팅 초기화
# for i in range(8):
#     for j in range(8):
#         # 인접 칸의 색을 확인하기 위한 델타 탐색
#         for d in range(4):
#             ny = i + dy[d]
#             nx = j + dx[d]
#             if 0 > ny or 8 <= ny or 0 > nx or 8 <= nx:
#                 continue
#             if board[i][j] == 'B':
#                 if board[ny][nx] == 'W':
#                     continue
#                 else:
#                     board[ny][nx] = 'W'
#                     cnt += 1
#             if board[i][j] == 'W':
#                 if board[ny][nx] == 'B':
#                     continue
#                 else:
#                     board[ny][nx] = 'B'
#                     cnt += 1
#         ans.append(cnt)
#
# print(min(ans))
'''
문제점:
1. 입력 배열 크기 문제:
arr 배열을 만들 때, M이 아닌 N개의 행이 있어야 합니다.
즉, 배열 arr은 N개의 행과 M개의 열로 구성됩니다.

2. 8x8 보드를 잘라내는 로직 오류:
board라는 배열을 8x8로 새로 생성해서 복사하는 로직이 올바르지 않습니다.
i와 j에서 시작하는 8x8 부분을 arr에서 직접 탐색해야 합니다.
board는 따로 생성할 필요가 없습니다.

3. 잘못된 델타 탐색 로직:
현재 코드에서는 인접한 4개의 칸(dy, dx를 사용)만 확인하고 색을 바꿔주는 방식을 사용하고 있는데,
이 방식은 체스판이 검은색과 흰색이 번갈아 나와야 하는 규칙을 제대로 구현하지 못합니다.
체스판은 고정된 패턴이므로 규칙에 맞는 두 가지 패턴을 사용하여 직접 비교해야 합니다.

4. 색을 교체하는 방식 오류:
색을 교체하는 것이 아니라, 현재 상태와 두 가지 패턴 중 하나를 비교해
변경해야 하는 칸의 수를 계산해야 합니다.
'''


# GPT 수정 + 최적화
# 1. 반복되는 계산 줄이기
#   - 패턴 정의 대신 매번 패턴을 비교할 때마다 직접 색을 계산한다.
#   - 즉, 탐색하며 색이 맞는지 확인할 때, 기준이 되는 좌상단 색만 확인하고
#     그 기준에 맞게 위치에 따라 어떤 색이 나와야하는지 계산한다.
# 2. 입력이 매우 큰 경우 효율적인 비교 방법
#   - 최적화를 위해 누적 합을 사용할 수 있지만, 이 문제에서는 별다른 중복 계산이
#     발생하지 않기 때문에 해당 방식보다는 현재 방식이 효율적이다.
#   - 다만, 다시 칠해야 하는 칸을 계산하는 과정을 2중 반복문으로 간소화하고
#     패턴을 직접 정의하지 않는 방식으로 최적화한다.

# 최적화 포인트
# 패턴을 미리 저장하지 않고, 현재 좌표와 색에 따라 패턴을 실시간으로 계산

N, M = map(int, input().split())
arr = [input() for _ in range(N)]


def count_repaints(x, y):
    count1 = 0  # 좌상단이 'W'로 시작하는 패턴에 맞추기 위한 다시 칠하기 횟수
    count2 = 0  # 좌상단이 'B'로 시작하는 패턴에 맞추기 위한 다시 칠하기 횟수

    # 8x8 부분을 순회하며 다시 칠해야 하는 칸 계산
    for i in range(8):
        for j in range(8):
            # 현재 칸의 색이 어떻게 되어야 하는지 계산
            if (i + j) % 2 == 0:  # 좌상단과 같은 색이어야 하는 칸 (i+j가 짝수인 칸)
                if arr[x + i][y + j] != 'W':  # 'W'로 시작하는 체스판과 비교
                    count1 += 1
                if arr[x + i][y + j] != 'B':  # 'B'로 시작하는 체스판과 비교
                    count2 += 1
            else:  # 좌상단과 반대 색이어야 하는 칸
                if arr[x + i][y + j] != 'B':  # 'W'로 시작하는 체스판과 비교
                    count1 += 1
                if arr[x + i][y + j] != 'W':  # 'B'로 시작하는 체스판과 비교
                    count2 += 1

    # 두 패턴 중 최소 칠하기 횟수를 반환
    return min(count1, count2)


min_repaints = float('inf')  # 무한대 저장 (매우 큰 임의의 수)

# 8x8 부분을 순회하며 다시 칠하기 횟수 계산
for i in range(N - 7):
    for j in range(M - 7):
        repaints = count_repaints(i, j)
        min_repaints = min(min_repaints, repaints)

# 최소 다시 칠하기 횟수 출력
print(min_repaints)

#------------------------------------------------------
# 누적 합 기법 적용 풀이

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# 하나의 누적합 배열만 사용
prefix = [[0] * (M + 1) for _ in range(9)]  # 9행 크기의 누적합 배열

min_repaints = float('inf')

# 8x8 크기의 영역에 대해 누적합 계산
for i in range(N - 7):
    for j in range(M - 7):
        count_W = 0  # 'W'로 시작하는 패턴에 맞추기 위한 다시 칠하기 횟수
        count_B = 0  # 'B'로 시작하는 패턴에 맞추기 위한 다시 칠하기 횟수

        # 슬라이딩 윈도우로 8x8 크기의 영역 탐색
        for x in range(8):
            for y in range(8):
                # 예상 패턴에 따른 계산
                expected_W = 'W' if (x + y) % 2 == 0 else 'B'
                expected_B = 'B' if (x + y) % 2 == 0 else 'W'

                if arr[i + x][j + y] != expected_W:
                    count_W += 1
                if arr[i + x][j + y] != expected_B:
                    count_B += 1

        # 다시 칠해야 하는 최소 칸 수 갱신
        min_repaints = min(min_repaints, count_W, count_B)

print(min_repaints)


