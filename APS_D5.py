# 문자열(string)
# 자주 쓰이는 유형
#   - 패턴 매칭 (다음 주 학습 예정)
#       - KMP, 보이어무어 --> 코테에서 절대 안나왔던 유형
#       - 다이나믹 프로그래밍(DP) => LIS, LCS
#   - 정렬 (우선순위)
#       - sort()
#   - 알파벳 카운팅, 문자 카운팅
#       - 문자 DAT 알고리즘

# sorted()  활용
numbers = [1, 3, 2, 4, 5, 4]
# numbers.sort()                       # 원본 배열을 '수정'
# sorted_numbers = sorted(numbers)     # 정렬된 배열을 '생성'
                                       # 생성하기 때문에 반환할 변수 필요

print(sorted(numbers))                     # [1, 2, 3, 4, 4, 5]
print(sorted(numbers, reverse=True))       # [5, 4, 4, 3, 2, 1]

words = ["cherry", "banana", "apple", "date", "abcd"]
# 문자열 정렬
print(sorted(words))                      # 오름차순 (사전순으로 정렬)
print(sorted(words, reverse=True))        # 내림차순

# 내가 원하는 조건으로 정렬
# 1. 길이로 정렬
print(sorted(words, key=len))
print(sorted(words, key=lambda w: len(w)))      # 위와 동일한 결과
# lambda: 익명함수.
# words의 요소 하나하나를 w(임의의 변수)로 복사하고 : 뒤에 기준조건을 작성.
# 기준조건을 2개 이상 동시에 하고싶다 --> lambda 활용!
#   ex. 1) 길이로 정렬 후 2) 같은 길이에서 오름차순으로 정렬
print(sorted(words, key=lambda w: (len(w), w)))    # 기준1. len(w): 길이, 기준2. w: 문자(사전순)


tuple_list = [("cherry", 1), ("banana", 3), ("apple", 2), ("date", 6), ("abcd", 5), ("aaaa", 7)]
# 문자열 길이순 ->  숫자 순
print(sorted(tuple_list, key=lambda el: (len(el[0]), el[1])))
# 문자열 길이순 -> 숫자 역순
print(sorted(tuple_list, key=lambda el: (len(el[0]), -el[1])))

# sort는 잘 활용할 수 있게 숙지하는게 중요하다
'''
# 백준 추천문제 '1181. 단어 정렬': sort 딸깍
# 1. 중복 제거 (리스트 컴프리헨션 활용)
# 2. 정렬

N = int(input())
words = {input() for _ in range(N)}
# words.sort()      # set은 sort가 없어서 안된다
# sorted: iterable 한 것만 넣어주면 정렬한 리스트를 반환한다.
sorted_words = sorted(words, key=lambda word: (len(word), word))

for word in sorted_words:
    print(word)

# 혹은 for word in sorted(words, key = lambda word: (len(word), word)):
#    print() 으로 위의 3줄을 2줄로 가능

# 백준 시간초과 많이 줄이는 방법
# 1. input() 대신 sys.stdin.readline 사용
#   (swea, 역테에서는 사용불가. import 지원 안함.)
# import sys
# input = sys.stdin.readline
# 2. python3 대신 pypy로도 제출해보기
'''

# 알파벳 수를 세어라
#   - counts 배열
#   -> 구현 방법 1. dictionary 활용
#   -> 구현 방법 2. 코드값을 활용(ASCII)(내장함수 ord 활용)

# print(ord('a'))  # 97
# print(ord('z'))  # 122
#
# print('a' < 'z')  # True. 내부적으로 코드값을 활용한다. (97 < 122)
# print('ab' < 'ac')  # True. 뒤쪽 알파벳일 수록 큼
# print('123' < '120')  # False. 뒤쪽 숫자일 수록 큼

words = 'asdfvdndcsdcwefklbdjfd'

# 'a'~'z' 까지 배열
# 쉬운 방법
cnt = [0] * 150  # 122 보다만 크게 생성
for w in words:
    # print(w, ord(w))
    cnt[ord(w)] += 1

print('a의 개수?', cnt[ord('a')])
print('f의 개수?', cnt[ord('f')])

# 효율적인 방법
cnt2 = [0] * 26
for w in words:
    cnt2[ord(w) - ord('a')] += 1

print('a의 개수 ? ', cnt2[ord('a') - ord('a')])
print('f의 개수 ? ', cnt2[ord('f') - ord('a')])
