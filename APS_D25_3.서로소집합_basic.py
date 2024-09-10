def make_set(n):
    p = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
    return p

# 교안의 find_set() 대표자 찾기
def find(x):
    # x 자기 자신이 x를 바라본다 == 해당 집합의 대표자를 찾았다.
    if parents[x] == x:
        return x

    # x의 부모가 가리키고 있는 정점부터 다시 대표자를 탐색
    return find(parents[x])


def union(x, y):
    # x와 y의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노트에 합친다. (문제에 따라 바뀌는 부분)
    if root_x < root_y:
        parents[root_y] = root_x  # y가 바라보는 부모는 x의 대표자
    else:
        parents[root_x] = root_y


# 예제 사용법
n = 7  # 원소의 개수
parents = make_set(n)  # 집합 생성. parents에 부모 정보들을 저장

union(1, 3)
union(2, 3)
union(5, 6)

# 대표자의 수 == 집합의 수
print(parents)  # [0, 1, 1, 1, 4, 5, 5]

print('find_set(6) = ', find(6))  # find_set(6) =  5

target_x = 2
target_y = 3

# 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
if find(target_x) == find(target_y):
    print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
else:
    print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
# 원소 2과 원소 3는 같은 집합에 속해 있습니다.