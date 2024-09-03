# 1486 .장훈이의 높은 선반 D4
# N명으로 탑을 쌓는 조합
# 점원 순서 선택 기준과 점원의 키는 연관이 없다 => 완전 탐색
# 신경쓰지 않아도 되는 부분은 없는가 => 백트래킹(가지치기)

# shelf => 특정 시점에 필요한 값
# ans => 전체 재귀함수가 공유 -> global 선언
def perm(member, shelf):
    global ans
    # 이미 탑의 높이가 B 이상이면 더이상 확인할 필요가 없다
    if shelf > B:
        # B 이상인 값중 최소 탑의 높이를 저장
        ans = min(ans, shelf)
        return
    # 모든 점원이 탑을 쌓는데 고려가 되었다면
    if member == N:
        return

    # 재귀 호출
    # member 번 점원을 탑에 쓴다
    perm(member+1, shelf + H_list[member])
    # 안 쓴다.
    perm(member+1, shelf)
T = int(input())

for tc in range(1,T+1):
    N, B = map(int, input().split())
    H_list = list(map(int,input().split()))
    S = sum(H_list)
    ans = 1e9
    perm(0, 0)
    print(f'#{tc} {ans - B}')

# perm(0, 0)
# 첫 반복: N이 5가 될 때까지 -> 1+3+3+5+6 == 18: perm(5,18)
# shelf==18 > B==16 이므로 line13: ans = min(ans, shelf), return
# perm(4, 12) 상태로 return (line23)
# line23: perm(member+1, shelf) -> perm(5, 12)
# member == N 이므로 return
# line23: perm(member+1, shelf) -> perm(5, 12)
# perm(3, 7)