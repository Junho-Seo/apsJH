# union 으로 동맹 결성

# 동맹들의 인구수 합을 구한 후 비교

def find(node):
    if parents[node] == node:
        return node

    parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    parents[root_x] = root_y

    # if root_x < root_y:
    #     parents[root_y] = root_x
    # else:
    #     parents[root_x] = root_y

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    population = list(map(int, input().split()))
    parents = [i for i in range(N)]

    Q = int(input())
    for i in range(Q):
        status, c1, c2 = map(str, input().split())
        if status == 'war':
            pass
            # A = find(ord(c1)-65)
            # B = find(ord(c2)-65)
            # parents.index(A)

        elif status == 'alliance':
            union(ord(c1)-65, ord(c2)-65)
    print(parents)