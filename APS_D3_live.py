# 배열(Array)2
# 2차원 배열

# 0으로 채운 1차원 배열 (빈 배열)
arr1 = [0] * 3
# 출력
print(arr1)
print(*arr1)

# 2차원 배열은?
arr2 = [[0] * 3 for _ in range(2)]      # 2행 3열
# 출력
for i in range(2):
    print(*arr2[i])

# 출력 방법 2
for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = ' ')
    print()

# 참고
arr = [[1, 2, 3], [4, 5, 6]]
print(len(arr))     # 2 (행의 길이)
print(len(arr[0]))      # 3 (0번 행의 열의 길이)

# 이렇게 하면 안된다!
arr = [[0]*3]*2
print(arr)      # [[0, 0, 0], [0, 0, 0]]
arr[0][0] = 1   # 0행 0열 index를 바꾸려고 한다.
print(arr)      # [[1, 0, 0], [1, 0, 0]] (둘 다 1로 바뀌어버린다!)