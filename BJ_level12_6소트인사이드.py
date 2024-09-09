N = list(map(int, str(input())))

N.sort(reverse=True)

for i in N:
    print(i, end='')