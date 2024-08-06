# 1216. [S/W 문제해결 기본] 3일차 - 회문2
'''
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

[제약사항]
각 칸의 들어가는 글자는 c언어 char type으로 주어지며
'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
가로, 세로 각각에 대해서 직선으로만 판단한다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며,
바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고,
공백 문자 후 찾은 회문의 길이를 출력한다.
'''

T = int(input())
for test_case in range(1, T+1):
    row_arr = [list(map(int, input().split())) for _ in range(100)]
    col_arr = list(map(list, zip(*row_arr)))
    len_pal = 0

    for i in range(100):        # i행
        # for j in range(100):
        #     for k in range(100):
                if arr[i][j + k] != arr[i][j + 99 - k]:




