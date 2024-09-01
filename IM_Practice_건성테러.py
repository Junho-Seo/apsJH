# 테스트 케이스의 수를 입력받습니다.
t = int(input())

# 각 테스트 케이스에 대해 처리합니다.
for tc in range(1, t + 1):
    # 세로 크기(N)와 가로 크기(M)를 입력받습니다.
    n, m = map(int, input().split())
    # 폭탄의 화력(K)을 입력받습니다.
    k = int(input())
    # 초기 폭발 전 상태를 입력받아 2차원 리스트로 저장합니다.
    graph = [list(input().strip()) for _ in range(n)]

    # 상하좌우와 제자리 폭발을 위한 방향 벡터입니다.
    dxs = [0, 0, 1, -1, 0]
    dys = [1, -1, 0, 0, 0]

    # 폭발 범위를 기록하기 위한 배열을 초기화합니다.
    exploded = [[0] * m for _ in range(n)]

    # 폭탄 위치를 순회하면서 폭발 범위를 기록합니다.
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "@":
                # 제자리 포함 4방향으로 폭발 범위를 체크합니다.
                for direction in range(5):
                    for rg in range(k + 1):
                        nx, ny = i + dxs[direction] * rg, j + dys[direction] * rg
                        # 폭발이 격자 내에서 발생하며 벽이 없는 경우만 처리합니다.
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[nx][ny] == "#":
                                break  # 벽을 만나면 더 이상 진행하지 않음
                            exploded[nx][ny] = 1
                        else:
                            break  # 격자 밖으로 나가면 더 이상 진행하지 않음

    # 최종 상태를 계산하고 출력합니다.
    print(f"#{tc}")
    for i in range(n):
        for j in range(m):
            if exploded[i][j]:
                # 폭발이 발생한 위치는 '%'로 표시합니다.
                print('%', end='')
            else:
                # 그 외의 경우 원래 상태를 유지합니다.
                print(graph[i][j], end='')
        print()