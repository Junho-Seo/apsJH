# 단계별 풀어보기 11. 브루트포스
# 2231 분해합 B2
# check 슬라이싱+리스트를 사용했다..!
n = int(input())
result = 0

# 1부터 입력값까지의 모든 수 탐색
for i in range(1, n+1):
    # i값을 각 자리수로 슬라이싱하여 리스트로 만든다.
    nums = list(map(int, str(i)))
    # i와 i의 각 자리수의 합
    result = i + sum(nums)
    if result == n:
        print(i)
        # 가장 작은 수(처음 나오는 생성자)를 출력 후 break로 for문 탈출
        # break를 하지 않으면 다른(더 큰) 생성자 출력
        break
    # 예외 처리
    # i가 입력값까지 가면 생성자가 없는 것이므로 0 출력
    if i == n:
        print(0)

# ----------------------------------------
# gpt 최적화 코드
# 1. 탐색 범위를 줄인다.
#   - N의 생성자 M은 N보다 클 수 없고 N의 자릿수 합만큼 더 작아질 수 있다.
#   - N-(N의 자릿수 합) 정도까지 탐색 범위를 줄일 수 있다.
#   - N이 123이라면 최소 생성자는 123-6 = 117 부터 확인
# 2. 효율적인 계산
#   - sum(map(int, str(i))) 대신 각 자리수를 직접 구한다.
#   - 추가적인 리스트 생성 및 매핑 작업을 줄일 수 있다.

n = int(input())

# 탐색 범위 줄이기
# n - (n의 자릿수 합) ~ n 범위에서 탐색
start = max(1, n - (len(str(n)) * 9))

for i in range(start, n + 1):
    # 각 자리수 합을 계산하는 대신 직접 구하기
    digit_sum = i + sum(int(digit) for digit in str(i))

    if digit_sum == n:
        print(i)
        break
else:
    print(0)
