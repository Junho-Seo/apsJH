# 정렬 종류 및 예제 참고: https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# sort, sorted 정리: https://velog.io/@turningtwenty/PYTHON-sort-sorted-%EC%99%84%EB%B2%BD%EC%A0%95%EB%A6%AC
# 노션 D21 분할정복 참고

N = int(input())
nums = list(int(input()) for _ in range(N))

# O(N^2) 시간복잡도

# 버블 정렬: 앞에서부터 인접한 두 수를 비교하여 제일 큰 값(맨 뒤)부터 완성
for i in range(N-1):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in range(N):
    print(nums[i])

# 선택 정렬: 가장 작은 값을 찾아 맨앞과 교환
# for i in range(N):
#     min_idx = i
#     for j in range(i+1, N):
#         if nums[j] < nums[min_idx]:
#             min_idx = j
#
#         nums[i], nums[min_idx] = nums[min_idx], nums[i]
#
# for i in range(N):
#     print(nums[i])

# 삽입 정렬: 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입
# for i in range(1, N):
#     for j in range(i, 0, -1):
#         if nums[j-1] > nums[j]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]
#
# for i in range(N):
#     print(nums[i])

#-------------------------------------------------------------
# O(N*logN) 시간복잡도

# 병합 정렬: 분할 정복과 재귀를 이용한 알고리즘
# 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬

def merge_sort(arr):
    # 리스트의 길이가 1이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    # 재귀적으로 왼쪽 절반과 오른쪽 절반을 정렬
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort((arr[mid:]))

    # 두 리스트를 병합할 결과 리스트 초기화
    merged_arr = []
    # 왼쪾 리스트와 오른쪽 리스트의 인덱스
    l = h = 0
    # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
    merged_arr += low_arr[l:]
    # 오른쪽 리스트에 남은 요소들을 결과 리스트에 추가
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr

ans = merge_sort(nums)
# print(*ans, sep='\n')
for i in range(len(ans)):
    print(ans[i])


# 퀵정렬: 병합 정렬이 균등하게 분할하였다면 pivot을 설정하여 그 기준으로 정렬.
# 추가적인 메모리 공간이 필요없다는 장점. 대용량 데이터를 처리 가능

# 예제 코드
# 피벗: 중간 요소로 설정
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화할 수 있습니다.
arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 다른 예제 코드
array = [8, 4, 6, 2, 5, 1, 3, 7, 9]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    print(front_arr, pivot_arr, back_arr)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

array = quick_sort(array)
print("after:", array)

'''
[4, 2, 1, 3] [5] [8, 6, 7, 9]
[] [1] [4, 2, 3]
[] [2] [4, 3]
[] [3] [4]
[6] [7] [8, 9]
[8] [9] []
after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''