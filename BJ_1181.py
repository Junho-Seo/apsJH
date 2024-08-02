# 1181. 단어 정렬
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 1. 중복 제거 (리스트 컴프리헨션 활용)
# 2. 정렬

N = int(input())
words = {input() for _ in range(N)}
# words.sort()      # set은 sort가 없어서 안된다
# sorted: iterable 한 것만 넣어주면 정렬한 리스트를 반환한다.
sorted_words = sorted(words, key = lambda word: (len(word), word))

for word in sorted_words:
    print(word)

# 혹은 for word in sorted(words, key = lambda word: (len(word), word)):
#    print() 으로 위의 3줄을 2줄로 가능

# 백준 시간초과 많이 줄이는 방법
# input stdin readline 사용
# import sys
# input = sys.stdin.readline
# python3 대신 pypy로도 제출해보기


# 내 풀이 (fail)
# N = int(input())
# words = []
# for word in range(N):
#     word = list(map(str, input().split()))
#     words += word
#
# sorted_words = sorted(words, key=lambda el: (len(el), el))
# print(sorted_words)
