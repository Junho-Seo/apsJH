# 21777. 큐(queue) 연습하기
# 문법 복습.(input부분)


"""
Python에서 큐를 구현하는 방법은 크게 3가지
1. 리스트 이용 (기본 사용법)
2. deque 모듈 (코테 필수 모듈)
3. queue 모듈 (멀티쓰레드 개념 학습 후 본격적 활용 연습 가능)

사용자로부터 명령어 수 N을 입력받는다.
N번만큼 반복하며 아래 조건에 맞도록 명령을 수행하시오
"""

# 리스트를 사용한 큐 구현
N = int(input())
q = []

for _ in range(N):
    command = input().split()
    if command[0] == "enqueue":
        q.append(int(command[1]))
    elif command[0] == "dequeue":
        if not q:
            print(-1)
        print(q.pop(0))
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "isEmpty":
        if not q:
            print(1)
        else:
            print(-1)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "rear":
        if not q:
            print(-1)
        else:
            print(q[-1])

# deque 모듈을 이용한 큐 구현
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    command = input().split()
    if command[0] == "enqueue":
        q.append(int(command[1]))
    elif command[0] == "dequeue":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "isEmpty":
        if not q:
            print(1)
        else:
            print(-1)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "rear":
        if not q:
            print(-1)
        else:
            print(q[-1])





'''
10  # 명령어 수
enqueue 10
enqueue 20
enqueue 30
front
rear
dequeue
front
rear
isEmpty
size
'''