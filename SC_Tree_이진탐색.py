# 21999. [파이썬 S/W 문제해결 기본] Tree Day2 - 이진탐색

def binary_tree(num):
    p = 1
    c = p * 2
    while c <= num:
        graph[p].append(c)
        if c + 1 <= num:
            graph[p].append(c + 1)
        p += 1
        c = p * 2


def bt_lst(num):
    if len(graph[num]) == 0:
        arr.append(num)
        return
    if len(graph[num]) == 1:
        bt_lst(graph[num][0])
        arr.append(num)
    elif len(graph[num]) == 2:
        bt_lst(graph[num][0])
        arr.append(num)
        bt_lst(graph[num][1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    arr = []
    tree = [0] * (N + 1)

    binary_tree(N)
    bt_lst(1)

    for i in range(N):
        tree[arr[i]] = i + 1
    print(f'#{tc}', tree[1], tree[N // 2])