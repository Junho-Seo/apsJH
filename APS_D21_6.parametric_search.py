# 이진 검색의 응용
# 면접 질문에서 현재는 거의 나오지 않는 주제
# 필요하다면 lower bound, upper bound 키워드로 검색 및 학습해보자

arr = [2, 4, 7, 9, 9, 9, 9, 11, 19, 23]
# 이진 탐색은 정렬된 데이터에 적용 가능하다.
# arr.sort()


def lower_bound(x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left


x = 9
first = lower_bound(x)
last = upper_bound(x)
print(first, last, arr[first:last])

print('----------------------------')
print('5 ~ 10사이의 값은 몇개가 있을까 ?')
first = lower_bound(5)
last = upper_bound(10)

print(first, last, arr[first:last])