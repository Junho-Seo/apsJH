# 10870. 개수 세기

# T = int(input())
# arr = list(map(int, input().split()))
# v = int(input())
#
# cnt = 0
#
# for i in range(T):
#     if arr[i] == v:
#         cnt += 1
# print(cnt)

# 10871. X보다 작은 수

# N, X = map(int, input().split())
# arr = list(map(int, input().split()))
#
# ans = []
#
# for i in range(N):
#     if arr[i] < X:
#         ans.append(arr[i])
#
# print(*ans, sep=' ')

# 10818	 최소, 최대

# N = int(input())
# arr = list(map(int, input().split()))
# # 시간 초과
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# print(f'{arr[0]} {arr[N-1]}')
# # 통과
# print(min(arr), max(arr))

# 2562	 최댓값

# arr = [0]*10
#
# for i in range(1, 10):
#     arr[i] = int(input())
#
# print(max(arr))
# print(arr.index(max(arr)))

# 10810	 공 넣기

# # 바구니 개수 N개 (1~N), 공 넣는 횟수(M)
# # 바구니에는 공 1개만.
#
# N, M = map(int, input().split())
# ball_info = [list(map(int, input().split())) for _ in range(M)]
#
# basket = [0]*(N)
#
# for i in range(M):
#     a, b, c = ball_info[i][0], ball_info[i][1], ball_info[i][2]
#     for j in range(a-1, b):
#         basket[j] = c
#
# print(*basket)

# 10810	 공 바꾸기

# 바구니 개수 N개 (1~N), 공 바꾸는 횟수(M)
# 바구니 2개 선택 후 교환

# N, M = map(int, input().split())
# ball_info = [list(map(int, input().split())) for _ in range(M)]
#
# basket = list(range(1, N+1))
#
# for i in range(M):
#     a, b = ball_info[i][0], ball_info[i][1]
#     basket[a-1], basket[b-1] = basket[b-1], basket[a-1]
#
# print(*basket)

# 5597	 과제 안 내신 분..? check
# att_list = list(range(1,31))
#
# for _ in range(28):
#     students = int(input())
#     att_list.remove(students)
#
# for i in range(len(att_list)):
#     print(att_list[i])

# 3052	 나머지 check
# set을 사용하면 if문 삭제 가능하나 순서가 섞인다.
# print(len(set(arr)))
# arr =[]
# for _ in range(10):
#     nums = int(input())
#     if nums%42 not in arr:
#         arr.append(nums%42)
#
# print(len(arr))

# 10811	 바구니 뒤집기 check
# N, M = map(int, input().split())
#
# basket = list(range(1, N+1))
# temp = 0
#
# for _ in range(M):
#     a, b = map(int,input().split())
#     temp = basket[a-1:b]
#     temp.reverse()
#     basket[a-1:b] = temp
#
# print(*basket)
# 참고풀이
# n,m = map(int, input().split())
# basket = [i for i in range(1,n+1)]
# temp = 0
# for x in range(m):
#   i,j = map(int, input().split())
#   temp = basket[i-1:j]
#   temp.reverse()
#   basket[i-1:j] = temp
#
# for x in range(n):
#   print(basket[x],end=" ")

# 1546	 평균
N = int(input())  # 과목 수
scores = list(map(int, input().split()))
ans = [0]*N

for i in range(N):
    ans[i] = (scores[i] / max(scores))*100

print(sum(ans)/len(ans))
# 다른 풀이
# N = int(input())  # 과목 수
# scores = list(map(int, input().split()))
#
# sum = 0
#
# for i in range(N):
#     A = (scores[i]/max(scores))*100
#     print(A)
#     sum = sum+A
# print(scores)
# print(sum/N)