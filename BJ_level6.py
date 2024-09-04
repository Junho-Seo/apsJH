# 25083	 새싹

# print('         ,r\'"7')
# print("r`-_   ,'  ,/")
# print(' \. ". L_r\'')
# print('   `~\/')
# print('      |')
# print('      |')

# 	3003	 킹, 퀸, 룩, 비숍, 나이트, 폰

# arr = list(map(int,input().split()))
# need = [1, 1, 2, 2, 2, 8]
# ans = [0]*6
# for i in range(6):
#     if arr[i] != need[i]:
#         ans[i] = need[i] - arr[i]
#     else:
#         ans[i] = 0
#
# print(*ans)

# 2444	 별 찍기 - 7
# 10을 넣으면 1 3 5 7 9 7 5 3 1

# N = int(input())
#
# for i in range(1, N):
#     print(' '*(N-i)+'*'*(2*i-1))
# for i in range(N, 0, -1):
#     print(' '*(N-i)+'*'*(2*i-1))

# 10988	 팰린드롬인지 확인하기
# # check
# word = input()
# N = len(arr)
# ans = 1
#
# for i in range(N//2):
#     if word[i] != word[-1-i]:
#         ans = 0
#         break
# print(ans)
# # 다른 풀이
# arr = input()
# if arr == arr[::-1]:
#     print('1')
# else:
#     print('0')

# 1157	 단어 공부
# # check
# word = input().upper()  # 전부 대문자로 변경
# word_list = list(set(word))  # set를 이용하여 중복 제거
# cnt = []
#
# for i in word_list: # word_list를 순회하며
#     count = word.count(i)  # word에 word_list의 해당 글자 수 count
#     cnt.append(count)  # count한 글자 수 cnt에 추가
# if cnt.count(max(cnt)) >= 2:    # cnt의 최대값이 두 개 이상이라면
#     print("?")
# else:
#     # word_list의 인덱스를 기준으로 count 했으므로
#     # cnt의 최대 값의 index와 같은 index에 있는 word_list의
#     # 알파벳을 print
#     print(word_list[(cnt.index(max(cnt)))])

# 	2941	 크로아티아 알파벳
# # check
# word = input()
# cro_al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# for i in cro_al:
#     # 다른 변수에 replace를 선언할 경우 원본 값을 바꾸지 않는다.
#     # ex. ljes=njak
#     # word2 = word.replace(i, '*')
#     word = word.replace(i, '*')
# # print(len(word2)) # 9 (오답)
# print(len(word))  # 6 (정답)

# 1316	 그룹 단어 체커
# # check
# T = int(input())
# cnt = T
#
# for _ in range(T):
#     word = input()
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             continue
#         elif word[i] in word[i+1:]:
#             cnt -= 1
#             break
# print(cnt)
# 다른 풀이
# n = int(input())
#
# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
#         if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
#             new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
#                 error += 1  # error에 1씩 증가.
#     if error == 0:
#         group_word += 1  # error가 0이면 그룹단어
# print(group_word)

