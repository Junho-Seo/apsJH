import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dequeue = deque()

for _ in range(n):
    num = list(map(int, input().split()))

    if num[0] == 1:
        dequeue.appendleft(num[1])
    elif num[0] == 2:
        dequeue.append(num[1])
    elif num[0] == 3:
        print(dequeue.popleft() if dequeue else -1)
    elif num[0] == 4:
        print(dequeue.pop() if dequeue else -1)
    elif num[0] == 5:
        print(len(dequeue))
    elif num[0] == 6:
        print(0 if dequeue else 1)
    elif num[0] == 7:
        print(dequeue[0] if dequeue else -1)
    elif num[0] == 8:
        print(dequeue[-1] if dequeue else -1)