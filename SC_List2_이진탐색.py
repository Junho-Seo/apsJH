# 21531 . [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2

# 이진 탐색
def bin_search(left, right, target, cnt=0):
    # 검색 범위를 초과한 경우 종료
    if left > right:
        return cnt
    cnt += 1  # 이진 탐색 횟수 증가
    mid = int((left + right) / 2)
    # 목표 페이지를 찾은 경우 종료
    if mid == target:
        return cnt
    elif mid < target:
        return bin_search(mid, right, target, cnt)
    else:
        return bin_search(left, mid, target, cnt)


# A와 B의 탐색 횟수 계산
def game_cnt(P, A, B):
    cnt_A = bin_search(1, P, A)
    cnt_B = bin_search(1, P, B)

    # 결과 비교
    if cnt_A < cnt_B:
        return "A"
    elif cnt_B < cnt_A:
        return "B"
    else:
        return "0"


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    result = game_cnt(P, A, B)
    print(f'#{tc} {result}')

