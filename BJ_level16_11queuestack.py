import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# i번 자료구조가 큐이면 A[i] = 0
# i번 자료구조가 덱이면 A[i] = 1
# i번 자료구조에 들어있는 원소 B[i]
# queuestack에 삽입할 원소를 담고있는 수열 C

'''
예시
초기상태 [1, 2, 3, 4]
첫 번째 원소 삽입 [2, 2, 3, 1]
첫 번째 원소 삽입 [4, 2, 3, 2]
첫 번째 원소 삽입 [7, 2, 3, 4]
'''
