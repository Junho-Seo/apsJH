# 1. 정렬 설명(버블, 카운팅 구현)
# 2. 디버깅 방법
# 3. DAT 설명

# shift + f10 : 기존에 실행했던 파일을 바로 실행
# ctrl + shift + f10: 현재 내 파일을 실행

# sort : Timsort(하이브리드 정렬) o(NlogN) 이 보장된다!
# - 알고리즘 문제 풀 때에는 적극적으로 활용하자.
# - 수업에는 정렬 기본적인 구현을 설명한다.
#   - 코드를 외우지 말고, 그림(원리)만 이해하면 된다.


numbers = [1, 3, 5, 2, 4, 9, 7, 5, 3, 3, 2]
length = len(numbers)

# 버블 정렬: 뒤에서부터 하나씩 확정
# 전체를 반복하면서 2개씩 비교 -> 무조건 이중 for문을 사용해야한다 -> O(N^2)
bubbles = numbers[:]    # 얕은 복사 -> 일차원까지만 새로운 배열을 생성. (슬라이싱을 이용한 방법)
                        # 따라서 1차원 배열에서는 사용해도 됨. (원본 변경 안됨)

for i in range(length - 1, 0, -1):  # 반복문 작성시에는 그림 그리면 빠름 (숙달되면 머리에서 바로 가능)
    # 비교하는 연산은 0~i 까지
    for j in range(0, i):
        # 두 개씩 비교(오름차순 '>' / 내림차순 '<' )
        if bubbles[j] > bubbles[j + 1]:
            bubbles[j], bubbles[j + 1] = bubbles[j + 1], bubbles[j]  # 위치 바꾸기 쉽다(파이썬)
print(bubbles)


# 디버깅 사용법 및 단축키 mm 확인


# 카운팅 배열
# DAT(Direct Address Table) 자료 구조
# - 배열의 index에 의미를 부여하는 구조
# - ex) 카운팅 배열의 counts[2] ==> 2번 index의 의미: 2의 개수를 의미

data = numbers[:]
counts = [0] * (max(data) + 1)  # index라 최대값 "+ 1" 해줌

# 1. 각 숫자의 개수(여기서는 num)를 counts 배열에 입력
for num in data:
    counts[num] += 1

# 2. counts 배열 -> 누적합 배열로 수정
for i in range(1, len(counts)):
    counts[i] += counts[i - 1]

# 3. temp 배열을 완성
#   - 원본 배열을 뒤에서부터 순회
#   - 3.1 counts 배열에서 해당 숫자의 index를 가져온다.
#   - 3.2 temp의 index 자리에 숫자를 넣어준다 + counts 배열 -= 1

temp = [0] * length
for i in range(length - 1, -1, -1):
    target = data[i]    # 자리를 찾고자 하는 숫자
    counts[target] -= 1     # 1을 미리 뺴준다.

    find_index = counts[target]     # 자리를 찾아서
    temp[find_index] = target      # temp의 해당 자리에 숫자를 넣어준다
print(temp)

# 시간 복잡도 계산
# 실제 연산(N + N + K)
#   - N: 정렬하고자 하는 데이터의 길이
#   - K: 데이터의 최대값 (최대값이 크면 못 쓴다!!)
#       - ex) numbers = [1, 50000000] -> 카운팅에서 이미 5000만회 수행
# 빅오표기법: O(N + K)
# 주의. K가 크면 못 쓴다!!

# 참고. 파이참 디버그 툴
# 디버깅(Debugging): 코드의 버그를 수정하는 과정
#   - Pycharm 같은 IDE 에서는 디버깅을 잘 할 수 있도록 디버깅 도구를 지원해준다.
# 디버그 툴 단축키
# - 링크: https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf
# ------------------------ 디버그 시작 전
# - Ctrl + F8(Breakpoint): 중단점 설정
# - Shift + F9: 디버깅 시작
# - Ctrl + F2: 디버그 종료
# ------------------------ 디버그 실행 중
# - F8(Step Over): 한 줄 실행. 함수내부로 이동하지 않음
# - F7(Step Into): 한 줄 실행. 함수라면 함수 내부로 이동
# - Shift + F8: 현재 커서 기준 함수 밖으로 나옴
# - F9(Resume): 다음 중단점까지 코드 실행
