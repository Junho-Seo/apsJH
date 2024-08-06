# 2005. 파스칼의 삼각형

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal = [[]*N for _ in range(N)]

    for i in range(N):

        for j in range(N):


'''
1       1
11      2
121     3
1331    4
14641   5
'''