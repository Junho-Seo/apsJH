# 5432. 쇠막대기 자르기
# 성빈님 코드참고

import sys
sys.stdin = open("input5432.txt", "r")
sys.stdout = open("output5432.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    steel = list(input())
    N = len(steel)

    for i in range(N - 1):
        # 레이저를 표현하는 '()'를 숫자 1로 변환하여 레이저를 구분
        if steel[i] == '(' and steel[i + 1] == ')':
            steel[i], steel[i + 1] = 1, 1

    cnt = 0  # 현재 쇠막대기 층의 개수
    ans1 = 0  # 잘려진 조각의 개수 (레이저로 인해 추가되는 조각)
    ans2 = 0  # 닫힌 괄호에 의해 최종적으로 잘려지는 조각의 개수
    for i in range(N):
        if steel[i] == '(':  # 새로운 쇠막대기의 시작
            cnt += 1  # 쇠막대기 층수 증가
        elif steel[i] == 1:  # 레이저를 만나면
            ans1 += cnt  # 현재 층수만큼 잘려진 조각 추가
        elif steel[i] == ')':  # 쇠막대기의 끝
            cnt -= 1  # 층수 감소
            ans2 += 1  # 최종적으로 잘려지는 조각 수 증가

    # 레이저로 잘려진 조각 수 + 쇠막대기의 끝에 의해 잘려지는 조각 수
    result = ans1 // 2 + ans2
    print(f'#{tc} {result}')

# 최적화 코드
T = int(input())  # 테스트 케이스의 수 입력
for tc in range(1, T + 1):
    steel = input().strip()  # 각 테스트 케이스마다 괄호 표현을 입력받음
    cnt = 0  # 현재 쇠막대기 층의 개수
    result = 0  # 최종 잘려진 조각 수

    i = 0
    while i < len(steel):
        if steel[i] == '(':
            if steel[i + 1] == ')':  # 레이저인 경우
                result += cnt  # 현재 층수만큼 조각 추가
                i += 1  # 레이저를 두 개의 문자로 처리하므로 인덱스 추가
            else:
                cnt += 1  # 쇠막대기의 시작이므로 층수 증가
        else:
            cnt -= 1  # 쇠막대기의 끝이므로 층수 감소
            result += 1  # 잘려진 조각 하나 추가
        i += 1

    print(f'#{tc} {result}')  # 결과 출력
