# 1865. 동철이의 일 분배 D4


# dfs+백트래킹
# 직원 번호(행 번호), 일 번호(열 번호) 리스트, 현재 확률
def dfs(members, items, total):
    global ans
    # 현재 확률이 최대 확률보다 작으면 종료 (가지치기)
    if total <= ans:
        return

    # 모든 직원이 일을 가진 경우
    if members == N:
        # ans와 total을 비교하여 큰 값을 ans에 저장 후 종료
        ans = max(ans, total)
        return

    # 일 번호를 직원 수만큼 탐색
    for i in range(N):
        # 해당 일 번호가 items에 없다면
        if i not in items:
            # items에 일 번호 추가
            items.append(i)
            # 재귀 호출
            # 다음 직원, 일 번호 리스트, 현재 성공률*해당 일의 성공률
            dfs(members+1, items, total*(done_rate[members][i]/100))
            # 기저 조건에 따라 탐색이 종료되면 items의 마지막 요소 제거(dfs)
            items.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    done_rate = [list(map(int, input().split()))for _ in range(N)]
    ans = 0

    dfs(0, [], 1)
    print(f'#{tc} {round(ans*100, 6):.6f}')



