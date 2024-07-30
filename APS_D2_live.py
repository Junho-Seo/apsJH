# list 1 2번째 시간
# 카운팅 정렬, 완전검색, 그리디

# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
# 에서 배열 원소 Ai의 크기가 |Ai| <= 10000 이라면?
# 생각해보기

# 카운팅 정렬

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5                            # DATA가 0~4까지의 정수

N = len(DATA)                               # DATA의크기
TEMP = [0] * N                              # 정렬 결과 저장

# 1단계 : DATA 원소 별 개수 세기
for x in DATA:                              # DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):                       # COUNT[1]~COUNT[4]까지 누적 개수
    COUNTS[i] += COUNTS[i-1]

# 3단계 : DATA의 맨 뒤부터 TEMP에 정렬하기
for i in range(N-1, -1, -1):                # N-1부터 0까지 1씩 감소
    COUNTS[DATA[i]] -= 1                   # 누적 개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]         # COUNTS[DATA[i]]를 인덱스로 사용한다는 의미

print(*TEMP)

# 3단계에서 뒤부터 하는 이유?
# 다시보기 2시간 35분쯤