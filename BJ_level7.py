# 2738	 행렬 덧셈

# N, M = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# B = [list(map(int, input().split())) for _ in range(N)]
# ans = [[0]*M for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         ans[i][j] = A[i][j] + B[i][j]
#
# for i in ans:
#     for j in i:
#         print(j, end=' ')
#     print()

# 	2566	 최댓값

# arr = [list(map(int, input().split())) for _ in range(9)]
#
# max_val = -1
# row = 0
# col = 0
#
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] >= max_val:
#             max_val = arr[i][j]
#             row = i+1
#             col = j+1
#
# print(max_val)
# print(row, col)

# 10798	 세로읽기
# # check
# arr = [list(input()) for _ in range(5)]
#
# for j in range(15):
#     for i in range(5):
#         if j < len(arr[i]):
#             print(arr[i][j], end='')

# 2563	 색종이
# # check
# N = int(input())  # 색종이 개수
# paper = [[0]*100 for _ in range(100)]  # 도화지 초기화
# area = 0  # 총 넓이 초기화
#
# for _ in range(N):
#     ld, bd = map(int, input().split())
#     for i in range(bd, bd+10):  # 세로 탐색
#         for j in range(ld, ld+10):  # 가로 탐색
#             paper[i][j] = 1     # 색종이의 좌표를 1로 변경
#
# for i in range(100):    # 도화지 전체를 돌면서
#     area += paper[i].count(1)  # 1의 개수를 센다.
#
# print(area)
