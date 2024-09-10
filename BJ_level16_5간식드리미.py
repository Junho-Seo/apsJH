import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
waiting = list(map(int, input().split()))

stack = []

# waiting의 앞부터 1이 나오면 pop,
# not stack 이면 nice

for i in waiting:
    stack.append(i)
    if stack[i] > stack[i+1]:
