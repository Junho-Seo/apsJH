# check: enumerate 활용!

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
balloons = deque(enumerate(map(int, input().split())))

ans = []

while balloons:
    idx, paper = balloons.popleft()
    ans.append(idx+1)

    if paper > 0:
        balloons.rotate(-(paper - 1))   # 양수라면 오른쪽으로 회전
    elif paper < 0:
        balloons.rotate(-paper)  # 음수라면 왼쪽으로 회전

print(*ans)
# print(' '.join(map(str, ans)))
