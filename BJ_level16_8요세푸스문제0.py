# check : deque의 rotate 기능!

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
q = deque(range(1, N+1))

ans = []

while q:
    # for _ in range(K-1):
    #     q.append(q.popleft())
    # 11, 12번 라인을 deque의 rotate 기능으로 처리
    # rotate(n)은 deque의 요소를 양수면 오른쪽으로, 음수면 왼쪽으로 n번 회전
    q.rotate(-(K-1))
    ans.append(str(q.popleft()))

print(f'<{", ".join(ans)}>')


'''
N = 7, K = 3
1 2 3 4 5 6 7
append 1
append 2
pop 3
append 4
append 5
pop 6
append 7
q = 


pop 2
pop 7
pop 5
pop 1
pop 4

첫 순회: q[N보다 작은 K의 배수] pop
다음 순회: K - (N % K) 부터 K의 배수 pop


'''