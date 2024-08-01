def binary_search(target):
    left, right = 1, 50
    middle = -1
    cnt = 0

    while middle != target:
        middle = (left + right) // 2

        if target < middle:
            right = middle - 1
        else:
            left = middle + 1

        cnt += 1

    print(f'{cnt}번 만에 검색 완료!')


binary_search(37)
binary_search(12)
binary_search(3)
binary_search(1)
binary_search(14)