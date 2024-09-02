# 비트연산을 이용한 풀이
def inorder(v): # 중위순회
    global pwd
    if v<8:
        inorder(v*2)
        pwd += str(tree[v])
        inorder(v*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    txt = input()
    print(f'#{tc}', end = ' ')
    for x in txt:
        asc = ord(x)
        tree = [0] * 8
        for i in range(1, 8):
            if asc & (1<<7-i):
                tree[i] = 1
            else:
                tree[i] = 0
        pwd = ''
        inorder(1)
        print(pwd, end = ' ')
    print()
