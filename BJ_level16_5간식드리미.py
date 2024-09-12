import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
waiting = list(map(int, input().split()))

stack = []
target = 1
for i in waiting:
    stack.append(i)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if stack:
    print("Sad")
else:
    print("Nice")
