# 21454 . [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
# 성빈님 풀이

"""
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.



[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.



[입력]


첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )


[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

#1 3
#2 0
#3 4
"""

# # 코드1
# T = int(input())
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     arr = [0] * 101
#     for i in list(map(int, input().split())):
#         arr[i] = 1
#
#     position = 0
#     cnt = 0
#     while position + K < N:
#         j = K
#         while j > 0:
#             if arr[position + j]:
#                 position += j
#                 cnt += 1
#                 break
#             j -= 1
#         if j == 0:
#             cnt = 0
#             break
#     print(f'#{tc} {cnt}')
#
# # 코드2
# T = int(input())
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     num = 0
#     stop = 0
#     b_stop = stop + K
#     while b_stop < N:
#         next_stops = [x for x in arr if stop < x <= b_stop]
#         if len(next_stops) == 0:
#             num = 0
#             break
#         next_stop = next_stops[-1]
#         num += 1
#         stop = next_stop
#         b_stop = stop + K
#
#     print(f'#{tc} {num}')
#
# # 코드3
# t = int(input())
#
# for tc in range(1, t + 1):
#     k, n, m = map(int, input().split())
#     gas = list(map(int, input().split()))
#     stops = [0] * (n + 1)
#
#     for g in gas:
#         stops[g] = 1
#
#     start, end, cnt = 0, k, 0
#
#     while end < n:
#         for i in range(end, start, -1):
#             if stops[i]:
#                 start = i
#                 end = start + k
#                 cnt += 1
#                 break
#         else:
#             print(f'#{tc} 0')
#             break
#     else:
#         print(f'#{tc} {cnt}')

T = int(input())
for tc in range(1, T + 1):
    # K: 최대 이동 가능 정류장 수, N: 종점 정류장 번호, M: 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 번호를 집합으로 입력받는다.
    charge_stations = set(map(int, input().split()))

    position = 0  # 현재 위치를 초기화
    cnt = 0  # 충전 횟수를 초기화

    # 현재 위치에서 최대 이동 가능 거리 내에 종점이 있는지 확인
    while position + K < N:
        for j in range(K, 0, -1):
            if position + j in charge_stations:
                # 충전기가 있는 정류장으로 이동
                position += j
                cnt += 1  # 충전 횟수를 증가시킨다.
                break
        else:
            cnt = 0
            break
    # 결과 출력
    print(f'#{tc} {cnt}')