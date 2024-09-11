'''
춘추 전국 시대는 여러 국가간의 전쟁과 동맹이 난무하던 시대였습니다.
한 때에는 N개의 국가가 존재하며, 각 국가들은 P명의 인구 수를 가지고 있습니다.
예를들어 A부터 G까지 7개의 나라가 있다고 하고 각 국가의 인구 수는 다음과 같다고 가정합시다.
A : 10
B : 20
C : 30
D : 40
E : 50
F : 60
G : 70
B와 D는 동맹을 맺고, A와 C와 F가 동맹을 맺었다고 가정해 봅시다.
동맹을 맺은 국가끼리는 전쟁을 일으키지 않으며, 동맹을 파기하는 일 또한 없습니다.
이러한 상황에서, B연합군(D + B)와 A연합군(A + C + F)이 전쟁을 하게 된다고 합시다.

이런 상황에서는 둘 중 연합군의 인구수가 더 큰 국가가 승리합니다.
B연합군의 인구 수는  60 (D + B), A연합군의 인구 수는 100 입니다. (A + C + F)
이 전쟁에서 B연합군의 국가들은 멸망하고, 살아남은 국가의 수는 5개가 됩니다. (A, C, E, F, G)
만약 두 국가의 인구 수가 동일하다면, 두 국가 모두 멸망합니다.
춘추 전국 시대의 여러 동맹과 전쟁 이후 살아남은 국가의 수를 출력해 주세요.

[입력]

첫번째 줄 테스트케이스의 수 T 를 입력 받습니다.

각 테스트 케이스의 첫번째 줄에 각 국가의 수 N을 입력 받습니다. (2 <= N <= 25)

두번째 줄에 N개 각 국가의 인구 수를 입력 받습니다. 인구의 수는 0 이상, 100,000 이하입니다.

세번째 줄에 동맹과 전쟁의 상황의 개수 T를 입력 받습니다. (1 <= T <= 100)

그 후의 T개의 줄에는 상황, 국가 A, 국가 B를 한 줄로 입력 받습니다.

상황에서 "alliance"는 동맹, "war"은 전쟁을 의미합니다.

[출력]

첫번째 줄에 동맹과 전쟁 이후 살아남은 국가의 개수를 테이스의 케이스 번호와 함께 출력합니다.

[testcase input]
2
7
10 20 30 40 50 60 70
5
alliance A C
alliance F C
alliance D B
alliance A F
war D F
3
38481 86027 89663
2
war A B
war B C

[testcase output]
#1 5
#2 1
'''


def find(node):
    # if parents[node] == node:
    #     return node
    #
    # parents[node] = find(parents[node])
    # return parents[node]

    if parents[node] != node:
        parents[node] = find(parents[node])  # 경로 압축
    return parents[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    # if root_x == root_y:
    #     return
    #
    # # root_x 가 연합의 대표
    # parents[root_y] = root_x
    # # 대표의 인구수에 연합 인구수 합산
    # population[root_x] += population[root_y]
    # # 합산 후 연합된 국가의 인구수 0으로 저장
    # population[root_y] = 0

    if root_x != root_y:
        parents[root_y] = root_x
        # 대표의 인구 수에 연합 인구 수 합산
        population[root_x] += population[root_y]
        # 합산 후 연합된 국가의 인구수 0으로 저장
        population[root_y] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    population = list(map(int, input().split()))
    parents = [i for i in range(N)]

    Q = int(input())
    for i in range(Q):
        status, c1, c2 = map(str, input().split())
        # 국가 이름을 아스키 코드로 변환 (인덱스 번호로 변경)
        c1 = ord(c1) - 65
        c2 = ord(c2) - 65

        if status == 'alliance':
            union(c1, c2)

        elif status == 'war':
            root_c1 = find(c1)
            root_c2 = find(c2)
            # 두 국가가 서로 다른 연합(대표자)이라면 전쟁 발생
            if root_c1 != root_c2:
                # c2 연합이 패배, c2 연합 국가 모두 멸망
                if population[root_c1] > population[root_c2]:
                    for i in range(N):
                        if find(i) == root_c2:
                            population[i] = 0
                # c1 연합이 패배, c1 연합 국가 모두 멸망
                elif population[root_c1] < population[root_c2]:
                    for i in range(N):
                        if find(i) == root_c1:
                            population[i] = 0
                # 인구 수가 같을 때, 둘 다 멸망
                else:
                    for i in range(N):
                        if find(i) == root_c1 or find(i) == root_c2:
                            population[i] = 0

    # 살아남은 국가의 수
    # find(i)로 연합의 대표를 찾아 대표 인덱스의 인구가 0이 아니면 cnt+1
    cnt = 0
    for i in range(N):
        if population[find(i)] > 0:
            cnt += 1
    # cnt = sum(1 for i in range(N) if population[find(i)] > 0)
    print(f"#{tc} {cnt}")
