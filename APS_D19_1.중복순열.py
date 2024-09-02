# 중복순열
path1 = []


def recur1(x):
    if x == 3:
        print(path1)
        return

    for i in range(1, 7):
        path1.append(i)
        recur1(x + 1)
        path1.pop()


recur1(0)

# 순열(중복 제거)
path2 = []
used = [0] * 7  # 1~6 숫자의 사용 여부를 기록할 리스트


def recur2(level):
    # 1. 기저 조건
    if level == 3:
        print(path2)
        return
    # 2. 후보군을 반복
    for i in range(1, 7):
        # i가 이미 뽑혔다면 continue (중복 제거 순열)
        # 아래 코드의 단점: "in" = O(len(path))
        # 시간 초과 위험도가 높다!
        # if i in path:
        #     continue

        # i가 이미 뽑혔다면 continue (중복 제거 순열)
        # 방문했다면 실행하지 마라
        # == 방문하지 않았다면 실행해라 if not used[i]:
        # 조건이 많아지면 코드가 난잡해지는데 continue를 이용하여 가독성을 높혔다(취향).
        if used[i] == 1:
            continue

        # 2.1 재귀 호출 전 - 사용 여부 체크 + 경로(이동할 위치) 기록
        used[i] = 1
        path2.append(i)
        # 2.2 다음 재귀 호출(파라미터 전달)
        recur2(level+1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제 + 사용 여부 초기화
        path2.pop()
        used[i] = 0


# recur2(0)    # 호출: 시작점을 같이 전달해주는 경우가 많다.
