arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    for i in range(n):
        if tar & 0x1:   # 마지막 한 자리가 1인지 0인지 검사
            print(arr[i], end=' ')
        tar >>= 1   # 검사한 자리를 제거


for tar in range(0, 1 << n):  # range(0, 8) 모든 부분집합 출력
    print('{', end=' ')
    get_sub(tar)
    print('}')


