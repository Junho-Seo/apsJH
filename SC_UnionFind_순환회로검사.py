# 키워드: 같은 그룹끼리 union 연산이 발생하면 싸이클이 발생한다!

def find(node):
    if node == parents[node]:
        return node

    return find(parents[node])

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 조건이 만족하면 싸이클이 발생
        # 싸이클 발생 시 False return
        return False

    parents[root_y] = root_x    # 병합
    return True                 # True 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    circuit = [list(map(int, input().split()))for _ in range(N)]

    parents = [i for i in range(N)]  # index 0부터 다 사용하므로 N

    is_cycle = True
    for i in range(N):
        for j in range(i+1, N):  # 우하단 대각선 기준으로 우측 반만 확인해야한다.(안 하면 에러)
            if circuit[i][j] == 0:  # 연결이 안되어 있다면 통과
                continue

            if union(i, j) is False: # i와 j가 같은 그룹이면 싸이클이 발생
                is_cycle = True
                break

        if is_cycle:
            break

    if is_cycle:
        print(f'#{tc} WARNING')
    else:
        print(f'#{tc} STABLE')

