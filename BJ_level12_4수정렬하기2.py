import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input())for _ in range(N))

nums.sort()
print(*nums, sep='\n')

