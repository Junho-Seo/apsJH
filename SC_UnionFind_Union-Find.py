# "그룹" 이라는 키워드가 나오면 Union-Find를 생각해보자.
# union-find 시간복잡도 O(1). 정확히는 역 아커만 함수 N (궁금하면 찾아보기)

# 2. find-set (대표자 찾기)
def find(node):
    if parents[node] == node:
        return node

    # 기본 코드
    # return find(parents[node])

    # 경로 압축
    # 노드 수가 적을 때, 입력 자체가 안정적으로 들어오는 특수한 경우
    # 에는 경로 압축이 더 느릴 수 있다.
    # 대부분의 경우에는 경로 압축 하는것이 더 빠르다
    parents[node] = find(parents[node])
    return parents[node]

# 3. union (결합)
def union(x, y):
    root_x = find(x)    # x의 대표자를 탐색
    root_y = find(y)    # y의 대표자를 탐색

    if root_x == root_y:    # 대표자가 같으면 이미 같은 그룹에 속함
        return

    # 기본 코드
    parents[root_y] = root_x

    # 문제에서 x, y값의 크기가 중요하다면 아래와 같이 최적화
    # 이 문제에선 숫자 크기가 중요하지 않으니 쓸모없는 연산이 추가되는 꼴
    # if root_x < root_y:
    #     parents[root_y] = root_x
    # else:
    #     parents[root_x] = root_y


T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 1. 초기화 과정 make-set (집합 생성)
    parents = [i for i in range(N+1)]
    print(f'#{tc}', end=' ')
    for _ in range(Q):
        K, A, B = map(int, input().split())
        if K == 1:
            union(A, B)
        if K == 0:
            if find(A) == find(B):  # 대표자가 같으면 같은 그룹룹
               print('YES', end=' ')
            else:
                print('NO', end=' ')

    print()