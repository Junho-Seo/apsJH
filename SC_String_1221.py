# 1221 .[S/W 문제해결 기본] 5일차 - GNS
# 참조. https://unie2.tistory.com/1192

import sys
sys.stdin = open("input1221.txt", "r")
sys.stdout = open("output1221.txt", "w")

T = int(input())
# 문자열 데이터 리스트 생성
data = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for test_case in range(1, T+1):
    t, len = input().split()        # 케이스 번호, 단어 개수
    nums = list(input().split())    # 단어 문자열을 리스트로 받는다.
    # data 리스트에서 nums[i]에 해당하는 인덱스 번호로 nums[i] 갱신
    for i in range(int(len)):
        nums[i] = data.index(nums[i])
    # nums를 오름차순 정렬
    nums.sort()
    # data 리스트에서 muns[i]를 인덱스로 하는 문자열 값으로 nums[i] 갱신
    for i in range(int(len)):
        nums[i] = data[nums[i]]

    print(f'#{test_case}')
    print(*nums)

# 코드값을 활용한 풀이 찾아보기.