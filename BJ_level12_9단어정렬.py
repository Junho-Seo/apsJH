N = int(input())

words = [input()for _ in range(N)]

words = list(set(words))
words.sort()
words.sort(key=len)


for i in words:
    print(i)
