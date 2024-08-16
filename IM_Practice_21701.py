# 21701. 기륜 선생님의 채점 방식은 독특해
# 석주님 풀이 비교해보기

'''
N명의 학생 M개의 문제
(최고점 - 최저점) 을 구하라

시험은 1부터 5까지의 5개의 항목 중, 정답을 선택하는 객관식으로 총 M개의 문제가 주어진다.

학생들이 제출한 답안지에는 각 문제에 대해 선택한 항목의 번호가 적혀 있다.

채점 방식은 다음과 같다.

 - 정답을 맞춘 문제는 1점이 주어진다.
 - 연속으로 정답을 맞출 경우, 이 전 점수에서 보너스 1점이 가산되어 주어진다.

M개의 문제에 대한 N명의 학생들의 답안지가 입력으로 주어졌을 때, 가장 높은 점수를 받은 학생과, 가장 낮은 점수를 받은 학생의 점수차를 출력하는 프로그램을 작성하라.

[제약사항]

3 <= N <= 30
2 <= M <= 40
정답 및 학생의 답안지로 입력되는 값은 1~5 사이의 정수이다.

[입력]

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다.

두번째 줄부터 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫번째 줄에는 학생의 수 N, 문제의 수 M이 공백으로 구분되어 주어진다.

각 테스트 케이스의 두번째 줄에는 M개의 문제에 대한 정답이 공백으로 구분되어 주어진다.

다음 N줄에 걸쳐, N명의 학생이 제출한 M개의 문제에 대한 답안지의 정보가 각 줄에 공백으로 구분되어 주어진다.

[출력]

각 테스트 케이 t에 대한 결과를 각 줄에 "#t" (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다.

해당 문제에 대한 코드를 작성해봤는데 수정할 부분을 한글 주석과 함께 작성해줘.
'''

import sys
sys.stdin = open("input21701.txt", "r")
sys.stdout = open("output21701.txt", "w")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())        # N 학생 수, M 문제 수
    answer = list(map(int, input().split()))    # 정답 리스트
    questions = [list(map(int, input().split()))for _ in range(N)]  # 문제 리스트 (NxM)
    students = [0] * N      # 학생별 총점 리스트 초기화

    for i in range(N):
        cnt = 0  # 연속 정답 횟수 초기화
        for j in range(M):
            if questions[i][j] == answer[j]:  # 정답인 경우
                cnt += 1
                students[i] += cnt      # i번 학생의 점수 채점
            else:  # 오답인 경우
                cnt = 0     # 연속 정답 횟수 초기화

    max_score = students[0]
    min_score = students[0]
    for max_val in students:        # 최대값
        if max_val > max_score:
            max_score = max_val
    for min_val in students:        # 최소값
        if min_val < min_score:
            min_score = min_val

    # max_score = max(students)
    # min_score = min(students)
    print(f'#{tc} {max_score - min_score}')
