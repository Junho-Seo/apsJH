# 검색 (Search)

def selection_sort(arr, N):  # arr 정렬대상, N 크기
    for i in range(N - 1):  # 주어진 구간에 대해... 기준위치 i를 정하고
        min_idx = i  # 최솟값 위치를 기준위치로 가정
        for j in range(i + 1, N):  # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 구간의 최솟값을 검색 후 교환


A = [2, 7, 5, 3, 4]
B = [4, 3, 2, 1]
selection_sort(A, len(A))
selection_sort(B, len(B))

# 교안 연습문제3(달팽이 숫자)
# 유사문제 SC_List2_1954 파일 참고

# 정렬 복습 (버블, 카운팅, 선택)

numbers = [34, 24, 23, 55, 63, 29, 19, 3, 99, 45]


# 버블 정렬 O(N^2)
# 뒤에서부터 정렬
def bubble_sort(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            cnt += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, cnt


bubbles, cnt = bubble_sort(numbers[:])
print("Numbers: ", numbers)
print("Bubble Sort:", bubbles)
print("수행횟수: ", cnt)
print('------------------------------')
'''
Numbers:  [34, 24, 23, 55, 63, 29, 19, 3, 99, 45]
Bubble Sort: [3, 19, 23, 24, 29, 34, 45, 55, 63, 99]
수행횟수:  45
------------------------------
'''

# 카운팅 정렬 O(N+K) (응용 버전 -> DAT)
# counts 배열을 이용한 정렬
# 1. max를 구함
# 2. max값 만큼의 길이를 가진 counts 배열 완성
# 3. counts 배열을 순회하면서 temp(정렬된 배열)완성
def counting_sort(arr):
    cnt = 0

    # max_val = max(arr)
    max_val = arr[0]
    for num in arr:
        cnt += 1
        if num > max_val:
            max_val = num

    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1
        cnt += 1

    total = 0
    for i in range(max_val + 1):
        count[i], total = total, total + count[i]
        cnt += 1

    for num in arr:
        output[count[num]] = num
        count[num] += 1
        cnt += 1

    return output, cnt


counts, cnt = counting_sort(numbers[:])
print("Numbers: ", numbers)
print("Counting Sort:", counts)
print("수행횟수: ", cnt)
print('------------------------------')
'''
Numbers:  [34, 24, 23, 55, 63, 29, 19, 3, 99, 45]
Counting Sort: [3, 19, 23, 24, 29, 34, 45, 55, 63, 99]
수행횟수:  130
------------------------------
'''

# 선택 정렬 O(N^2)
# 1. numbers를 순회하면서
# 2. 가장 작은 값을 찾아서, 현재 위치 숫자와 자리를 변경
def selection_sort(arr):
    N = len(numbers)
    cnt = 0  # 연산 횟수 계산하기 위해 반복문 돌 때마다 1씩 추가
    # 위치값(인덱스값)이 필요하기 때문에 반복문을 range로 구현
    for i in range(N):
        min_idx = i  # 최소값을 가진 인덱스를 i로 가정
        for j in range(i + 1, N):
            cnt += 1
            if arr[j] < arr[min_idx]:  # 등호를 넣으면 같은값도 바꿔버린다. 쓸데없는 연산 추가됨.
                min_idx = j  # 최소값을 찾아 min_idx로 넣어준다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 찾은 값의 위치를 바꿔준다.
        cnt += 1

    return arr, cnt


selections, cnt = selection_sort(numbers[:])
print("Numbers: ", numbers)
print("Selections Sort:", selections)
print("수행횟수: ", cnt)
print('------------------------------')
'''
Numbers:  [34, 24, 23, 55, 63, 29, 19, 3, 99, 45]
Selections Sort: [3, 19, 23, 24, 29, 34, 45, 55, 63, 99]
수행횟수:  55
------------------------------
'''

# '수'의 범위가 좁을수록 counting sort가 유리 (연산 횟수; 시간 복잡도 기준)


# 이진 탐색
#   - 탐색의 범위를 반씩 줄여나가며 탐색하는 기법 (병뚜껑 게임)
#   - 주의. 반드시 정렬된 데이터를 사용하여야 한다!!!
#   - 시간상으로 얼마나 걸릴까?
#    - 1~50 예시
#    - 25? up
#    - 다음 탐색 범위: 26 ~ 50 -> 38? down
#    - 다음 탐색 범위: 26 ~ 37 -> 31? up
#    - 다음 탐색 범위: 31 ~ 37 -> 34? up
#    - 다음 탐색 범위: 35 ~ 37 -> 36? up
#    - 다음 탐색 범위: 36 ~ 37 -> 37? 정답!
#    - 6번만에 정답(최악의 경우)
#   - 이진 탐색의 시간 복잡도(탐색 시간)는 O(logN)
#   - 총 걸리는 시간: 정렬 시간 (NlogN) + 탐색 시간(logN)

# 완전 탐색처럼 보이지만 데이터가
# N : 1 ~ 10억(말도 안 되는 수)  --> 이런 경우는 대부분 이진탐색(logN) 활용

def binary_search(target):
    left, right = 1, 50
    middle = -1  # 아무 수나 넣어도 됨. 선언.
    cnt = 0  # 탐색 횟수

    while middle != target:  # 절반값이 target이 될 때 까지 반복
        middle = (left + right) // 2

        if target < middle:  # 작은 범위 탐색
            right = middle - 1
        else:  # 큰 범위 탐색
            left = middle + 1

        cnt += 1  # while문 돌 때마다 1씩 추가

    print(f'{cnt}번 만에 검색 완료!')


binary_search(37)
binary_search(12)
binary_search(3)
binary_search(1)
binary_search(14)
binary_search(50)
'''
6번 만에 검색 완료!
2번 만에 검색 완료!
4번 만에 검색 완료!
5번 만에 검색 완료!
6번 만에 검색 완료!
6번 만에 검색 완료!
'''

def my_abs(num):
    if type(num) == type(1) or type(num) == type(1.0): # 정수 혹은 실수인 경우
        if num >= 0: return num
        else: return -num
    elif type(num) == type(1j): # 복소수인 경우
        return (num.real ** 2 + num.imag ** 2) ** (1/2)
    else: # 숫자가 아닌 경우
        raise TypeError('숫자를 입력해 주세요!')