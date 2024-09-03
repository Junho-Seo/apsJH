arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3


def run(lev, start):    # lev 번째는 start 부터 뽑아라
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)     # start는 i+1 부터 고려해라
        path.pop()


run(0, 0)
