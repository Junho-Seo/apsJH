# 2798	 블랙잭
# 브루트 포스
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            total = arr[i] + arr[j] + arr[k]
            if total <= M:
                # ans = max(total, ans)
                if total > ans:
                    ans = total

print(ans)






# 재귀를 이용한 코드

def blackjack(pick, start_idx, total):
    global ans
    # 카드 수의 합이 목표값보다 크면 종료
    if total > M:
        return
    # 3장을 뽑으면 종료
    if pick == 3:
        ans = max(ans, total)
        return
    # idx_list로 인한 인덱스 중복 체크를 방지한 개선코드
    # 현재 카드 선택 후 다음 카드로 이동
    for i in range(start_idx, N):   # start_idx부터 시작하여 중복 방지
        blackjack(pick+1, i+1, total+arr[i])    # 중복 방지를 위해 i+1을 넘김

    # for i in range(N):
    #     if i not in idx_list:
    #         idx_list.append(i)
    #         blackjack(pick+1, idx_list, total+arr[i])
    #         idx_list.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

# blackjack(0, [], 0)
blackjack(0, 0, 0)
print(ans)

